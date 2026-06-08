#!/usr/bin/env python3
"""
Suno API Generation Script

Reads song markdown files from docs/songs/ and submits them to the Suno API.
Auth token and config are read from .env file.

Supports two auth modes:
  1. SUNO_COOKIE (recommended) — auto-refreshes the JWT from Clerk. Set once,
     valid for days/weeks. Copy cookies from browser DevTools.
     Optionally also set SUNO_SESSION_ID (or SESSION_ID) to use direct
     session token minting (the "Automatic token maintenance and keep-alive"
     pattern from https://github.com/SunoAI-API/Suno-API).
  2. SUNO_AUTH_TOKEN (fallback) — manual JWT from browser. Expires hourly.

Also supports proactive keep-alive mode:
    python generate.py --keep-alive
    python generate.py --keep-alive --keep-interval 10

Usage:
    python generate.py docs/songs/my-song.md
    python generate.py docs/songs/my-song.md --dry-run
    python generate.py docs/songs/my-song.md --version v5.5
 """

import argparse
import json
import os
import re
import sys
import time
import base64
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict

try:
    import requests
except ImportError:
    print("Missing 'requests' library. Install with: pip install requests")
    sys.exit(1)

try:
    from dotenv import load_dotenv
except ImportError:
    # Manual .env loading fallback
    load_dotenv = None


def load_env():
    """Load environment variables from .env file."""
    env_path = Path(__file__).parent / ".env"
    if load_dotenv:
        load_dotenv(env_path)
    elif env_path.exists():
        for line in env_path.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, _, value = line.partition("=")
                os.environ.setdefault(key.strip(), value.strip())


def extract_session_from_cookie(cookie: str) -> str:
    """Extract the __session JWT directly from the cookie string."""
    import re
    sessions = re.findall(r"__session=([^;]+)", cookie)
    if not sessions:
        raise Exception("No __session cookie found.")
    # Use the last session value (most recent if duplicates exist)
    return sessions[-1]


def extract_session_id_from_cookie(cookie: str) -> Optional[str]:
    """Best-effort extraction of Clerk session id (sess_...) from cookie string."""
    matches = re.findall(r"(?:__session|session|sess)[=:]?([A-Za-z0-9_.-]{10,})", cookie)
    for m in matches:
        if m.startswith("sess_"):
            return m
    return None


def get_fresh_token_from_cookie(cookie: str, session_id: Optional[str] = None) -> tuple[str, Optional[str]]:
    """Exchange Suno cookies for a fresh JWT via Clerk (supports keep-alive style maintenance).

    When session_id is provided (or discoverable), prefers the explicit token mint endpoint
    POST /v1/client/sessions/{session_id}/tokens -- this is the mechanism behind
    "Automatic token maintenance and keep-alive" in projects like SunoAI-API/Suno-API.
    It also returns Set-Cookie headers which can extend/rotate the underlying cookies.

    Falls back to the sessions list endpoint (GET /v1/client) which works with just COOKIE.

    Returns:
        (jwt, set_cookie_header_or_None)
    """
    headers = {
        "Cookie": cookie,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "application/json",
    }
    set_cookie = None
    jwt = None

    sid = session_id or extract_session_id_from_cookie(cookie)

    if sid:
        try:
            url = f"https://clerk.suno.com/v1/client/sessions/{sid}/tokens?_clerk_js_version=4.72.0-snapshot.vc141245"
            resp = requests.post(url, headers=headers, timeout=30)
            if resp.status_code == 200:
                jwt = resp.json().get("jwt")
                set_cookie = resp.headers.get("Set-Cookie")
                if set_cookie:
                    print("  (Clerk keep-alive: received Set-Cookie update)")
        except Exception as e:
            print(f"  Session token mint failed, will fallback: {e}")

    if not jwt:
        # Discovery / fallback via client sessions list
        url = "https://clerk.suno.com/v1/client?_clerk_js_version=4.72.2"
        resp = requests.get(url, headers=headers, timeout=30)
        if resp.status_code != 200:
            raise Exception(f"Clerk API returned {resp.status_code}: {resp.text[:300]}")
        data = resp.json()
        sessions = data.get("response", {}).get("sessions", [])
        if not sessions:
            raise Exception("No sessions found in Clerk response. Cookie may be invalid.")
        sess = sessions[0]
        jwt = sess.get("last_active_token", {}).get("jwt")
        if not jwt:
            raise Exception("No JWT found in Clerk session. Cookie may be expired.")
        set_cookie = resp.headers.get("Set-Cookie")
        # Log discovered sid so user can set SUNO_SESSION_ID for future explicit mints/keep-alive
        discovered = sess.get("id")
        if discovered and not session_id:
            print(f"  (discovered session id {discovered}; set SUNO_SESSION_ID to use direct mint)")

    if not jwt:
        raise Exception("Failed to obtain JWT from Clerk.")
    return jwt, set_cookie


