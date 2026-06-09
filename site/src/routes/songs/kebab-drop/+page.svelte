<script lang="ts">
	import SongTabs from '$lib/components/SongTabs.svelte';

	const stylePrompt =
		'Heartfelt male vocals, emotional pop-punk delivery. Hyper melodic drum and bass, 174 BPM, joyous anthemic emotional, bright uplifting synths, breaks-laden beats, rock-infused production, catchy hooks, festival energy, dreamy atmosphere, no aggressive rap, no dark neurofunk, no heavy distortion';

	const lyrics = `[Intro]
[Mood: Dreamy]
[Energy: Low]
[Instrument: Bright synth pads, sparse breaks, atmospheric]
[Instrumental, 4 bars]
[Vocal Style: Soft]
[Vocal Effect: Reverb]
Out in the haze the night feels wrong
Everyone else seems to belong
The lights pull me down the street
A dreamland waiting for my feet

[Verse 1]
[Vocal Style: Open, Emotional]
[Energy: Medium]
Stepping in from the rave's last roar
Hunger hits like never before
The world outside is spinning fast
But here the moment seems to last
Order up the wrap comes hot
This is the peace I've always sought

[Pre-Chorus]
[Energy: Rising]
[Build]
One bite in and the bass rolls deep
In this dreamland I can finally sleep

[Chorus]
[Energy: High]
[Drop]
[Vocal Style: Power]
IN THIS DREAMLAND KEBAB IN HAND
SAUCE ON MY FINGERS I UNDERSTAND
THE CHAOS FADES IN THIS PERFECT MESS
BASS IN MY CHEST I FEEL BLESSED
DREAMLAND THIS IS THE PLACE
LAMB AND BREAD AND TIME ERASED
UNDER THE LIGHTS THE WORLD FEELS RIGHT
THIS KEBAB RUN MY GUIDING LIGHT

[Verse 2]
[Vocal Style: Open, Emotional]
[Energy: Medium]
Juicy meat and the chips inside
All the questions seem to subside
Everyone's searching for something true
I found mine in this sauce and you
The foil crinkles the steam rises high
This is the dream I can't deny

[Pre-Chorus]
[Energy: Rising]
[Callback: continue with same vibe as chorus]
One more bite and the drop hits clean
In this dreamland I'm finally seen

[Chorus]
[Energy: High]
[Drop]
[Vocal Style: Power]
IN THIS DREAMLAND KEBAB IN HAND
SAUCE ON MY FINGERS I UNDERSTAND
THE CHAOS FADES IN THIS PERFECT MESS
BASS IN MY CHEST I FEEL BLESSED

[Bridge - The Revelation]
[Mood: Triumphant]
[Energy: Maximum]
[Instrument: Rock-infused synth riffs, full breaks, bright leads]
Am I the only one who finds it here
In the mess and the bass and the cheer
The world keeps spinning but I stand still
This dreamland moment this is real

[Build]
[Energy: Rising]
[Buildup, 8 bars]
Last bites coming the night won't last
But this feeling is built to last

[Final Chorus]
[Energy: Maximum]
[Drop]
[Vocal Style: Belt]
IN THIS DREAMLAND KEBAB IN HAND
SAUCE ON MY FINGERS I UNDERSTAND
FULL BELLY BASS AND A HEART SET FREE
THIS IS THE DREAM THIS IS ME

[Outro]
[Energy: Low]
[Vocal Style: Soft]
[Instrument: Fading melodic synths, slowing breaks]
Satisfied the walk back home
Dreamland lingers in every bone
Until next time the lights call me
Kebab bass harmony
[Fade Out]
[End]`;
</script>

