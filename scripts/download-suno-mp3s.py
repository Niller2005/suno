#!/usr/bin/env python3
"""
Download MP3s from Suno CDN based on song markdown files.

Scans song markdown files for Suno clip URLs (https://suno.com/song/{id}),
downloads MP3s from the CDN, and copies them to the VitePress public
directory for embedding as audio players.

Usage:
    python scripts/download-suno-mp3s.py                              # all songs
    python scripts/download-suno-mp3s.py docs/songs/my-song.md        # specific song
    python scripts/download-suno-mp3s.py --no-copy docs/songs/*.md    # skip VitePress copy
"""

import argparse
import re
import shutil
import sys
from pathlib import Path

try:
    import requests
except ImportError:
    print("Missing 'requests' library. Install with: pip install requests")
    sys.exit(1)

REPO_ROOT = Path(__file__).resolve().parent.parent
DOWNLOADS_DIR = REPO_ROOT / "downloads"
PUBLIC_AUDIO_DIR = REPO_ROOT / "docs" / "public" / "audio"
SONGS_DIR = REPO_ROOT / "docs" / "songs"
CDN_BASE = "https://cdn1.suno.ai"


def extract_clip_ids(filepath: Path) -> list[str]:
    """Extract unique Suno clip IDs from markdown links like [Clip N](https://suno.com/song/{id})."""
    content = filepath.read_text(encoding="utf-8")
    seen = set()
    ids = []
    for clip_id in re.findall(r"suno\.com/song/([a-f0-9-]+)", content):
        if clip_id not in seen:
            seen.add(clip_id)
            ids.append(clip_id)
    return ids


def download_clip(clip_id: str, dest: Path) -> bool:
    """Download an MP3 from the Suno CDN. Returns True on success."""
    url = f"{CDN_BASE}/{clip_id}.mp3"
    try:
        resp = requests.get(
            url,
            headers={
                "Referer": "https://suno.com/",
                "Origin": "https://suno.com",
            },
            timeout=120,
            stream=True,
        )
        if resp.status_code == 200:
            with open(dest, "wb") as f:
                for chunk in resp.iter_content(chunk_size=8192):
                    f.write(chunk)
            return True
        else:
            print(f"    Download failed: HTTP {resp.status_code}")
            return False
    except Exception as e:
        print(f"    Download error: {e}")
        return False


def process_song(filepath: Path, copy_to_public: bool = True) -> dict:
    """Process a single song file. Returns stats dict."""
    stats = {"downloaded": 0, "skipped": 0, "failed": 0}
    song_name = filepath.stem
    clip_ids = extract_clip_ids(filepath)

    if not clip_ids:
        print(f"  No Suno clip URLs found, skipping.")
        return stats

    for i, clip_id in enumerate(clip_ids, 1):
        filename = f"{song_name}-clip{i}.mp3"
        download_path = DOWNLOADS_DIR / filename

        if download_path.exists() and download_path.stat().st_size > 0:
            print(f"  Clip {i}: Already exists ({filename}), skipping download.")
            stats["skipped"] += 1
        else:
            print(f"  Clip {i}: Downloading {clip_id} ...")
            if download_clip(clip_id, download_path):
                size_mb = download_path.stat().st_size / (1024 * 1024)
                print(f"  Clip {i}: Downloaded ({size_mb:.1f} MB)")
                stats["downloaded"] += 1
            else:
                print(f"  Clip {i}: FAILED to download")
                download_path.unlink(missing_ok=True)
                stats["failed"] += 1
                continue

        if copy_to_public and download_path.exists():
            public_path = PUBLIC_AUDIO_DIR / filename
            shutil.copy2(download_path, public_path)
            print(f"  Clip {i}: Copied to docs/public/audio/{filename}")

    return stats


def main():
    parser = argparse.ArgumentParser(
        description="Download Suno MP3s from song markdown files"
    )
    parser.add_argument(
        "song_files",
        nargs="*",
        help="Song .md files to process (default: all songs/*.md)",
    )
    parser.add_argument(
        "--no-copy",
        action="store_true",
        help="Don't copy to VitePress public directory",
    )
    args = parser.parse_args()

    DOWNLOADS_DIR.mkdir(exist_ok=True)
    if not args.no_copy:
        PUBLIC_AUDIO_DIR.mkdir(parents=True, exist_ok=True)

    if args.song_files:
        files = [Path(f) for f in args.song_files]
    else:
        files = sorted(SONGS_DIR.glob("*.md"))

    totals = {"downloaded": 0, "skipped": 0, "failed": 0}

    for song_file in files:
        if not song_file.exists():
            print(f"WARN: File not found: {song_file}")
            continue
        print(f"=== Processing: {song_file.stem} ===")
        stats = process_song(song_file, copy_to_public=not args.no_copy)
        for key in totals:
            totals[key] += stats[key]

    print()
    print("=== Summary ===")
    print(f"  Downloaded: {totals['downloaded']}")
    print(f"  Skipped:    {totals['skipped']}")
    print(f"  Failed:     {totals['failed']}")
    if not args.no_copy:
        print(f"  Audio dir:  {PUBLIC_AUDIO_DIR}")


if __name__ == "__main__":
    main()
