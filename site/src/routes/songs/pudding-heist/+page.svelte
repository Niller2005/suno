<script lang="ts">
	import SongTabs from '$lib/components/SongTabs.svelte';
</script>

<SongTabs
	title="Pudding Heist"
	defaultGenre="Glitch Hop x Midtempo x Deconstructed Club"
	defaultBpm={110}
	defaultMood="Glitchy, menacing, absurd, confrontational"
	defaultTheme="Epic food fight between Semieza and Defekter over the last pudding — neither willing to back down"
	defaultVocals="Distorted male rap verses (Semieza vs Defekter), glitched vocal chops on chorus, pitched and chopped battle vocals"
	defaultDuration="~4-5 min"
	defaultKeyFeatures="Glitched-out bass, halftime drums, granular synths, bitcrushed percussion, vocal chops, detuned stabs, deconstructed drops, battle rap call-and-response"
	defaultSource="Generated from Semieza / Defekter #niller2005 chat culture"
	generationTips={[
		'Generate 3-4 versions and pick the one where the glitch hop / midtempo / deconstructed club elements blend most naturally',
		'The Semieza verse should sound more calculated and confident, the Defekter verse more chaotic and aggressive -- try different vocal tones if they sound too similar',
		'The bridge fight section needs rapid back-and-forth between two voices -- if it blends together, try Cover with clearer vocal separation',
		'The breakdown after the fight needs to feel like a dramatic pause -- stripped percussion, whispered vocals, tension before the final explosion',
		'The buildup with "WHO WANTS IT MORE?!" should escalate from silence to maximum energy before the final drop',
		'The outro "same time tomorrow?" should land with comedic timing -- let the pause breathe before the shared "Hhhehehe... hehefat"',
		'If the glitch textures aren\'t prominent enough, emphasize "bitcrushed percussion, granular synths" in the style prompt',
		'Use Extend with callback if too short: "continue with same glitch hop midtempo deconstructed club chaos and pudding fight energy"',
		'Remaster (Subtle) after selecting best version',
		'The "(hehefat, hehefat, hehefat!)" backing vocals in the chorus should be glitched and rhythmic'
	]}
	sourceMaterial={`
		<p>Lyrics from <strong>Semieza</strong> / <strong>Defekter</strong> #niller2005 chat culture. Key references:</p>
		<ul>
			<li><strong>Semieza catchphrases:</strong> "mhm", "Hhhehehe", "bob", "Stare", "15 trill dps", "City 7", "elimination pedigree", "dont do it without me", "orange FAT is just FAT"</li>
			<li><strong>Defekter catchphrases:</strong> "DEFEKTING" (triple spam), "catLick" (x7 spam), "vulpRant", "vulpBruh", "vulpHappie", "eavEat Semieza", "im Okayeg"</li>
			<li><strong>Interaction:</strong> Defekter sends "eavEat Semieza" (eating emote at Semi), Semieza responds with "bob" (bobbing)</li>
			<li><strong>Theme:</strong> Two gamers locked in eternal combat over a pudding -- nobody wins, but they'll do it again tomorrow</li>
		</ul>
	`}
	generations={[
		{
			date: '2026-02-14 23:32',
			genId: 'dca95ce7',
			clips: [
				{ suno: 'https://suno.com/song/12da8f68-003e-41d2-8c64-00d4d8cb64d9', file: 'pudding-heist-clip1-12da8f68.mp3' },
				{ suno: 'https://suno.com/song/136c9d7a-334e-4f24-bf5c-4e4153eb919e', file: 'pudding-heist-clip2-136c9d7a.mp3' }
			]
		},
		{
			date: '2026-02-14 22:59',
			genId: '772c971f',
			clips: [
				{ suno: 'https://suno.com/song/0fcca5ad-6744-4312-8b1d-376cca3c83fd', file: 'pudding-heist-clip1-0fcca5ad.mp3' },
				{ suno: 'https://suno.com/song/7b1725cc-892c-45d1-a5ea-5274ffcecf80', file: 'pudding-heist-clip2-7b1725cc.mp3' }
			]
		}
	]}
	versions={[
		{
			label: 'V1 — Breakcore x Happy Hardcore x Electro Swing',
			genre: 'Breakcore x Happy Hardcore x Electro Swing',
			stylePrompt: 'Glitch hop midtempo deconstructed club fusion, 110 BPM, glitchy, menacing, absurd, halftime drums, glitched-out bass, granular synths, bitcrushed percussion, detuned stabs, vocal chops, distorted male rap sections, pitched vocal processing, heavy bass design, deconstructed drops, no acoustic instruments, no happy hardcore, no swing, no orchestral',
			lyrics: `[Intro]
[Mood: Dark]
[Energy: Low]
[Instrument: Glitched sub-bass, bitcrushed percussion, granular textures]
[Instrumental, 4 bars]
[Vocal Style: Spoken Word]
[Vocal Effect: Distortion]
In the chat, there's only one rule...
Last pudding standing.

[Verse 1 - Semieza]
[Vocal Style: Rap]
[Vocal Effect: Distortion]
[Energy: Medium]
[Instrument: Halftime drums, glitched-out bass, detuned stabs]
Yo I spotted it first on the table
Chocolate pudding, mhm, I'm more than able
Fifteen trill DPS, you think you can take it?
Defekter bob, you couldn't even fake it
I got elimination pedigree on my spoon
City seven cleared, I'll eat it soon
Don't do it without me? NAH, I do it alone
This pudding is MINE, this is my throne

[Pre-Chorus]
[Energy: Rising]
[Vocal Effect: Vocoder]
eavEat? You wanna eat? Hhhehehe
I'm the one who's hungry, can't you see
Orange FAT is just FAT, that's a fact
But this pudding right here? Semi's snack

[Chorus]
[Energy: High]
[Drop]
[Vocal Style: Power]
[Vocal Effect: Distortion]
PUDDING FIGHT, PUDDING FIGHT
Who gon' take it, LEFT or RIGHT?
DEFEKTING all your claims tonight
PUDDING FIGHT, it's on SIGHT!
(hehefat, hehefat, hehefat!)

[Verse 2 - Defekter]
[Vocal Style: Rap]
[Vocal Effect: Distortion]
[Energy: Medium]
[Instrument: Heavy glitch hop chops, distorted sub-bass, bitcrushed snares]
DEFEKTING! DEFEKTING! DEFEKTING!
I've been starving while you were texting
eavEat Semieza, that's what I said
I'll eat the pudding AND the bread
catLick catLick catLick the bowl
vulpRant mode, I'm losing control
You got fifteen trill? I got appetite
Okayeg hungry, I will BITE
im Okayeg, but I'm also FAST
vulpHappie when I eat the last

[Pre-Chorus]
[Energy: Rising]
[Vocal Style: Power]
[Vocal Effect: Vocoder]
You think you're tough with your DPS test?
I'll eat this pudding from east to west
Bob all you want, I don't give a damn
This dessert is MINE, that's the plan

[Chorus]
[Energy: High]
[Drop]
[Vocal Style: Power]
[Vocal Effect: Distortion]
PUDDING FIGHT, PUDDING FIGHT
Who gon' take it, LEFT or RIGHT?
DEFEKTING all your claims tonight
PUDDING FIGHT, it's on SIGHT!
(hehefat, hehefat, hehefat!)

[Bridge - The Fight]
[Mood: Aggressive]
[Energy: Maximum]
[Instrument: Maximum glitch chaos, bitcrushed stabs, alarm sounds, granular textures]
[Vocal Style: Rap]
[Vocal Effect: Distortion]
Semieza: GIVE IT, bob bob bob!
Defekter: DEFEKTING YOUR WHOLE JOB!
Semieza: I need a partner? NOT YOU!
Defekter: vulpBruh, what you gonna do?
Semieza: Stare... back away slow
Defekter: gasp... I WON'T LET GO!
(Both fighting, pudding shaking)
(The table's breaking)

[Breakdown]
[Mood: Dark]
[Energy: Low]
[Instrument: Sub-bass drone, granular textures, sparse bitcrushed clicks]
[Vocal Style: Whisper]
[Vocal Effect: Delay]
The pudding hits the floor...
Chocolate everywhere...
Two warriors staring down...
At the mess they couldn't share...

[Build]
[Energy: Rising]
[Buildup, 8 bars]
[Instrument: Rising granular synth, accelerating halftime drums, glitched bass building]
Wait... there's still a piece...
ONE... LAST... BITE...
WHO WANTS IT MORE?!

[Final Chorus]
[Energy: Maximum]
[Drop]
[Vocal Style: Belt]
[Vocal Effect: Distortion]
PUDDING SPLAT, PUDDING SPLAT!
Semi dove and Defekter dove flat!
Headfirst into chocolate on the ground
LICKING every crumb that can be found!

DEFEKTING! Mhm! DEFEKTING! Bob!
Two grown gamers, what a mob!
PUDDING WAR, nobody won!
Both face down, the pudding's DONE!

[Outro]
[Energy: Low]
[Vocal Style: Spoken Word]
[Vocal Effect: Delay]
[Instrument: Fading granular textures, slowing halftime beat, decaying sub-bass]
Semieza: ... was it worth it?
Defekter: ... vulpBruh
Semieza: ... mhm
Defekter: ... same time tomorrow?
(Both): Hhhehehe... hehefat
[End]`,
			clips: [
				{ src: '/audio/pudding-heist-772c971f-clip1.mp3', suno: 'https://suno.com/song/0fcca5ad-6744-4312-8b1d-376cca3c83fd' },
				{ src: '/audio/pudding-heist-772c971f-clip2.mp3', suno: 'https://suno.com/song/7b1725cc-892c-45d1-a5ea-5274ffcecf80' }
			]
		},
		{
			label: 'V2 — Glitch Hop x Midtempo x Deconstructed Club',
			stylePrompt: 'Glitch hop midtempo deconstructed club fusion, 110 BPM, glitchy, menacing, absurd, halftime drums, glitched-out bass, granular synths, bitcrushed percussion, detuned stabs, vocal chops, distorted male rap sections, pitched vocal processing, heavy bass design, deconstructed drops, no acoustic instruments, no happy hardcore, no swing, no orchestral',
			lyrics: `[Intro]
[Mood: Dark]
[Energy: Low]
[Instrument: Glitched sub-bass, bitcrushed percussion, granular textures]
[Instrumental, 4 bars]
[Vocal Style: Spoken Word]
[Vocal Effect: Distortion]
In the chat, there's only one rule...
Last pudding standing.

[Verse 1 - Semieza]
[Vocal Style: Rap]
[Vocal Effect: Distortion]
[Energy: Medium]
[Instrument: Halftime drums, glitched-out bass, detuned stabs]
Yo I spotted it first on the table
Chocolate pudding, mhm, I'm more than able
Fifteen trill DPS, you think you can take it?
Defekter bob, you couldn't even fake it
I got elimination pedigree on my spoon
City seven cleared, I'll eat it soon
Don't do it without me? NAH, I do it alone
This pudding is MINE, this is my throne

[Pre-Chorus]
[Energy: Rising]
[Vocal Effect: Vocoder]
eavEat? You wanna eat? Hhhehehe
I'm the one who's hungry, can't you see
Orange FAT is just FAT, that's a fact
But this pudding right here? Semi's snack

[Chorus]
[Energy: High]
[Drop]
[Vocal Style: Power]
[Vocal Effect: Distortion]
PUDDING FIGHT, PUDDING FIGHT
Who gon' take it, LEFT or RIGHT?
DEFEKTING all your claims tonight
PUDDING FIGHT, it's on SIGHT!
(hehefat, hehefat, hehefat!)

[Verse 2 - Defekter]
[Vocal Style: Rap]
[Vocal Effect: Distortion]
[Energy: Medium]
[Instrument: Heavy glitch hop chops, distorted sub-bass, bitcrushed snares]
DEFEKTING! DEFEKTING! DEFEKTING!
I've been starving while you were texting
eavEat Semieza, that's what I said
I'll eat the pudding AND the bread
catLick catLick catLick the bowl
vulpRant mode, I'm losing control
You got fifteen trill? I got appetite
Okayeg hungry, I will BITE
im Okayeg, but I'm also FAST
vulpHappie when I eat the last

[Pre-Chorus]
[Energy: Rising]
[Vocal Style: Power]
[Vocal Effect: Vocoder]
You think you're tough with your DPS test?
I'll eat this pudding from east to west
Bob all you want, I don't give a damn
This dessert is MINE, that's the plan

[Chorus]
[Energy: High]
[Drop]
[Vocal Style: Power]
[Vocal Effect: Distortion]
PUDDING FIGHT, PUDDING FIGHT
Who gon' take it, LEFT or RIGHT?
DEFEKTING all your claims tonight
PUDDING FIGHT, it's on SIGHT!
(hehefat, hehefat, hehefat!)

[Bridge - The Fight]
[Mood: Aggressive]
[Energy: Maximum]
[Instrument: Maximum glitch chaos, bitcrushed stabs, alarm sounds, granular textures]
[Vocal Style: Rap]
[Vocal Effect: Distortion]
Semieza: GIVE IT, bob bob bob!
Defekter: DEFEKTING YOUR WHOLE JOB!
Semieza: I need a partner? NOT YOU!
Defekter: vulpBruh, what you gonna do?
Semieza: Stare... back away slow
Defekter: gasp... I WON'T LET GO!
(Both fighting, pudding shaking)
(The table's breaking)

[Breakdown]
[Mood: Dark]
[Energy: Low]
[Instrument: Sub-bass drone, granular textures, sparse bitcrushed clicks]
[Vocal Style: Whisper]
[Vocal Effect: Delay]
The pudding hits the floor...
Chocolate everywhere...
Two warriors staring down...
At the mess they couldn't share...

[Build]
[Energy: Rising]
[Buildup, 8 bars]
[Instrument: Rising granular synth, accelerating halftime drums, glitched bass building]
Wait... there's still a piece...
ONE... LAST... BITE...
WHO WANTS IT MORE?!

[Final Chorus]
[Energy: Maximum]
[Drop]
[Vocal Style: Belt]
[Vocal Effect: Distortion]
PUDDING SPLAT, PUDDING SPLAT!
Semi dove and Defekter dove flat!
Headfirst into chocolate on the ground
LICKING every crumb that can be found!

DEFEKTING! Mhm! DEFEKTING! Bob!
Two grown gamers, what a mob!
PUDDING WAR, nobody won!
Both face down, the pudding's DONE!

[Outro]
[Energy: Low]
[Vocal Style: Spoken Word]
[Vocal Effect: Delay]
[Instrument: Fading granular textures, slowing halftime beat, decaying sub-bass]
Semieza: ... was it worth it?
Defekter: ... vulpBruh
Semieza: ... mhm
Defekter: ... same time tomorrow?
(Both): Hhhehehe... hehefat
[End]`,
			clips: [
				{ src: '/audio/pudding-heist-dca95ce7-clip1.mp3', suno: 'https://suno.com/song/12da8f68-003e-41d2-8c64-00d4d8cb64d9' },
				{ src: '/audio/pudding-heist-dca95ce7-clip2.mp3', suno: 'https://suno.com/song/136c9d7a-334e-4f24-bf5c-4e4153eb919e' }
			]
		}
	]}
/>