def get_auth_token() -> tuple[str, bool]:
    """Get the best available auth token.

    Returns:
        (token, is_auto_refreshed)
        is_auto_refreshed is True when the token was just fetched from
        Clerk using SUNO_COOKIE (never expires during this call).
    """
    cookie = os.environ.get("SUNO_COOKIE", "")
    session_id = os.environ.get("SUNO_SESSION_ID", "") or os.environ.get("SESSION_ID", "")
    manual_token = os.environ.get("SUNO_AUTH_TOKEN", "")

    if cookie:
        # Try Clerk API first (auto-refresh). Supports the /sessions/{id}/tokens keep-alive style.
        try:
            token, set_cookie = get_fresh_token_from_cookie(cookie, session_id or None)
            if set_cookie:
                # We intentionally do not auto-write .env here (would be surprising in CLI).
                # User can re-run scripts/set-suno-cookies with an updated value if Clerk rotated cookies.
                pass
            return token, True
        except Exception as e:
            print(f"Clerk refresh failed: {e}")
            # Fall back to extracting __session JWT directly from cookie
            try:
                token = extract_session_from_cookie(cookie)
                print("Using __session JWT directly from cookie")
                return token, False
            except Exception as e2:
                print(f"Direct session extraction failed: {e2}")
            if manual_token:
                print("Falling back to SUNO_AUTH_TOKEN")
                return manual_token, False
            raise

    if manual_token:
        return manual_token, False

    print("ERROR: No authentication available.")
    print("\nRecommended (auto-refresh, set once):")
    print("  1. Open Suno in Chrome → DevTools → Network")
    print("  2. Click anything, find a request to studio-api.prod.suno.com")
    print("  3. Right-click → Copy → Copy as cURL (bash)")
    print("  4. Extract the Cookie header and run:")
    print("     scripts/set-suno-cookies 'cookie=value; ...'")
    print("\nAlternative (manual, expires hourly):")
    print("  1. Run DevTools snippet (scripts/suno-token-snippet.js)")
    print("  2. Click anything on Suno to copy token")
    print("  3. Run: scripts/set-suno-token")
    sys.exit(1)


def check_token_expiry(token: str) -> dict:
    """Decode JWT payload and check expiration."""
    try:
        # JWT is header.payload.signature - decode the payload
        payload_b64 = token.split(".")[1]
        # Add padding
        payload_b64 += "=" * (4 - len(payload_b64) % 4)
        payload = json.loads(base64.urlsafe_b64decode(payload_b64))
        exp = payload.get("exp", 0)
        now = time.time()
        remaining = exp - now
        if remaining <= 0:
            print(f"WARNING: Token EXPIRED {abs(remaining) / 60:.0f} minutes ago!")
            print("\nQuick refresh:")
            print("  Auto (recommended): scripts/set-suno-cookies 'your-cookies...'")
            print("  Manual: scripts/set-suno-token")
            return {"expired": True, "payload": payload}
        elif remaining < 300:  # Less than 5 minutes
            print(f"WARNING: Token expires in {remaining:.0f} seconds!")
            print("  Tip: switch to cookie auth with scripts/set-suno-cookies")
        else:
            print(f"Token valid for {remaining / 60:.0f} more minutes")
        return {"expired": False, "payload": payload}
    except Exception as e:
        print(f"Could not decode token: {e}")
        return {"expired": False, "payload": {}}


