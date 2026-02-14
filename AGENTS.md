# AGENTS.md - Suno Music Creation

## Project Overview

This repository is a workspace for creating songs with Suno AI. Songs are stored as markdown files in `docs/songs/` using kebab-case filenames (e.g., `beyond-the-silence-of-the-stars.md`). These files serve double duty: they're the source of truth for song definitions and also the pages for the VitePress documentation site. Use the `suno-music-creator` skill for professional workflows.

## Song Markdown Format

Every song file must follow this structure:

```markdown
# Song Title

## Details

| Parameter | Value |
|-----------|-------|
| **Genre** | Genre name |
| **BPM** | Number |
| **Mood** | Comma-separated mood descriptors |
| **Theme** | Theme description |
| **Vocals** | Vocal type and style |
| **Duration** | Target duration |
| **Key features** | Distinctive production elements |

## Style Prompt

\```
Genre, BPM, mood, key instruments, vocal type, production style, negative prompts
\```

## Lyrics

\```
[Section tags with meta-tags]
Lyric lines (6-12 syllables per line)
\```

## Generation Tips

- Bullet points with practical Suno generation advice
```

## Style Prompt Formula

```
[Genre], [BPM] BPM, [Mood], [Key instruments], [Vocal type], [Production style], no [exclusions]
```

Rules:
- Keep prompts focused: 1-2 genres + 1 mood + key instruments
- Use era references ("80s synths", "90s boom bap") for flavor
- Use negative prompting to exclude unwanted elements: "no guitars", "no orchestral"
- Specify exact BPM for tempo-critical tracks
- Never name specific artists (copyright risk)

## Lyrics Meta-Tags

### Structure Tags

`[Intro]`, `[Verse 1]`, `[Pre-Chorus]`, `[Chorus]`, `[Post-Chorus]`, `[Bridge]`, `[Break]`, `[Hook]`, `[Interlude]`, `[Outro]`, `[End]`, `[Fade Out]`

### Instrumental Tags

`[Instrumental]`, `[Guitar Solo]`, `[Piano Solo]`, `[Synth Solo]`, `[Drum Break]`, `[Drop]`, `[Build]`

### Energy & Mood

```
[Energy: Low], [Energy: Medium], [Energy: Rising], [Energy: High], [Energy: Maximum]
[Mood: Dark], [Mood: Uplifting], [Mood: Melancholic], [Mood: Aggressive], [Mood: Triumphant]
```

### Vocal Controls

```
[Vocal Style: Whisper], [Vocal Style: Soft], [Vocal Style: Power], [Vocal Style: Raspy]
[Vocal Style: Falsetto], [Vocal Style: Belt], [Vocal Style: Spoken Word], [Vocal Style: Rap]
[Vocal Effect: Reverb], [Vocal Effect: Delay], [Vocal Effect: Auto-tune]
[Vocal Effect: Vocoder], [Vocal Effect: Distortion]
```

### Instrumentation

```
[Instrument: Piano], [Instrument: Acoustic Guitar], [Instrument: Synth Pads]
[Instrument: 808 Bass], [Instrument: Strings (Legato)], [Instrument: Brass]
[Instrumental, N bars]
```

### Timing

```
[Slow], [Fast], [Half-time], [Double-time], [Breakdown], [Buildup, 8 bars]
```

### Performance Indicators

| Format | Effect |
|--------|--------|
| `UPPERCASE TEXT` | Shouted/emphasized |
| `(text in parentheses)` | Backing vocals/harmonies |
| `~word~` | Elongated note |
| `word-` | Cut off abruptly |
| Repeated lines | Sung in loop |

## Lyrics Guidelines

- Keep lines to 6-12 syllables for best vocal alignment
- Lines over 12 syllables cause vocal alignment issues
- Front-load important meta-tags in the first lines of lyrics
- Don't stack too many consecutive tags (confuses AI)
- Match mood tags to lyrical content
- Repeat chorus structure identically for cohesion

## Generation Best Practices

- Generate 3-4 versions per track, pick the best output
- Use `Remaster (Subtle)` after selecting best version for polish
- Use `Extend` with callbacks ("continue with same vibe") if track is too short
- Use `Cover` to change style or voice on a selected generation
- Use `Replace Section` in Studio (Premier) to regenerate specific parts
- Specify exact BPM in style prompt for tempo-critical tracks
- Use negative prompting: "no guitars", "no orchestral", etc.
- Never chain too many Extends without callbacks (causes drift)

## Song Creation Checklist

- [ ] BPM matches target (plus/minus 5 BPM acceptable)
- [ ] Vocals clear and expressive
- [ ] No audio artifacts
- [ ] Structure complete (intro, verses, chorus, outro)
- [ ] Energy level appropriate for purpose
- [ ] Lyrics audible and correct
- [ ] Musical motifs consistent throughout

## File Conventions

- **Location**: `docs/songs/`
- **Filenames**: kebab-case, derived from song title (e.g., `dubi-dubi-doo.md`)
- **Format**: Markdown with VitePress frontmatter, Details table, Style Prompt code block, Lyrics code block, Generation Tips list
- **Downloads**: Track audio files go in `downloads/` and `docs/public/audio/` (for VitePress)

