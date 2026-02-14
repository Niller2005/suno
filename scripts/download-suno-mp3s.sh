#!/bin/bash
# Download MP3s from Suno CDN based on song markdown files
#
# Usage:
#   ./scripts/download-suno-mp3s.sh [song-file.md ...]
#
# If no arguments given, scans all songs/*.md files for Suno clip URLs.
# Downloads MP3s to downloads/ and copies them to docs/public/audio/ for VitePress.
#
# URL pattern: https://suno.com/song/{id} -> https://cdn1.suno.ai/{id}.mp3

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DOWNLOADS_DIR="$REPO_ROOT/downloads"
PUBLIC_AUDIO_DIR="$REPO_ROOT/docs/public/audio"
SONGS_DIR="$REPO_ROOT/songs"
CDN_BASE="https://cdn1.suno.ai"

mkdir -p "$DOWNLOADS_DIR" "$PUBLIC_AUDIO_DIR"

# Collect song files to process
if [ $# -gt 0 ]; then
    FILES=("$@")
else
    FILES=("$SONGS_DIR"/*.md)
fi

downloaded=0
skipped=0
failed=0

for song_file in "${FILES[@]}"; do
    if [ ! -f "$song_file" ]; then
        echo "WARN: File not found: $song_file"
        continue
    fi

    song_name="$(basename "$song_file" .md)"
    echo "=== Processing: $song_name ==="

    # Extract Suno song IDs from markdown links like [Clip N](https://suno.com/song/{id})
    clip_ids=($(grep -oP 'suno\.com/song/\K[a-f0-9-]+' "$song_file" 2>/dev/null || true))

    if [ ${#clip_ids[@]} -eq 0 ]; then
        echo "  No Suno clip URLs found, skipping."
        continue
    fi

    clip_num=0
    for clip_id in "${clip_ids[@]}"; do
        clip_num=$((clip_num + 1))
        filename="${song_name}-clip${clip_num}.mp3"
        download_path="$DOWNLOADS_DIR/$filename"
        public_path="$PUBLIC_AUDIO_DIR/$filename"

        # Skip if already downloaded
        if [ -f "$download_path" ] && [ -s "$download_path" ]; then
            echo "  Clip $clip_num: Already exists ($filename), skipping download."
            skipped=$((skipped + 1))
        else
            echo "  Clip $clip_num: Downloading $clip_id ..."
            if curl -L -f -s -o "$download_path" \
                "$CDN_BASE/$clip_id.mp3" \
                -H "Referer: https://suno.com/" \
                -H "Origin: https://suno.com" \
                --max-time 120; then
                size=$(stat -c%s "$download_path" 2>/dev/null || stat -f%z "$download_path" 2>/dev/null || echo "?")
                echo "  Clip $clip_num: Downloaded ($size bytes)"
                downloaded=$((downloaded + 1))
            else
                echo "  Clip $clip_num: FAILED to download"
                rm -f "$download_path"
                failed=$((failed + 1))
                continue
            fi
        fi

        # Copy to VitePress public dir
        if [ -f "$download_path" ]; then
            cp "$download_path" "$public_path"
            echo "  Clip $clip_num: Copied to docs/public/audio/$filename"
        fi
    done
done

echo ""
echo "=== Summary ==="
echo "  Downloaded: $downloaded"
echo "  Skipped:    $skipped"
echo "  Failed:     $failed"
echo "  Audio dir:  $PUBLIC_AUDIO_DIR"
