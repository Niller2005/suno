# Getting Started

Welcome to the Suno Music Lab guide. This project is a workspace for creating AI-generated music with [Suno AI](https://suno.com).

## How It Works

1. **Write a song definition** as a markdown file in the `docs/songs/` directory
2. **Craft a style prompt** describing genre, BPM, mood, and instrumentation
3. **Write lyrics** with Suno meta-tags for structure, energy, and vocal control
4. **Generate** the track using Suno AI (via the web UI)
5. **Iterate** -- generate multiple versions, pick the best, remaster and polish

## Project Structure

```
suno/
├── docs/
│   ├── songs/       # Song definition markdown files (also VitePress pages)
│   ├── public/audio/ # MP3 files for audio players
│   └── guide/       # Documentation pages
├── downloads/       # Generated audio files (local copies)
├── generate.py      # Python script for batch generation
└── scripts/         # Utility scripts (download, etc.)
```

## Quick Start

### Writing Your First Song

Create a new markdown file in `docs/songs/` following the [Song Format](./song-format) specification:

```markdown
# My Song Title

## Details

| Parameter | Value |
|-----------|-------|
| **Genre** | Your genre |
| **BPM** | 120 |
| **Mood** | Your mood descriptors |
| **Theme** | What the song is about |
| **Vocals** | Vocal type and style |
| **Duration** | ~4-5 min |
| **Key features** | Notable production elements |

## Style Prompt

` `` (use triple backticks)
Your genre, 120 BPM, mood, instruments, vocal type, production style, no exclusions
` ``

## Lyrics

` `` (use triple backticks)
[Intro]
[Energy: Low]
Your lyrics here...
` ``

## Generation Tips

- Your tips for getting the best result
```

### Generating Tracks

You can generate tracks in two ways:

- **Suno Web UI**: Copy the style prompt and lyrics into [suno.com/create](https://suno.com/create)

## Next Steps

- [Song Format](./song-format) -- Full specification for song markdown files
- [Style Prompts](./style-prompts) -- How to craft effective style prompts
- [Meta-Tags Reference](./meta-tags) -- Complete list of Suno meta-tags
- [Generation Tips](./generation-tips) -- Best practices for generating quality tracks