<SongTabs
	title="Kebab Drop"
	defaultGenre="Hyper Melodic Drum and Bass / Pop-Rock DNB"
	defaultBpm={174}
	defaultMood="Joyous, anthemic, emotional, euphoric, dreamy"
	defaultTheme="Late-night kebab run as a personal dreamland escape"
	defaultVocals="Heartfelt male singer-songwriter vocals with pop-punk edge"
	defaultDuration="~3-4 min"
	defaultKeyFeatures="Breaks-laden DNB beats, bright hyper-melodic synth leads, rock-infused riffs and drops"
	generationTips={[
		'Generate 3-4 versions on v5.5 (chirp-fenix); pick the one with the strongest bright hyper-melodic synth leads and most emotional heartfelt male vocal delivery',
		'The pop-rock fusion in the drops needs rock-infused riffs/synths to cut through the breaks — emphasize "rock-infused production, bright uplifting synths" if the hybrid feel is missing',
		'Pre-chorus should build like a Fox Stevenson-style emotional lift into the anthemic chorus drop',
		'Chorus "IN THIS DREAMLAND..." must land as a joyous sing-along anthem — powerful, repeatable, emotional',
		'Bridge revelation section needs the rock energy peak before the final chorus explosion',
		'Use Extend + callback if short: "continue with same hyper melodic drum and bass pop-rock fusion dreamland energy and emotional vocal performance"',
		'Remaster (Subtle) after best pick for polished fusion mix',
		'New style for V3 generation — previous V1/V2 tabs preserve the old rap/MC versions for comparison'
	]}
	generations={[
		{
			date: '2026-06-08 13:00',
			genId: '1e6e6a19',
			clips: [
				{ suno: 'https://suno.com/song/99be1e52-492b-41f4-869d-c01c1b28e313', file: 'kebab-drop-clip1-99be1e52.mp3' },
				{ suno: 'https://suno.com/song/ecc33653-5b4a-4eb5-ad6a-c0223538e67d', file: 'kebab-drop-clip2-ecc33653.mp3' }
			]
		},
		{
			date: '2026-06-08 12:54',
			genId: '33cfddc2',
			clips: [
				{ suno: 'https://suno.com/song/c9c73ec4-30f6-4c6c-ac15-a679def2edf7', file: 'kebab-drop-clip1-c9c73ec4.mp3' },
				{ suno: 'https://suno.com/song/35f2a9f2-03c1-4e06-bbfa-88237be54e3b', file: 'kebab-drop-clip2-35f2a9f2.mp3' }
			]
		},
		{
			date: '2026-06-08 12:08',
			genId: '09eaa053',
			clips: [
				{ suno: 'https://suno.com/song/c16e8ae4-8cb3-4734-adef-7d87b63e3d72', file: 'kebab-drop-clip1-c16e8ae4.mp3' },
				{ suno: 'https://suno.com/song/858198ea-6fef-4bcc-92c3-2febf5888645', file: 'kebab-drop-clip2-858198ea.mp3' }
			]
		}
	]}
	versions={[
		{
			label: 'V1 — Drum and Bass (v5 / chirp-crow)',
			stylePrompt,
			lyrics,
			clips: [
				{ src: '/audio/kebab-drop-09eaa053-clip1.mp3', suno: 'https://suno.com/song/c16e8ae4-8cb3-4734-adef-7d87b63e3d72' },
				{ src: '/audio/kebab-drop-09eaa053-clip2.mp3', suno: 'https://suno.com/song/858198ea-6fef-4bcc-92c3-2febf5888645' }
			]
		},
		{
			label: 'V2 — Drum and Bass (v5.5 / chirp-fenix)',
			stylePrompt,
			lyrics,
			clips: [
				{ src: '/audio/kebab-drop-33cfddc2-clip1.mp3', suno: 'https://suno.com/song/c9c73ec4-30f6-4c6c-ac15-a679def2edf7' },
				{ src: '/audio/kebab-drop-33cfddc2-clip2.mp3', suno: 'https://suno.com/song/35f2a9f2-03c1-4e06-bbfa-88237be54e3b' }
			]
		},
		{
			label: 'V3 — Hyper Melodic DNB (Dreamland)',
			stylePrompt,
			lyrics,
			clips: [
				{ src: '/audio/kebab-drop-1e6e6a19-clip1.mp3', suno: 'https://suno.com/song/99be1e52-492b-41f4-869d-c01c1b28e313' },
				{ src: '/audio/kebab-drop-1e6e6a19-clip2.mp3', suno: 'https://suno.com/song/ecc33653-5b4a-4eb5-ad6a-c0223538e67d' }
			]
		}
	]}
/>
