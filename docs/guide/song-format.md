# Song Format

Every song in this project is a markdown file stored in the `songs/` directory. Files use **kebab-case** naming derived from the song title (e.g., `beyond-the-silence-of-the-stars.md`).

## Required Structure

Each song file must contain these sections in order:

### 1. Title (H1)

The song's display name.

```markdown
# Beyond the Silence of the Stars
```

### 2. Details Table

A markdown table with key metadata:

```markdown
## Details

| Parameter | Value |
|-----------|-------|
| **Genre** | Euphoric Hardstyle |
| **BPM** | 150 |
| **Mood** | Epic, dramatic, triumphant |
| **Theme** | Cosmic / ethereal |
| **Vocals** | Powerful female vocals |
| **Duration** | ~4-5 min |
| **Key features** | Reverse bass kicks, euphoric synth leads |
```

**Required parameters:** Genre, BPM, Mood, Theme, Vocals, Duration, Key features

**Optional parameters:** Source (for lyrics origin), any additional context

### 3. Style Prompt

A code block containing the prompt passed to Suno's generation engine:

````markdown
## Style Prompt

```
Euphoric hardstyle, 150 BPM, epic, dramatic, powerful reverse bass kicks, soaring euphoric synth leads, orchestral strings, no rap, no acoustic guitar
```
````

See [Style Prompts](./style-prompts) for crafting guidelines.

### 4. Lyrics

A code block containing the full lyrics with meta-tags:

````markdown
## Lyrics

```
[Intro]
[Energy: Low]
[Instrumental, 8 bars]

[Verse 1]
[Vocal Style: Soft]
Beyond the silence of the stars
I heard a voice across the dark
...
```
````

See [Meta-Tags Reference](./meta-tags) for all available tags.

### 5. Generation Tips

Bullet points with practical advice for generating the track:

```markdown
## Generation Tips

- Generate 3-4 versions and pick the best
- Remaster (Subtle) after selecting your best version
- If too short, use Extend with callback
```

## Optional Sections

- **Source Material** -- Origin of lyrics (e.g., chat logs)
- **Lyrics Changes Log** -- Record of edits from the original
- **Generations** -- Links to generated Suno clips

## Line Length Guidelines

- Keep lyric lines to **6-12 syllables** for best vocal alignment
- Lines over 12 syllables cause vocal alignment issues
- Front-load important meta-tags in the first lines of lyrics