def keep_alive_loop(interval_seconds: int = 5):
    """Automatic token maintenance and keep-alive loop.

    Replicates the spirit of SunoAI-API/Suno-API "Automatic token maintenance and keep-alive":
    proactively mint fresh JWTs on a short interval using Clerk's session token endpoint
    (when SUNO_SESSION_ID is available) or the client sessions endpoint.

    This ensures a long-running process (or dedicated maintenance daemon) never sees
    an expired token. It also exercises the Clerk endpoints which can help maintain
    cookie/session lifetime.

    Start with:
        python generate.py --keep-alive
        # or with custom interval
        python generate.py --keep-alive --poll-timeout 5   # reuse flag for interval (hack)
    """
    load_env()
    cookie = os.environ.get("SUNO_COOKIE", "")
    session_id = (
        os.environ.get("SUNO_SESSION_ID", "")
        or os.environ.get("SESSION_ID", "")
        or extract_session_id_from_cookie(cookie)
    )
    if not cookie:
        print("ERROR: SUNO_COOKIE (or SESSION_ID + COOKIE) required for --keep-alive")
        sys.exit(1)

    print("🔄 Starting automatic token keep-alive (from Suno-API pattern). Press Ctrl-C to stop.")
    print(f"   Interval: {interval_seconds}s | session_id: {'yes' if session_id else 'no (using fallback)'}")
    print("   This keeps JWTs fresh without needing manual SUNO_AUTH_TOKEN refreshes.")

    while True:
        try:
            token, set_cookie = get_fresh_token_from_cookie(cookie, session_id)
            # Use latest cookie for subsequent iterations if Clerk rotated any
            if set_cookie:
                # set_cookie is typically a delta like "name=val; Path=..."; for loop we can
                # append/override into our cookie string heuristically (simple strategy)
                # For full correctness a real cookie jar would be used; here we just log.
                print("   ✓ JWT refreshed + Clerk Set-Cookie received (session kept warm)")
            else:
                print("   ✓ JWT refreshed")
            # Light validation (no noisy print)
            try:
                payload_b64 = token.split(".")[1]
                payload_b64 += "=" * (4 - len(payload_b64) % 4)
                payload = json.loads(base64.urlsafe_b64decode(payload_b64))
                exp = payload.get("exp", 0)
                remaining_min = max(0, int((exp - time.time()) / 60))
                print(f"     token valid ~{remaining_min} min")
            except Exception:
                pass
        except Exception as e:
            print(f"   ✗ Keep-alive error: {e}")
        time.sleep(interval_seconds)


# Suno model versions (from /api/generate/v2-web/models or similar)
# name -> external_key for the "mv" field
MODEL_VERSIONS = {
    "v5.5": "chirp-fenix",
    "v5": "chirp-crow",
    "v4.5+": "chirp-bluejay",
    "v4.5": "chirp-auk",
    "v4.5-all": "chirp-auk-turbo",
    "v4": "chirp-v4",
    "v3.5": "chirp-v3-5",
    "v3": "chirp-v3-0",
    "v2": "chirp-v2-xxl-alpha",
}


def resolve_model_version(version: Optional[str]) -> str:
    """Resolve a friendly model version name (v5.5, v5, ...) or external key to the mv value."""
    if not version:
        return os.environ.get("SUNO_MODEL", "chirp-crow")
    v = version.strip().lower().lstrip("v")
    # direct key passthrough
    if version.strip().lower().startswith("chirp-"):
        return version.strip()
    # aliases (allow "5.5", "5", "fenix", "4.5+", etc.)
    aliases = {
        "5.5": "chirp-fenix",
        "fenix": "chirp-fenix",
        "5": "chirp-crow",
        "crow": "chirp-crow",
        "4.5+": "chirp-bluejay",
        "bluejay": "chirp-bluejay",
        "4.5": "chirp-auk",
        "auk": "chirp-auk",
        "4.5-all": "chirp-auk-turbo",
        "auk-turbo": "chirp-auk-turbo",
        "4": "chirp-v4",
        "3.5": "chirp-v3-5",
        "3": "chirp-v3-0",
        "2": "chirp-v2-xxl-alpha",
    }
    if v in aliases:
        return aliases[v]
    # unknown: pass through (API may reject or accept)
    return version.strip()


