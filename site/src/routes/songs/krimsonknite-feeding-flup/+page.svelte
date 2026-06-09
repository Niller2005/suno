<script lang="ts">
	import SongTabs from '$lib/components/SongTabs.svelte';

	const stylePrompt =
		'Drum and Bass neurofunk, 174 BPM, chaotic, heavy, absurd, aggressive, comedic, rolling breaks, Reese bass, neurofunk basslines, amen breaks, heavy sub-bass, aggressive drops, distorted vocal chops, no acoustic guitar, no orchestral, no happy hardcore, no piano ballad';

	const lyrics = `[Intro]
[Mood: Dark]
[Energy: Low]
[Vocal Style: Spoken Word]
[Instrument: Sub-bass drone, sparse drums, tension building]
Here comes Krimsonknite with a plate
Time to feed, can't escape your fate

[Verse 1 - Krimsonknite]
[Vocal Style: Rap]
[Energy: Medium]
[Instrument: Rolling breaks, Reese bass, neurofunk stabs]
Open wide, it's feeding time
Gonna make this belly climb
Burgers, fries, and milkshake too
Every single bite for you
Don't you dare to run away
You're my project, you're my prey
Chew it fast, don't make me wait
Gonna make you overweight

[Chorus]
[Energy: High]
[Drop]
[Vocal Style: Power]
[Vocal Effect: Distortion]
SUPER FAT FLUP, SUPER FAT
Krimson's feast, you can't combat
Growing rounder, growing wide
Belly bounce from side to side
SUPER FAT FLUP, SUPER FAT
No more skinny, that is that
Feeding you until you pop
Food won't ever, ever stop

[Verse 2 - Flup's Doom]
[Vocal Style: Rap]
[Energy: Medium]
[Instrument: Heavy breaks, distorted sub-bass, neurofunk wobbles]
Used to fit inside my chair
Now I'm wider than a bear
Krimson says it's just the start
Gonna have to grow a part
Plate on plate, the stack is high
Watch me swell, watch me comply
Belt is snapping, buttons fly
Reaching for another pie

[Pre-Chorus]
[Energy: Rising]
[Vocal Style: Power]
[Vocal Effect: Reverb]
He's getting bigger, can't you see?
The ultimate feeding spree
One more plate, one more pound
Krimson won't stop around

[Chorus]
[Energy: High]
[Drop]
[Vocal Style: Power]
[Vocal Effect: Distortion]
SUPER FAT FLUP, SUPER FAT
Krimson's feast, you can't combat
Growing rounder, growing wide
Belly bounce from side to side
SUPER FAT FLUP, SUPER FAT
No more skinny, that is that
Feeding you until you pop
Food won't ever, ever stop

[Bridge - Maximum Feed]
[Energy: Maximum]
[Mood: Aggressive]
[Vocal Style: Power]
[Instrument: Maximum drum chaos, distorted Reese bass, alarm sounds]
FEED HIM! FEED HIM! MORE AND MORE!
HE'S GONNA BURST ON THE FLOOR!
SWALLOW! CHEW! OPEN WIDE!
KRIMSONKNITE WON'T BE DENIED!

[Buildup]
[Energy: Rising]
[Buildup, 8 bars]
[Instrument: Rising Reese bass, accelerating rolling breaks, distorted synths]
Almost at maximum size
One more bite to win the prize
SUPER... FAT... FLUUUUUUP!

[Final Chorus]
[Energy: Maximum]
[Drop]
[Vocal Style: Belt]
[Vocal Effect: Distortion]
SUPER FAT FLUP, SUPER FAT
Krimsonknite served up the stack
Rounder, wider, can't control
Krimson owns your very soul
SUPER FAT FLUP, SUPER FAT
Stretching out your new fur mat
Food coma, cannot escape
This is your ultimate fate

[Outro]
[Energy: Low]
[Vocal Style: Soft]
[Vocal Effect: Delay]
[Instrument: Fading breaks, decaying sub-bass, sparse percussion]
Belly full... can't move at all...
Krimson smiles... watching Flup grow...
Hhhhehehe... so... fat...
[Fade Out]`;
</script>

<SongTabs
	title="Krimsonknite Feeding Flup"
	defaultGenre="Drum and Bass / Neurofunk"
	defaultBpm={174}
	defaultMood="Chaotic, heavy, absurd, aggressive, comedic"
	defaultTheme="Krimsonknite force-feeding Flup to make him super fat — an unstoppable feeding frenzy"
	defaultVocals="Aggressive male rap verses, shouted chorus hooks, spoken word intro"
	defaultDuration="~3-4 min"
	defaultKeyFeatures="Rolling breaks, Reese bass, neurofunk basslines, amen breaks, heavy sub-bass, aggressive drops, distorted vocal chops"
	defaultSource="#niller2005 chat culture — Krimsonknite and Flup memes"
	generationTips={[
		'Generate 3-4 versions and pick the one where the neurofunk bass and rolling breaks hit hardest',
		'The intro should feel ominous and tense — like a predator stalking prey, but the prey is a buffet',
		'Verse 1 (Krimsonknite) should sound confident and menacing, like a villain monologuing about their evil plan',
		'The chorus "SUPER FAT FLUP" needs to be a massive shouted hook — if it doesn\'t land with enough aggression, try Cover with a heavier vocal tone',
		'Verse 2 should feel more desperate and chaotic, as Flup realizes he can\'t escape his fate',
		'The bridge "FEED HIM! FEED HIM!" should be absolute drum and bass chaos — rapid-fire shouting over maximum energy breaks',
		'The buildup "SUPER... FAT... FLUUUUUUP!" needs dramatic pause before the final drop — make sure the tension peaks correctly',
		'The outro "Hhhhehehe... so... fat..." should land with creepy comedic timing — let the delay trail off into silence',
		'If the bass isn\'t heavy enough, emphasize "Reese bass, neurofunk basslines, heavy sub-bass" in the style prompt',
		'Use Extend with callback if too short: "continue with same drum and bass neurofunk chaos and super fat flup feeding energy"',
		'Remaster (Subtle) after selecting best version for a polished, heavy mix'
	]}
	generations={[
		{
			date: '2026-04-22 14:49',
			genId: 'e5ae9909',
			clips: [
				{ suno: 'https://suno.com/song/f966f832-58f1-42d3-8480-99900674d5cb', file: 'krimsonknite-feeding-flup-clip1-f966f832.mp3' },
				{ suno: 'https://suno.com/song/6e61ee5a-30a5-4159-8094-112c11b8f3f9', file: 'krimsonknite-feeding-flup-clip2-6e61ee5a.mp3' }
			]
		}
	]}
	versions={[
		{
			label: 'V1 — Drum and Bass / Neurofunk',
			stylePrompt,
			lyrics,
			clips: [
				{ src: '/audio/krimsonknite-feeding-flup-e5ae9909-clip1.mp3', suno: 'https://suno.com/song/f966f832-58f1-42d3-8480-99900674d5cb' },
				{ src: '/audio/krimsonknite-feeding-flup-e5ae9909-clip2.mp3', suno: 'https://suno.com/song/6e61ee5a-30a5-4159-8094-112c11b8f3f9' }
			]
		}
	]}
/>
