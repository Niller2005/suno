# Generation Tips

Best practices for generating high-quality tracks with Suno AI.

## Generation Workflow

### 1. Generate Multiple Versions

Always generate **3-4 versions** per track. Suno's output varies significantly between runs -- the same prompt can produce wildly different results. Pick the version with:

- Cleanest vocals
- Best kick/bass balance
- Most accurate BPM
- Strongest structural adherence

### 2. Remaster the Best Version

After selecting your best generation, apply **Remaster (Subtle)** for polish. This cleans up minor artifacts without changing the character of the track.

### 3. Extend if Needed

If a track is too short, use **Extend** with a callback phrase:

> "continue with same [genre] vibe and [theme]"

Examples:
- "continue with same euphoric hardstyle vibe and cosmic theme"
- "continue with same liquid drum and bass energy"
- "continue with same speed garage bass and shuffled beat energy"

::: warning
Don't chain too many Extends without callbacks -- this causes **style drift** where the track gradually loses coherence.
:::

### 4. Cover for Voice Changes

If the vocals aren't right, use **Cover** to:
- Change vocal persona (male/female, pitched up/down)
- Add specific vocal effects (vocoder, auto-tune)
- Adjust vocal delivery style

### 5. Replace Section (Studio/Premier)

For surgical fixes, **Replace Section** lets you regenerate specific parts of a track without affecting the rest. Useful for:
- Fixing a weak chorus drop
- Improving a bridge section
- Cleaning up an intro/outro

## Quality Checklist

Before finalizing a track, verify:

- [ ] BPM matches target (plus/minus 5 BPM acceptable)
- [ ] Vocals are clear and expressive
- [ ] No audio artifacts (clicks, pops, distortion)
- [ ] Structure is complete (intro, verses, chorus, outro)
- [ ] Energy levels are appropriate
- [ ] Lyrics are audible and correct
- [ ] Musical motifs are consistent throughout

## Genre-Specific Tips

### Electronic (DnB, Hardstyle, House)

- BPM is non-negotiable -- regenerate if it drifts
- Kick/bass relationship is everything
- Drops should hit hard; if they don't, regenerate
- Use negative prompts aggressively: "no acoustic guitar", "no piano ballad"

### Psytrance

- The acid bass should mutate and evolve throughout
- Middle Eastern melodic hints are the signature flavor
- 8-bar instrumental breaks let the bass go unhinged
- Buildups should be massive walls of sound

### Speed Garage / UK Underground

- The shuffle/2-step feel is essential -- if it sounds 4x4, regenerate
- Organ stabs and time-stretched vocal chops are key
- Deep rolling sub bass is the foundation

### Kawaii Hyperpop

- Pitched-up vocals are essential -- use Cover if too normal
- Chaotic energy shifts define the genre
- Sparkly synths + heavy reese bass = the right contrast

## Common Issues

| Issue | Solution |
|-------|----------|
| Vocals too quiet | Regenerate or try Cover with different persona |
| Wrong BPM | Regenerate -- Suno usually nails BPM but can drift |
| Weak drops | Regenerate or Replace Section on the drop |
| Missing effects | Add specific effects to style prompt and regenerate |
| Too short | Extend with callback |
| Style drift | Regenerate from scratch rather than chaining Extends |
| Lyrics cut off | Shorten lyrics or split into separate generation |