def parse_song_md(filepath: str) -> dict:
    """Parse a song markdown file into API-ready fields."""
    content = Path(filepath).read_text(encoding="utf-8")

    # Extract title from H1
    title_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else Path(filepath).stem

    # Extract style prompt (first code block after ## Style Prompt)
    style_match = re.search(r"## Style Prompt\s*\n+```\n(.*?)\n```", content, re.DOTALL)
    tags = style_match.group(1).strip() if style_match else ""

    # Extract lyrics (code block after ## Lyrics)
    lyrics_match = re.search(r"## Lyrics\s*\n+```\n(.*?)\n```", content, re.DOTALL)
    lyrics = lyrics_match.group(1).strip() if lyrics_match else ""

    # Extract negative tags from Details table if present
    negative_tags = ""
    # Check style prompt for "no ..." patterns to also populate negative_tags
    no_patterns = re.findall(r"no\s+([^,\n]+)", tags, re.IGNORECASE)
    if no_patterns:
        negative_tags = ", ".join(p.strip() for p in no_patterns)

    # Extract BPM from Details table
    bpm_match = re.search(r"\*\*BPM\*\*\s*\|\s*(\d+)", content)
    bpm = int(bpm_match.group(1)) if bpm_match else None

    return {
        "title": title,
        "tags": tags,
        "negative_tags": negative_tags,
        "prompt": lyrics,  # Suno calls lyrics "prompt" in the API
        "bpm": bpm,
    }


def generate_browser_token() -> str:
    """Generate a browser token matching Suno's format."""
    timestamp = int(time.time() * 1000)
    token_data = json.dumps({"timestamp": timestamp})
    encoded = base64.b64encode(token_data.encode()).decode()
    return json.dumps({"token": encoded})


def download_clip(clip_id: str, song_slug: str, clip_num: int) -> Optional[str]:
    """Download an mp3 from the Suno CDN. Returns the local file path or None."""
    cdn_url = f"https://cdn1.suno.ai/{clip_id}.mp3"
    downloads_dir = Path(__file__).parent / "downloads"
    downloads_dir.mkdir(exist_ok=True)

    filename = f"{song_slug}-clip{clip_num}-{clip_id[:8]}.mp3"
    filepath = downloads_dir / filename

    print(f"  Downloading clip {clip_num}: {cdn_url}")
    try:
        resp = requests.get(cdn_url, timeout=120, stream=True)
        if resp.status_code == 200:
            with open(filepath, "wb") as f:
                for chunk in resp.iter_content(chunk_size=8192):
                    f.write(chunk)
            size_mb = filepath.stat().st_size / (1024 * 1024)
            print(f"    Saved: {filepath} ({size_mb:.1f} MB)")
            return str(filepath)
        else:
            print(f"    Download failed: HTTP {resp.status_code}")
            return None
    except Exception as e:
        print(f"    Download error: {e}")
        return None


