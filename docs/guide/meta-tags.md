# Meta-Tags Reference

Suno uses meta-tags in lyrics to control song structure, energy, vocals, and instrumentation. Tags are placed in square brackets within the lyrics code block.

## Structure Tags

Control the song's arrangement:

| Tag | Purpose |
|-----|---------|
| `[Intro]` | Opening section |
| `[Verse 1]`, `[Verse 2]`, etc. | Verse sections |
| `[Pre-Chorus]` | Build section before chorus |
| `[Chorus]` | Main hook/chorus |
| `[Post-Chorus]` | Section after chorus |
| `[Bridge]` | Contrasting section |
| `[Break]` | Stripped-down section |
| `[Hook]` | Catchy repeated section |
| `[Interlude]` | Connecting passage |
| `[Outro]` | Closing section |
| `[End]` | Hard stop |
| `[Fade Out]` | Gradual fade |

## Instrumental Tags

Control instrumental sections and solos:

| Tag | Purpose |
|-----|---------|
| `[Instrumental]` | Instrumental section |
| `[Instrumental, N bars]` | Instrumental for specific length |
| `[Guitar Solo]` | Guitar solo section |
| `[Piano Solo]` | Piano solo section |
| `[Synth Solo]` | Synthesizer solo |
| `[Drum Break]` | Drums-only section |
| `[Drop]` | EDM-style drop |
| `[Build]` | Building section |
| `[Buildup, N bars]` | Buildup for specific length |

## Energy Tags

Control intensity levels:

| Tag | Effect |
|-----|--------|
| `[Energy: Low]` | Quiet, intimate |
| `[Energy: Medium]` | Moderate intensity |
| `[Energy: Rising]` | Building momentum |
| `[Energy: High]` | Full intensity |
| `[Energy: Maximum]` | Peak intensity |

## Mood Tags

Set the emotional tone:

| Tag | Effect |
|-----|--------|
| `[Mood: Dark]` | Dark, moody atmosphere |
| `[Mood: Uplifting]` | Positive, bright |
| `[Mood: Melancholic]` | Sad, reflective |
| `[Mood: Aggressive]` | Intense, hard-hitting |
| `[Mood: Triumphant]` | Epic, victorious |
| `[Mood: Peaceful]` | Calm, serene |

## Vocal Style Tags

Control how vocals are delivered:

| Tag | Effect |
|-----|--------|
| `[Vocal Style: Whisper]` | Whispered delivery |
| `[Vocal Style: Soft]` | Gentle, quiet singing |
| `[Vocal Style: Power]` | Powerful singing |
| `[Vocal Style: Raspy]` | Rough, textured voice |
| `[Vocal Style: Falsetto]` | High register |
| `[Vocal Style: Belt]` | Full-power belting |
| `[Vocal Style: Spoken Word]` | Speaking, not singing |
| `[Vocal Style: Rap]` | Rap delivery |

## Vocal Effect Tags

Apply processing to vocals:

| Tag | Effect |
|-----|--------|
| `[Vocal Effect: Reverb]` | Spacious reverb |
| `[Vocal Effect: Delay]` | Echo/delay effect |
| `[Vocal Effect: Auto-tune]` | Pitch correction effect |
| `[Vocal Effect: Vocoder]` | Robotic vocoder |
| `[Vocal Effect: Distortion]` | Distorted vocals |

## Instrumentation Tags

Specify instruments:

```
[Instrument: Piano]
[Instrument: Acoustic Guitar]
[Instrument: Synth Pads]
[Instrument: 808 Bass]
[Instrument: Strings (Legato)]
[Instrument: Brass]
```

You can also specify multiple instruments:

```
[Instrument: Deep sub bass, shuffled garage beat, time-stretched vocal chop]
```

## Timing Tags

Control tempo and feel:

| Tag | Effect |
|-----|--------|
| `[Slow]` | Reduce tempo |
| `[Fast]` | Increase tempo |
| `[Half-time]` | Half-time feel |
| `[Double-time]` | Double-time feel |
| `[Breakdown]` | Stripped-down section |
| `[Buildup, N bars]` | Build over N bars |

## Performance Indicators

In-line formatting within lyrics (not tags):

| Format | Effect |
|--------|--------|
| `UPPERCASE TEXT` | Shouted/emphasized |
| `(text in parentheses)` | Backing vocals/harmonies |
| `~word~` | Elongated note |
| `word-` | Cut off abruptly |
| Repeated lines | Sung in loop |

## Best Practices

- **Don't stack too many tags** -- 2-3 consecutive tags is fine, but 5+ confuses the AI
- **Front-load important tags** -- Put structural and energy tags before vocal tags
- **Match mood to content** -- `[Mood: Dark]` with uplifting lyrics creates confusion
- **Use instrumental bars** -- `[Instrumental, 8 bars]` gives the AI breathing room
- **Repeat chorus structure** -- Keep chorus tags identical across repetitions for cohesion
