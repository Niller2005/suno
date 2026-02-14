#!/usr/bin/env python3
"""
Suno API Generation Script

Reads song markdown files from docs/songs/ and submits them to the Suno API.
Auth token and config are read from .env file.

Usage:
    python generate.py docs/songs/my-song.md
    python generate.py docs/songs/my-song.md --dry-run
    python generate.py docs/songs/my-song.md --duration 240
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
            print("Refresh your token from browser DevTools and update .env")
            return {"expired": True, "payload": payload}
        elif remaining < 300:  # Less than 5 minutes
            print(f"WARNING: Token expires in {remaining:.0f} seconds!")
        else:
            print(f"Token valid for {remaining / 60:.0f} more minutes")
        return {"expired": False, "payload": payload}
    except Exception as e:
        print(f"Could not decode token: {e}")
        return {"expired": False, "payload": {}}


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


def download_clip(clip_id: str, song_slug: str, clip_num: int) -> str | None:
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
    downloaded: dict[str, str] | None = None,
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


def submit_to_suno(song: dict, dry_run: bool = False) -> dict:
    """Submit a song to the Suno API."""
    auth_token = os.environ.get("SUNO_AUTH_TOKEN", "")
    device_id = os.environ.get("SUNO_DEVICE_ID", "")
    model = os.environ.get("SUNO_MODEL", "chirp-crow")
    api_url = os.environ.get("SUNO_API_URL", "https://studio-api.prod.suno.com")

    if not auth_token:
        print("ERROR: SUNO_AUTH_TOKEN not set in .env")
        sys.exit(1)

    # Check token expiry
    token_info = check_token_expiry(auth_token)
    if token_info["expired"]:
        print("Cannot proceed with expired token.")
        sys.exit(1)

    # Build request body
    body = {
        "token": None,
        "generation_type": "TEXT",
        "title": song["title"],
        "tags": song["tags"],
        "negative_tags": song["negative_tags"],
        "mv": model,
        "prompt": song["prompt"],
    }

    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Device-Id": device_id,
        "Browser-Token": generate_browser_token(),
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:147.0) Gecko/20100101 Firefox/147.0",
        "Referer": "https://suno.com/",
        "Origin": "https://suno.com",
        "Accept": "*/*",
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
    auth_token = os.environ.get("SUNO_AUTH_TOKEN", "")
    api_url = os.environ.get("SUNO_API_URL", "https://studio-api.prod.suno.com")
    device_id = os.environ.get("SUNO_DEVICE_ID", "")

    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Device-Id": device_id,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:147.0) Gecko/20100101 Firefox/147.0",
        "Referer": "https://suno.com/",
        "Origin": "https://suno.com",
        "Accept": "*/*",
    }

    # Poll using the feed endpoint
    ids_param = ",".join(clip_ids)
    poll_url = f"{api_url}/api/feed/?ids={ids_param}"

    start = time.time()
    print(f"\nPolling for completion (timeout: {timeout}s)...")

    while time.time() - start < timeout:
        try:
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

    auth_token = os.environ.get("SUNO_AUTH_TOKEN", "")
    api_url = os.environ.get("SUNO_API_URL", "https://studio-api.prod.suno.com")
    device_id = os.environ.get("SUNO_DEVICE_ID", "")

    if not auth_token:
        print("ERROR: SUNO_AUTH_TOKEN not set in .env")
        sys.exit(1)

    token_info = check_token_expiry(auth_token)
    if token_info["expired"]:
        print("Cannot proceed with expired token.")
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
        description="Generate Suno tracks from song markdown files"
    )
    parser.add_argument("song_file", help="Path to song .md file")
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
    args = parser.parse_args()

    if not Path(args.song_file).exists():
        print(f"ERROR: File not found: {args.song_file}")
        sys.exit(1)

    load_env()

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

    result = submit_to_suno(song, dry_run=args.dry_run)

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