def append_generation_links(
    filepath: str,
    generation_id: str,
    clips: list[dict],
    downloaded: Optional[Dict[str, str]] = None,
):
    """Append generation links to the song markdown file under ## Generations.

    Args:
        filepath: Path to the song markdown file.
        generation_id: The generation UUID.
        clips: List of clip dicts from the API response.
        downloaded: Optional mapping of clip_id -> local file path.
    """
    content = Path(filepath).read_text(encoding="utf-8")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    downloaded = downloaded or {}

    # Build the new entry
    lines = []
    lines.append(f"- **{timestamp}** (gen `{generation_id[:8]}`):")
    for i, clip in enumerate(clips):
        clip_id = clip.get("id", "unknown")
        url = f"https://suno.com/song/{clip_id}"
        local = downloaded.get(clip_id)
        if local:
            rel_path = os.path.relpath(local, Path(filepath).parent)
            lines.append(
                f"  - [Clip {i + 1}]({url}) | [{Path(local).name}]({rel_path})"
            )
        else:
            lines.append(f"  - [Clip {i + 1}]({url})")
    entry = "\n".join(lines)

    # Check if ## Generations section already exists
    gen_match = re.search(r"^## Generations\s*$", content, re.MULTILINE)
    if gen_match:
        # Append to existing section
        insert_pos = gen_match.end()
        content = content[:insert_pos] + "\n\n" + entry + content[insert_pos:]
    else:
        # Add new section at the end of the file
        content = content.rstrip() + "\n\n## Generations\n\n" + entry + "\n"

    Path(filepath).write_text(content, encoding="utf-8")
    print(f"\nUpdated {filepath} with generation links")
    for i, clip in enumerate(clips):
        clip_id = clip.get("id", "unknown")
        local = downloaded.get(clip_id)
        extra = f" -> {local}" if local else ""
        print(f"  Clip {i + 1}: https://suno.com/song/{clip_id}{extra}")


def submit_to_suno(song: dict, dry_run: bool = False, model_version: Optional[str] = None) -> dict:
    """Submit a song to the Suno API."""
    auth_token, is_auto = get_auth_token()
    device_id = os.environ.get("SUNO_DEVICE_ID", "")
    model = resolve_model_version(model_version) if model_version else os.environ.get("SUNO_MODEL", "chirp-crow")
    api_url = os.environ.get("SUNO_API_URL", "https://studio-api-prod.suno.com")

    if is_auto:
        print("Using auto-refreshed token from cookies")
    else:
        # Check token expiry for manual tokens
        token_info = check_token_expiry(auth_token)
        if token_info["expired"]:
            print("Cannot proceed with expired token.")
            print("\nTo refresh:")
            print("  Auto: scripts/set-suno-cookies 'your-cookies...'")
            print("  Manual: scripts/set-suno-token")
            sys.exit(1)

    import uuid

    # Build request body matching browser request
    body = {
        "token": None,
        "generation_type": "TEXT",
        "title": song["title"],
        "tags": song["tags"],
        "negative_tags": song["negative_tags"],
        "mv": model,
        "prompt": song["prompt"],
        "make_instrumental": False,
        "user_uploaded_images_b64": None,
        "metadata": {
            "web_client_pathname": "/create",
            "is_max_mode": False,
            "is_mumble": False,
            "create_mode": "custom",
            "disable_volume_normalization": False,
        },
        "override_fields": [],
        "cover_clip_id": None,
        "cover_start_s": None,
        "cover_end_s": None,
        "persona_id": None,
        "artist_clip_id": None,
        "artist_start_s": None,
        "artist_end_s": None,
        "continue_clip_id": None,
        "continued_aligned_prompt": None,
        "continue_at": None,
        "transaction_uuid": str(uuid.uuid4()),
    }

    # Generate browser-token with current timestamp
    import base64
    timestamp = int(time.time() * 1000)
    browser_token_payload = json.dumps({"timestamp": timestamp})
    browser_token = base64.urlsafe_b64encode(browser_token_payload.encode()).decode().rstrip("=")

    headers = {
        "Authorization": f"Bearer {auth_token}",
        "browser-token": json.dumps({"token": browser_token}),
        "Device-Id": device_id,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36",
        "Referer": "https://suno.com/",
        "Origin": "https://suno.com",
        "Accept": "*/*",
        "sec-ch-ua": '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
    }

    endpoint = f"{api_url}/api/generate/v2-web/"

    if dry_run:
        print("\n=== DRY RUN ===")
        print(f"POST {endpoint}")
        print(f"\nTitle: {body['title']}")
        print(f"Model: {body['mv']}")
        print(f"Tags: {body['tags'][:100]}...")
        print(f"Negative tags: {body['negative_tags']}")
        print(f"Lyrics length: {len(body['prompt'])} chars")
        print(f"\nFull body ({len(json.dumps(body))} bytes):")
        print(json.dumps(body, indent=2, ensure_ascii=False)[:2000])
        if len(json.dumps(body)) > 2000:
            print("... (truncated)")
        return {"dry_run": True}

    print(f"\nSubmitting '{song['title']}' to Suno API...")
    print(f"  Model: {model}")
    print(f"  Tags: {song['tags'][:80]}...")
    print(f"  Lyrics: {len(song['prompt'])} chars")

    response = requests.post(endpoint, json=body, headers=headers, timeout=60)

    if response.status_code == 200:
        data = response.json()
        print(f"\nGeneration submitted successfully!")
        print(f"  Generation ID: {data.get('id')}")
        clips = data.get("clips", [])
        for i, clip in enumerate(clips):
            print(f"  Clip {i + 1}: {clip.get('id')} (status: {clip.get('status')})")
        return data
    else:
        print(f"\nERROR: API returned {response.status_code}")
        print(f"Response: {response.text[:500]}")
        return {"error": response.status_code, "body": response.text}


