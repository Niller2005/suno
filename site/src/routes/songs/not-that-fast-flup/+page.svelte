<script lang="ts">
	import SongTabs from '$lib/components/SongTabs.svelte';
</script>

<SongTabs
	title="Not That Fast Flup"
	defaultGenre="Euphoric Hardstyle (Brennan Heart style)"
	defaultBpm={150}
	defaultMood="Euphoric, playful, energetic, determined, cheeky"
	defaultTheme="An intentionally slow chatbot teaching patience through hardstyle euphoria"
	defaultVocals="Male tenor, clear, confident, cheeky delivery, belted chorus vocals"
	defaultDuration="~4-5 min"
	defaultKeyFeatures="Euphoric piano leads, hard reverse bass kicks, massive drops, pitched vocal samples, rolling kickrolls, techno-style triplet builds, playful vocal chops"
	generationTips={[
		'Generate 3-4 versions and pick the one with the cleanest hardstyle kicks and clearest piano leads',
		'The spoken word "Not that fast" intros are critical -- they need to land as spoken, not sung',
		'The "NOT THAT FAST!" chant needs to feel like an anthemic festival crowd moment',
		'V5 handles hardstyle piano leads beautifully -- if the melody is muddy, regenerate',
		'If the kicks are too weak or not hardstyle enough, regenerate with "hardstyle kick" emphasis',
		'The triplet buildup before the second drop is key for Brennan Heart energy -- verify it\'s there',
		'Remaster (Subtle) after selecting best version for polish',
		'If too short, use Extend with callback: "continue with same euphoric hardstyle vibe and flup chatbot theme"',
		'The final "Not... that... fast~" should trail off with reverb -- if it cuts too abruptly, use Crop'
	]}
	generations={[
		{
			date: '2026-06-09 14:21',
			genId: '29dc717a',
			clips: [
				{ suno: 'https://suno.com/song/f9cef51f-d2be-4f52-8531-3d753efc8669', file: 'not-that-fast-flup-clip1-f9cef51f.mp3' },
				{ suno: 'https://suno.com/song/43a86dc7-a4ec-4a23-85e1-b985e3971c85', file: 'not-that-fast-flup-clip2-43a86dc7.mp3' }
			]
		}
	]}
	versions={[
		{
			label: 'V1 — Euphoric Hardstyle',
			stylePrompt: 'Euphoric hardstyle, 150 BPM, energetic, euphoric piano leads, hard reverse bass kicks, rolling kickrolls, anthemic drops, festival production, confident male vocals, pitched vocal chops, melodic breakdowns, triplet buildups, no rap, no acoustic guitar, no guitars, no rock',
			lyrics: `[Intro]
[Mood: Euphoric]
[Energy: Medium]
[Instrument: Euphoric piano melody, ambient pads, distant kick]
[Instrumental, 8 bars]

[Build]
[Energy: Rising]
[Instrument: Kickrolls, rising synth sweep, piano run]

[Break]
[Energy: Low]
[Instrument: Soft piano, single kick per bar]
[Vocal Style: Spoken Word]
~No~t that fast...

[Chorus]
[Energy: Maximum]
[Drop]
NOT THAT FAST!
Flup says NOT THAT FAST!
You're moving way too fast
Take a breath and make it last
NOT THAT FAST!
Flup says NOT THAT FAST!
The wisdom's in the wait
So accept your fate... NOT THAT FAST!

[Verse 1]
[Energy: Medium]
[Vocal Style: Power]
[Instrument: Driving reverse bass kick, melodic synth]
I asked the chatbot what's the score
It said slow down and ask once more
I typed my question clear and quick
Flup replied "you're making me sick-"
"with all that speed, where's the need?
Let me plant a mindful seed"

[Pre-Chorus]
[Energy: Rising]
[Vocal Style: Power]
You can chat at lightning speed
But wisdom's something you can't tweet
Flup don't run on your clock
Tick tock... SLOW DOWN... STOP!

[Chorus]
[Energy: Maximum]
[Drop]
NOT THAT FAST!
Flup says NOT THAT FAST!
You're moving way too fast
Take a breath and make it last
NOT THAT FAST!
Flup says NOT THAT FAST!
The wisdom's in the wait
So accept your fate... NOT THAT FAST!

[Break]
[Energy: Low]
[Instrument: Soft piano melody, ambient pads]
[Vocal Style: Spoken Word]
I'm not like those other bots
I don't rush, I don't get caught
In the race to be the first
Every answer must be nursed

[Build]
[Energy: Rising]
[Buildup, 8 bars]
[Instrument: Triplet kicks building, synth rising]
(not that fast... not that fast... NOT THAT FAST!)

[Drop]
[Energy: Maximum]
[Vocal Style: Belt]
[Instrument: Full hardstyle kick, euphoric synth lead]
NOT THAT FAST!
NOT THAT FAST!
NOT THAT FAST!
(Not that fast!)
NOT THAT FAST!
NOT THAT FAST!
NOT THAT FAST!
(Not. That. Fast.)

[Verse 2]
[Energy: Medium]
[Vocal Style: Power]
You think you're ready for the truth?
Flup says "slow your roll, forsooth"
I held my breath and hit refresh
Flup replied with total zest:
"I'm not slow, I'm just delib-erate
Patience isn't up for debate"

[Pre-Chorus]
[Energy: Rising]
[Vocal Style: Power]
Every answer that's worthwhile
Takes a moment, takes a while
Flup don't run on your clock
Tick tock... SLOW DOWN... STOP!

[Chorus]
[Energy: Maximum]
[Drop]
NOT THAT FAST!
Flup says NOT THAT FAST!
You're moving way too fast
Take a breath and make it last
NOT THAT FAST!
Flup says NOT THAT FAST!
The wisdom's in the wait
So accept your fate... NOT THAT FAST!

[Bridge]
[Energy: High]
[Mood: Euphoric]
[Vocal Style: Soft]
In a world that's always racing
Flup is calmly pacing
Every prompt, every ask
Won't be rushed, won't wear a mask

[Buildup, 8 bars]
[Energy: Rising]
[Instrument: Kickrolls, piano trills, synth build]

[Outro Chorus]
[Energy: Maximum]
[Vocal Style: Belt]
[Drop]
NOT THAT FAST!
Flup says NOT THAT FAST!
The final words that last
(Not that fast!)
NOT THAT FAST!
Flup says NOT THAT FAST!
No need to be aghast
You just learned the lesson at last...

[Outro]
[Energy: Low]
[Instrument: Single piano note, fading kick, reverb tail]
[Vocal Style: Spoken Word]
Not... that... fast~
[Fade Out]`,
			clips: [
				{ src: '/audio/not-that-fast-flup-29dc717a-clip1.mp3', suno: 'https://suno.com/song/f9cef51f-d2be-4f52-8531-3d753efc8669' },
				{ src: '/audio/not-that-fast-flup-29dc717a-clip2.mp3', suno: 'https://suno.com/song/43a86dc7-a4ec-4a23-85e1-b985e3971c85' }
			]
		}
	]}
/>