## Generating Songs with generate.py

The `generate.py` script reads song markdown files and submits them to the Suno API. It handles parsing, API submission, polling, downloading, and updating the markdown with generation links.

### Prerequisites

- Python 3.10+
- `requests` library (`pip install requests`)
- `python-dotenv` optional (`pip install python-dotenv`)
- A `.env` file in the project root with:

```
SUNO_AUTH_TOKEN=<JWT from browser DevTools>
SUNO_DEVICE_ID=<device ID from browser DevTools>
SUNO_MODEL=chirp-crow
SUNO_API_URL=https://studio-api.prod.suno.com
```

To get the token: open Suno in browser, DevTools > Network > any API request > copy `Authorization: Bearer <token>`. Tokens expire -- the script warns when <5 minutes remain and errors on expired tokens.

### Commands

```bash
# Dry run -- show what would be sent without calling the API
python generate.py docs/songs/my-song.md --dry-run

# Generate -- submit to Suno, poll for completion, download mp3s
python generate.py docs/songs/my-song.md

# Generate without polling (fire and forget)
python generate.py docs/songs/my-song.md --no-poll

# Generate without downloading mp3s
python generate.py docs/songs/my-song.md --no-download

# Custom poll timeout (default 600s)
python generate.py docs/songs/my-song.md --poll-timeout 300
```

### What It Does

1. **Parses** the song markdown: extracts title, style prompt (tags), negative tags (from "no ..." patterns), lyrics, and BPM
2. **Validates** the auth token (JWT expiry check)
3. **Submits** to `POST /api/generate/v2-web/` with generation_type `TEXT`
4. **Polls** the feed endpoint every 10s until all clips are `complete` or `error` (default 600s timeout)
5. **Downloads** completed mp3s to `downloads/` as `{song-slug}-clip{N}-{id[:8]}.mp3`
6. **Updates** the song markdown with a `## Generations` section containing timestamped links to Suno and local files

### Generation Workflow

When asked to generate a song:

1. **Always dry-run first** -- run with `--dry-run` and review the output
2. Confirm the title, tags, lyrics length, and negative tags look correct
3. Run without `--dry-run` to submit to Suno
4. The script automatically polls, downloads, and updates the markdown
5. Review the `## Generations` section appended to the song file
6. Listen to the downloaded clips and pick the best one

### Post-Generation: VitePress Integration

After a successful generation, complete these steps to make the song playable on the site:

1. **Copy MP3s to public audio directory**:
   - Copy from `downloads/{song}-clip{N}-{id}.mp3` to `docs/public/audio/{song}-{genid}-clip{N}.mp3` (include generation ID for traceability)
   - The `{genid}` is the first 8 characters of the generation ID (visible in the `## Generations` section)
   - Example: `cp downloads/my-song-clip1-a1b2c3d4.mp3 docs/public/audio/my-song-772c971f-clip1.mp3`

2. **Add audio player section to the song markdown** (after the Details table, before Style Prompt):
   - Use `vitepress-plugin-tabs` (`:::tabs` / `== Tab Name` syntax) to organize versions
   - Each version gets its own tab: `== V1 — Genre Description`
   - When regenerating a song with a new style, add a new tab rather than overwriting the previous one
   - The first generation is always the first tab; subsequent regenerations are added as new tabs
   ```markdown
   <script setup>
   import { withBase } from 'vitepress'
   </script>

   ## Listen

   :::tabs
   == V1 — Genre Description

   ### Clip 1

   <audio controls preload="metadata" style="width: 100%; margin-bottom: 1rem;">
     <source :src="withBase('/audio/{song}-{genid}-clip1.mp3')" type="audio/mpeg">
     Your browser does not support the audio element.
   </audio>

   [View on Suno](https://suno.com/song/{clip-id})
   :::
   ```
   Repeat the `### Clip N` block for each clip within a tab. Add new `== VN — Genre` tabs for regenerations.

3. **Add to song catalog index** (`docs/songs/index.md`):
   - Insert a row in the table in alphabetical order
   - Format: `| [Song Title](./song-slug) | Genre | BPM | Mood |`

4. **Add to sidebar** (`docs/.vitepress/config.mts`):
   - Insert entry in the `/songs/` sidebar items array in alphabetical order
   - Format: `{ text: "Song Title", link: "/songs/song-slug" }`

### Output Structure

After generation, the song file gets a `## Generations` section:

```markdown
## Generations

- **2026-02-14 15:30** (gen `a1b2c3d4`):
  - [Clip 1](https://suno.com/song/clip-id-1) | [my-song-clip1-a1b2c3d4.mp3](../../downloads/my-song-clip1-a1b2c3d4.mp3)
  - [Clip 2](https://suno.com/song/clip-id-2) | [my-song-clip2-a1b2c3d4.mp3](../../downloads/my-song-clip2-a1b2c3d4.mp3)
```

Downloaded mp3s are saved to `downloads/` at the project root.
