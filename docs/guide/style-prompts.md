# Style Prompts

The style prompt tells Suno's AI engine what kind of music to generate. It's passed as a text description alongside lyrics.

## Formula

```
[Genre], [BPM] BPM, [Mood], [Key instruments], [Vocal type], [Production style], no [exclusions]
```

## Rules

| Rule | Details |
|------|---------|
| Keep it focused | 1-2 genres + 1 mood + key instruments |
| Use era references | "80s synths", "90s boom bap" for flavor |
| Negative prompting | Exclude unwanted elements: "no guitars", "no orchestral" |
| Specify BPM | Exact BPM for tempo-critical tracks |
| No artist names | Never name specific artists (copyright risk) |

## Examples

### Euphoric Hardstyle

```
Euphoric hardstyle, 150 BPM, epic, dramatic, powerful reverse bass kicks, soaring euphoric synth leads, orchestral strings, massive buildups, anthemic drops, powerful female vocals, festival production, no rap, no acoustic guitar
```

### Liquid Drum and Bass

```
Liquid drum and bass, 174 BPM, smooth, rolling bassline, atmospheric pads, lush strings, ethereal female vocals, soulful, dreamy, uplifting, warm sub bass, crisp breakbeats, no distortion, no harsh sounds
```

### Speed Garage

```
Speed garage, 136 BPM, high energy, shuffled 2-step beat, deep rolling sub bass, organ stabs, chopped pitched vocal samples, time-stretched vocal chops, garage percussion, UK underground, cheeky, raw, male rap verses with female vocal hooks, no guitar, no piano ballad
```

### Psytrance / Electro House

```
Psytrance electro house, 142 BPM, aggressive, complex layered synthesizers, squelchy acid bassline, psychedelic arpeggios, hard-hitting 4/4 kick, glitch effects, tempo changes, massive buildups, processed male vocals, vocoder, spoken word sections, Middle Eastern melodic hints, dark psychedelic atmosphere, festival production, no acoustic guitar, no piano
```

### Stutter House

```
Stutter house, 126 BPM, groovy, four-on-the-floor, chopped vocal samples, glitchy stuttered effects, deep bassline, minimal synths, hypnotic, atmospheric pads, sexy female vocals, polished club production, no guitars, no orchestral
```

### Kawaii Hyperpop DnB

```
Kawaii hyperpop drum and bass, 174 BPM, chaotic, cute, pitched-up vocal chops, sparkly bright synths, heavy reese bass, rolling breakbeats, glitch effects, auto-tuned female vocals, anime-style ad-libs, euphoric drops, bitcrushed textures, no acoustic guitar, no piano ballad, no slow tempo
```

## Tips

- **Genre blending**: Combining 2 genres works well ("psytrance electro house"), but avoid mixing more than 2
- **Mood consistency**: Match your mood keywords to the lyrical content and meta-tags
- **Instrumentation specificity**: "deep rolling sub bass" is better than just "bass"
- **Negative prompts**: Always exclude elements that would clash with your genre (e.g., "no acoustic guitar" for electronic)
- **BPM matters**: Suno respects BPM closely, so specify it for tempo-critical genres like DnB (174), hardstyle (150), or house (126)
