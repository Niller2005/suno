# Getting Started

Welcome to the Suno Music Lab guide. This project is a workspace for creating AI-generated music with [Suno AI](https://suno.com).

## How It Works

1. **Write a song definition** as a markdown file in the `songs/` directory
2. **Craft a style prompt** describing genre, BPM, mood, and instrumentation
3. **Write lyrics** with Suno meta-tags for structure, energy, and vocal control
4. **Generate** the track using Suno AI (via the web UI or MCP tools)
5. **Iterate** -- generate multiple versions, pick the best, remaster and polish

## Project Structure

```
suno/
├── songs/           # Song definition markdown files
├── downloads/       # Generated audio files
├── generate.py      # Python script for batch generation
├── docs/            # This documentation site
└── suno-mcp/        # MCP server for IDE integration
```

## Quick Start

### Writing Your First Song

Create a new markdown file in `songs/` following the [Song Format](./song-format) specification:

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
- **MCP Tools**: Use the integrated MCP server for automated generation from your IDE

## Next Steps

- [Song Format](./song-format) -- Full specification for song markdown files
- [Style Prompts](./style-prompts) -- How to craft effective style prompts
- [Meta-Tags Reference](./meta-tags) -- Complete list of Suno meta-tags
- [Generation Tips](./generation-tips) -- Best practices for generating quality tracks