def poll_status(generation_id: str, clip_ids: list[str], timeout: int = 600):
    """Poll for generation completion."""
    api_url = os.environ.get("SUNO_API_URL", "https://studio-api-prod.suno.com")
    device_id = os.environ.get("SUNO_DEVICE_ID", "")
    cookie = os.environ.get("SUNO_COOKIE", "")

    # Poll using the feed endpoint
    ids_param = ",".join(clip_ids)
    poll_url = f"{api_url}/api/feed/?ids={ids_param}"

    start = time.time()
    print(f"\nPolling for completion (timeout: {timeout}s)...")

    while time.time() - start < timeout:
        try:
            # Refresh token before each poll (cheap if using cookies)
            auth_token, _ = get_auth_token()
            headers = {
                "Authorization": f"Bearer {auth_token}",
                "Cookie": cookie,
                "Device-Id": device_id,
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:147.0) Gecko/20100101 Firefox/147.0",
                "Referer": "https://suno.com/",
                "Origin": "https://suno.com",
                "Accept": "*/*",
            }
            resp = requests.get(poll_url, headers=headers, timeout=30)
            if resp.status_code == 200:
                clips = resp.json()
                if isinstance(clips, list):
                    statuses = [c.get("status", "unknown") for c in clips]
                    print(f"  Status: {', '.join(statuses)}", end="\r")

                    if all(s == "complete" for s in statuses):
                        print(f"\n\nAll clips complete!")
                        for clip in clips:
                            print(
                                f"  {clip['id']}: {clip.get('audio_url', 'no url yet')}"
                            )
                        return clips
                    elif any(s == "error" for s in statuses):
                        print(f"\n\nGeneration failed!")
                        for clip in clips:
                            if clip.get("status") == "error":
                                print(
                                    f"  {clip['id']}: {clip.get('metadata', {}).get('error_message', 'unknown error')}"
                                )
                        return clips
            else:
                print(f"  Poll error: {resp.status_code}")
        except Exception as e:
            print(f"  Poll exception: {e}")

        time.sleep(10)

    print(f"\nTimeout after {timeout}s. Check Suno dashboard for results.")
    return None


def parse_generation_clip_ids(filepath: str, gen_index: int = 0) -> list[str]:
    """Extract clip IDs from the ## Generations section of a song markdown.

    Args:
        filepath: Path to the song markdown file.
        gen_index: Which generation to extract (0 = most recent, 1 = second most recent, etc.)

    Returns:
        List of clip UUIDs found in the specified generation entry.
    """
    content = Path(filepath).read_text(encoding="utf-8")

    # Find ## Generations section
    gen_section = re.search(r"## Generations\s*\n(.*)", content, re.DOTALL)
    if not gen_section:
        return []

    section_text = gen_section.group(1)

    # Each generation entry starts with "- **timestamp** (gen `id`):"
    # Collect all entries (split by top-level "- **")
    entries = re.split(r"(?=^- \*\*)", section_text.strip(), flags=re.MULTILINE)
    entries = [e.strip() for e in entries if e.strip()]

    if gen_index >= len(entries):
        return []

    entry = entries[gen_index]

    # Extract clip IDs from suno.com/song/{uuid} links
    clip_ids = re.findall(r"suno\.com/song/([0-9a-f-]{36})", entry)
    return clip_ids


