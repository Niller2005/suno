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
