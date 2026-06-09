<script lang="ts">
	import SongTabs from '$lib/components/SongTabs.svelte';
</script>

<SongTabs
	title="Beacon Baron"
	defaultGenre="Trap / Grime"
	defaultBpm={140}
	defaultMood="Aggressive, braggadocious, chaotic, confrontational"
	defaultTheme="Torchlight Infinite beacon farming flex / orangessfat vs nrpHD trash talk war"
	defaultVocals="Aggressive male rap with shouted ad-libs, dual voice for nrpHD rage responses"
	defaultDuration="~4-5 min"
	defaultKeyFeatures="Heavy 808 slides, grime synth stabs, rolling hi-hats, call-and-response rage sections, hard drops on taunt lines, distorted bass"
	defaultSource="Generated from orangessfat &amp; Semieza chat logs in #niller2005"
	generationTips={[
		'Generate 3-4 versions and pick the one with the heaviest 808 slides and grimiest synth stabs',
		'The call-and-response between orangessfat and nrpHD is crucial — if the vocal tone doesn\'t shift for Verse 2, try a Cover with a different vocal persona for nrpHD\'s part',
		'The chorus needs to HIT with maximum aggression on the UPPERCASE lines — "BEACON BARON" should feel like a war cry',
		'The bridge whisper section should contrast hard against the final chorus explosion',
		'If the 808s sound too clean/thin, add "distorted heavy 808" to the style prompt',
		'Use Extend with callback if too short: "continue with same trap grime beacon baron energy and aggressive taunting vibe"',
		'Remaster (Subtle) after selecting best version',
		'The "nrpMad! nrpMad!" ad-libs should hit like punches between chorus lines — if they\'re missing, try Replace Section'
	]}
	sourceMaterial={`
		<p>Lyrics generated from chat messages by <strong>orangessfat</strong> in <strong>#niller2005</strong> channel. Key references:</p>
		<ul>
			<li>TLI (Torchlight Infinite) gameplay: deep space beacons (28 FE each), flame elementium, 30 FE per map, 15 beacons farmed, rainbow beacon card, god of war mechanic (8% spawn), profound farming, 40-second map clears, 1.3k FE/hour, vorax, armor stacking</li>
			<li>orangessfat vs nrpHD rivalry: "peel me a pomegranate nrpHD", "you are a luxury nrpHD", "are you evil dog of death nrpHD", constant "shut the fuck up" exchanges</li>
			<li>Catchphrases: "fuh", "fuh bozos", "stfu", "dumbfuck", "bitchass", "hoe", "cunt ass bitch", "deal with it", "mhm", "danki", "Smile", "nerpnerp", "bark"</li>
			<li>nrpHD rage culture: "RAGEY", "nrpMad", "MadChatting", keyboard warrior energy</li>
			<li>Real gameplay stats: stood in fire, HP regens every 10 seconds, city defence 7-15 struggles, Semieza carry references</li>
		</ul>
	`}
	generations={[
		{
			date: '2026-02-15 00:03',
			genId: '750da1df',
			clips: [
				{ suno: 'https://suno.com/song/4d6ca078-f028-401c-8b5d-7d78856947bd', file: 'beacon-baron-clip1-4d6ca078.mp3' },
				{ suno: 'https://suno.com/song/cdf9d02d-3fff-444e-a7ff-f8d249b02ad7', file: 'beacon-baron-clip2-cdf9d02d.mp3' }
			]
		},
		{
			date: '2026-02-14 23:44',
			genId: 'de7e15c4',
			clips: [
				{ suno: 'https://suno.com/song/cdeb27bf-f757-4663-b155-dfe7ac248239', file: 'beacon-baron-clip1-cdeb27bf.mp3' },
				{ suno: 'https://suno.com/song/0f5f872e-a3d8-4e20-9be7-0db9d5fa41c7', file: 'beacon-baron-clip2-0f5f872e.mp3' }
			]
		}
	]}
	versions={[
		{
			label: 'V1 — Trap / Grime',
			stylePrompt: 'Trap grime hybrid, 140 BPM, aggressive, heavy sliding 808 bass, rolling hi-hats, dark grime synth stabs, distorted sub bass, hard-hitting snares, braggadocious male rap, shouted vocals, call and response, confrontational energy, UK grime influence, no acoustic guitar, no piano ballad, no clean pop vocals',
			lyrics: `[Intro]
[Mood: Dark]
[Energy: Medium]
[Instrument: Deep 808 slide, grime synth stab, rolling hi-hats]
[Instrumental, 4 bars]
[Vocal Style: Spoken Word]
[Vocal Effect: Distortion]
(Ayo nrpHD...)
(You hear that sound?)
(That's flame elementium, bitch...)

[Verse 1]
[Vocal Style: Rap]
[Energy: High]
Fifteen beacons in the bag, I'm the baron
Deep space drops while you dyin' and starin'
Eight percent spawn rate, I'm the chosen one
God of war mechanic, look what I've done

Thirty FE every map, it's a minute flat
Forty second clears, can you handle that?
Rainbow beacon card, yeah I got that too
nrpHD peel me a pomegranate, thank you

[Pre-Chorus]
[Energy: Rising]
[Vocal Style: Power]
Twenty-eight FE per beacon, do the math
One-point-three K per hour on my path
You still dyin' to turrets on floor seven
I'm sellin' stacks of beacons, this is heaven

[Chorus]
[Energy: Maximum]
[Drop]
[Vocal Style: Belt]
BEACON BARON, FLAME ELEMENTIUM KING
Sellin' all these beacons, hear the register ring!
FUH U NRPHD, SHUT THE FUCK UP HOE
I make bank while you rage in the chat below!

(nrpMad! nrpMad!)
BEACON BARON, stackin' FE to the sky
Your DPS is dogshit and you wonder why!
Dumbfuck, bitchass, sit the fuck down
I'm the beacon baron, wear the fuckin' crown!

[Verse 2 - nrpHD Response]
[Vocal Style: Raspy]
[Energy: High]
[Mood: Aggressive]
You think you're hot shit with your beacon stash?
Your build is mid, your armor's trash
I'll type so fast your chat will SCROLL
MadChatting, RAGEY, losing control

You fat orange farming little beacons all day
While I'm pushin' content in the real way
City defence seven-fifteen, you can't clear
Carried by Semieza, let me make that clear

[Pre-Chorus - orangessfat Clap Back]
[Vocal Style: Rap]
[Energy: Rising]
Fuh bozos, fuh sen, fuh you too
I stood in fire and I made it through
My HP regens once every ten
But I'm still alive and I'll farm again

[Chorus]
[Energy: Maximum]
[Drop]
[Vocal Style: Belt]
BEACON BARON, FLAME ELEMENTIUM KING!
Sellin' all these beacons, hear the register ring!
FUH U NRPHD, SHUT THE FUCK UP HOE!
I make bank while you rage in the chat below!

(nrpMad! nrpMad!)
BEACON BARON, stackin' FE to the sky!
Your DPS is dogshit and you wonder why!
Dumbfuck, bitchass, sit the fuck down!
I'm the beacon baron, wear the fuckin' crown!

[Bridge - The Rage Escalation]
[Mood: Dark]
[Energy: Medium]
[Vocal Style: Whisper]
[Instrument: Stripped 808, dark grime pads]
nrpHD typin' paragraphs in the chat
Keyboard warrior, imagine that
"You are a luxury nrpHD," I said
Now he's RAGEY, face turnin' red

[Build]
[Energy: Rising]
[Vocal Style: Spoken Word]
Only five beacons this time, that's the worst
But I sold 'em all and I quenched my thirst
Semieza saw the prices, I said watch
After seein' beacon FE, I farm nonstop

[Vocal Style: Power]
[Energy: High]
ARE YOU EVIL DOG OF DEATH NRPHD?
BARK BARK BARK, that's all I see!
STOP BEING A WHINY IDIOT, SIT DOWN
CUNT ASS BITCH, I RUN THIS TOWN

[Buildup, 4 bars]
[Energy: Rising]

[Chorus]
[Energy: Maximum]
[Vocal Style: Belt]
[Drop]
BEACON BARON, FLAME ELEMENTIUM KING!
SELLIN' ALL THESE BEACONS, HEAR THE REGISTER RING!
FUH U NRPHD, SHUT THE FUCK UP HOE!
I MAKE BANK WHILE YOU RAGE IN THE CHAT BELOW!

(NRPMAD! NRPMAD!)
BEACON BARON, STACKIN' FE TO THE SKY!
YOUR DPS IS DOGSHIT AND YOU WONDER WHY!
DUMBFUCK, BITCHASS, SIT THE FUCK DOWN!
I'M THE BEACON BARON, WEAR THE FUCKIN' CROWN!

[Outro]
[Energy: Medium]
[Vocal Style: Whisper]
[Vocal Effect: Delay]
[Instrument: Fading 808, echoing grime stab]
Fuh real, fuh real, fuh in fuh reak...
nrpHD still typin', what a freak...
Beacon baron, flame elementium ~king~...
(mhm... danki... mhm...)
Deal with it, Smile...
[Fade Out]`,
			clips: [
				{ src: '/audio/beacon-baron-de7e15c4-clip1.mp3', suno: 'https://suno.com/song/cdeb27bf-f757-4663-b155-dfe7ac248239' },
				{ src: '/audio/beacon-baron-de7e15c4-clip2.mp3', suno: 'https://suno.com/song/0f5f872e-a3d8-4e20-9be7-0db9d5fa41c7' }
			]
		},
		{
			label: 'V2 — Electro Swing DnB',
			stylePrompt: 'Electro swing drum and bass fusion, 140 BPM, aggressive, energetic, heavy 808 slides, dark grime synth stabs, rolling hi-hats, swung beats, deep sub bass, orchestral stabs, braggadocious male rap, shouted vocals, call and response, confrontational energy, no acoustic guitar, no piano ballad',
			lyrics: `[Intro]
[Mood: Dark]
[Energy: Medium]
[Instrument: Swung beat, deep sub bass, orchestral stab]
[Instrumental, 4 bars]
[Vocal Style: Spoken Word]
[Vocal Effect: Vocoder]
(Here we go again...)

[Verse 1]
[Vocal Style: Rap]
[Energy: High]
Same beacon grinder, different beat
Fifteen deep space, can't be beat
Eight percent spawn, I'm still the one
God of war, look what I've done

I told you once, I'll tell you twice
My FE stack is looking nice
One-point-three K per hour, watch me thrive
nrpHD can't keep up, I'm in overdrive

[Chorus]
[Energy: Maximum]
[Drop]
BEACON BARON, I'M THE KING
Hear my register, watch it ring
Stackin' beacons, stackin' FE
nrpHD can't get to me

(nrpMad! nrpMad!)
BEACON BARON, TO THE SKY
Watch me flexin', watch me fly
Dumbfuck BOZO, sit back down
I STILL WEAR THE FUCKIN' CROWN

[Outro]
[Vocal Style: Spoken Word]
[Vocal Effect: Delay]
Same story, different beat...
Still the baron...
Deal with it...`,
			clips: [
				{ src: '/audio/beacon-baron-750da1df-clip1.mp3', suno: 'https://suno.com/song/4d6ca078-f028-401c-8b5d-7d78856947bd' },
				{ src: '/audio/beacon-baron-750da1df-clip2.mp3', suno: 'https://suno.com/song/cdf9d02d-3fff-444e-a7ff-f8d249b02ad7' }
			]
		}
	]}
/>