def check_status(filepath: str, no_download: bool = False, timeout: int = 60):
    """Check the status of the most recent generation from a song file.

    Parses clip IDs from the ## Generations section, queries the feed endpoint,
    and optionally downloads completed clips that haven't been downloaded yet.
    """
    clip_ids = parse_generation_clip_ids(filepath)
    if not clip_ids:
        print("ERROR: No clip IDs found in ## Generations section")
        print("  Has this song been generated yet?")
        sys.exit(1)

    print(f"Checking status for {len(clip_ids)} clip(s):")
    for cid in clip_ids:
        print(f"  {cid}")

    auth_token, is_auto = get_auth_token()
    api_url = os.environ.get("SUNO_API_URL", "https://studio-api-prod.suno.com")
    device_id = os.environ.get("SUNO_DEVICE_ID", "")

    if is_auto:
        print("Using auto-refreshed token from cookies")
    else:
        token_info = check_token_expiry(auth_token)
        if token_info["expired"]:
            print("Cannot proceed with expired token.")
            print("\nTo refresh:")
            print("  Auto: scripts/set-suno-cookies 'your-cookies...'")
            print("  Manual: scripts/set-suno-token")
            sys.exit(1)

    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Device-Id": device_id,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:147.0) Gecko/20100101 Firefox/147.0",
        "Referer": "https://suno.com/",
        "Origin": "https://suno.com",
        "Accept": "*/*",
    }

    ids_param = ",".join(clip_ids)
    poll_url = f"{api_url}/api/feed/?ids={ids_param}"

    try:
        resp = requests.get(poll_url, headers=headers, timeout=timeout)
    except Exception as e:
        print(f"ERROR: Request failed: {e}")
        sys.exit(1)

    if resp.status_code != 200:
        print(f"ERROR: API returned {resp.status_code}")
        print(f"Response: {resp.text[:500]}")
        sys.exit(1)

    clips = resp.json()
    if not isinstance(clips, list):
        print(f"ERROR: Unexpected response format: {type(clips)}")
        sys.exit(1)

    print(f"\nStatus:")
    all_complete = True
    for clip in clips:
        status = clip.get("status", "unknown")
        clip_id = clip.get("id", "unknown")
        title = clip.get("title", "")
        duration = clip.get("metadata", {}).get("duration", "?")
        audio_url = clip.get("audio_url", "")

        status_icon = {
            "complete": "[OK]",
            "submitted": "[..]",
            "streaming": "[>>]",
            "error": "[!!]",
        }.get(status, "[??]")

        print(f"  {status_icon} {clip_id[:8]}... — {status}")
        if status == "complete":
            print(f"       Duration: {duration}s")
            if audio_url:
                print(f"       Audio: {audio_url[:80]}...")
        elif status == "error":
            err_msg = clip.get("metadata", {}).get("error_message", "unknown error")
            print(f"       Error: {err_msg}")
            all_complete = False
        else:
            all_complete = False

    # Download completed clips if not already downloaded
    if all_complete and not no_download:
        content = Path(filepath).read_text(encoding="utf-8")
        song_slug = Path(filepath).stem
        downloaded: dict[str, str] = {}
        needs_download = False

        for i, clip in enumerate(clips):
            clip_id = clip.get("id", "")
            # Check if already downloaded (has a .mp3 link in the markdown)
            if clip_id and f"{clip_id[:8]}.mp3" not in content:
                needs_download = True
                local_path = download_clip(clip_id, song_slug, i + 1)
                if local_path:
                    downloaded[clip_id] = local_path

        if downloaded:
            # Re-read content to update the clip lines with download paths
            content = Path(filepath).read_text(encoding="utf-8")
            for clip_id, local_path in downloaded.items():
                rel_path = os.path.relpath(local_path, Path(filepath).parent)
                # Find the line with this clip's suno link and append download link
                old_pattern = f"(https://suno.com/song/{clip_id})"
                new_pattern = f"(https://suno.com/song/{clip_id}) | [{Path(local_path).name}]({rel_path})"
                content = content.replace(old_pattern, new_pattern)
            Path(filepath).write_text(content, encoding="utf-8")
            print(f"\nUpdated {filepath} with download links")
        elif not needs_download:
            print(f"\nAll clips already downloaded.")
    elif not all_complete:
        print(f"\nNot all clips are complete yet. Run --status again later.")


def main():
    parser = argparse.ArgumentParser(
        description="Generate Suno tracks from song markdown files. Also supports --keep-alive for automatic token maintenance (inspired by SunoAI-API/Suno-API)."
    )
    parser.add_argument(
        "song_file",
        nargs="?",
        default=None,
        help="Path to song .md file (not needed for --keep-alive or --status on a prior gen)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be sent without calling API",
    )
    parser.add_argument(
        "--status",
        action="store_true",
        help="Check status of the most recent generation (no new submission)",
    )
    parser.add_argument(
        "--no-poll", action="store_true", help="Don't poll for completion"
    )
    parser.add_argument(
        "--no-download",
        action="store_true",
        help="Don't download mp3s after completion",
    )
    parser.add_argument(
        "--poll-timeout",
        type=int,
        default=600,
        help="Polling timeout in seconds (default: 600)",
    )
    parser.add_argument(
        "--keep-alive",
        action="store_true",
        help="Run automatic token maintenance and keep-alive loop (no song needed). Implements proactive Clerk JWT refresh like Suno-API.",
    )
    parser.add_argument(
        "--keep-interval",
        type=int,
        default=5,
        help="Refresh interval seconds for --keep-alive (default: 5, matching server-style keep-alive)",
    )
    parser.add_argument(
        "--version",
        "--model",
        dest="model_version",
        default=None,
        help="Suno model version (e.g. v5.5, v5, v4.5+, v4.5, chirp-fenix, crow). Overrides SUNO_MODEL. Default: v5 (chirp-crow)",
    )
    args = parser.parse_args()

    load_env()

    if args.keep_alive:
        keep_alive_loop(interval_seconds=args.keep_interval)
        return

    if not args.song_file:
        parser.error("song_file is required (unless using --keep-alive)")

    if not Path(args.song_file).exists():
        print(f"ERROR: File not found: {args.song_file}")
        sys.exit(1)

    # Status check mode -- query existing generation, don't submit new one
    if args.status:
        check_status(args.song_file, no_download=args.no_download)
        return

    print(f"Parsing: {args.song_file}")
    song = parse_song_md(args.song_file)
    print(f"  Title: {song['title']}")
    print(f"  BPM: {song['bpm']}")
    print(f"  Tags length: {len(song['tags'])} chars")
    print(f"  Lyrics length: {len(song['prompt'])} chars")

    result = submit_to_suno(song, dry_run=args.dry_run, model_version=args.model_version)

    if not args.dry_run and "id" in result:
        clips = result.get("clips", [])
        clip_ids = [c["id"] for c in clips]
        downloaded: dict[str, str] = {}

        # Poll for completion
        completed_clips = None
        if clip_ids and not args.no_poll:
            completed_clips = poll_status(
                result["id"], clip_ids, timeout=args.poll_timeout
            )

        # Download mp3s if polling succeeded
        if completed_clips and not args.no_download:
            song_slug = Path(args.song_file).stem
            print(f"\nDownloading completed clips...")
            for i, clip in enumerate(completed_clips):
                if clip.get("status") == "complete":
                    local_path = download_clip(clip["id"], song_slug, i + 1)
                    if local_path:
                        downloaded[clip["id"]] = local_path

        # Update markdown with links (and download paths if available)
        if clips:
            append_generation_links(args.song_file, result["id"], clips, downloaded)


if __name__ == "__main__":
    main()
