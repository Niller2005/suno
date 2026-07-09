<script lang="ts">
	import SongTabs from '$lib/components/SongTabs.svelte';
</script>

<SongTabs
	title="Defeat Pump"
	defaultGenre="Electro Swing / Drum & Bass / UK Garage"
	defaultBpm={155}
	defaultMood="Aggressive, comedic, dark cabaret, high-energy rave"
	defaultTheme="Summer heat / broken heat pump / incompetent technician / gaming rage / cyberpunk meltdown"
	defaultVocals="Male rapper, aggressive comedic delivery, rapid-fire flow, shouted ad-libs, spoken word interludes"
	defaultDuration="~4-5 min"
	defaultKeyFeatures="Amen breakbeat, 2-step UKG shuffle, swing rhythm brass stabs, sub-bass, jump-up bassline, dark cabaret synths, glitch FX, festival production"
	generationTips={[
		'Generate 3-4 versions and pick the one with the tightest DnB breakbeat and hardest UKG shuffle',
		'The rap at 155 BPM needs rapid-fire delivery — if Suno slows it down, try adding "fast rapping" to the style prompt',
		'The "trump trump" in the chorus should hit as a sharp stutter over the 2-step beat',
		'Listen for sub-bass presence — DnB/UKG rely on heavy sub for impact',
		'Use Extend with callback if too short: "continue with the same electro swing DnB energy and brass stabs"',
		'Remaster (Subtle) after selecting best version',
		'Watch for vocal clarity at high BPM — if garbled, regenerate with "clear vocals" emphasis',
		'The bridge should drop to halftime feel before the final chorus erupts'
	]}
	generations={[
		{
			date: '2026-07-09 11:19',
			genId: 'bcc8593c',
			clips: [
				{ suno: 'https://suno.com/song/91c11184-a1d8-4d65-a95d-7242abdfb82a', file: 'defeat-pump-clip1-91c11184.mp3' },
				{ suno: 'https://suno.com/song/b774d445-3dfc-441a-8e5e-a25cca6da7b1', file: 'defeat-pump-clip2-b774d445.mp3' }
			]
		},
		{
			date: '2026-07-09 11:33',
			genId: 'c8fc9224',
			clips: [
				{ suno: 'https://suno.com/song/c0b2d5fe-39e6-43a9-aee7-1703aa4fa9fa', file: 'defeat-pump-clip1-c0b2d5fe.mp3' },
				{ suno: 'https://suno.com/song/3d80e337-ce9a-4126-badb-7c021a1fc05d', file: 'defeat-pump-clip2-3d80e337.mp3' }
			]
		}
	]}
	versions={[
		{
			label: 'V1 — Electroswing / Rap / Cyberpunk',
			stylePrompt: 'Male rapper, aggressive comedic delivery, rapid-fire flow, shouted ad-libs, spoken word interludes. Electro swing drum and bass with UK garage influences, 155 BPM, energetic, amen breakbeat, 2-step shuffle, swing rhythm, brass stabs, sub-bass, dark cabaret synths, glitch FX, festival production, no guitar, no acoustic instruments, no ballad',
			lyrics: `[Intro]
[Mood: Dark Cabaret, Comedic]
[Energy: Low]
[Instrument: Brass Stabs, Synth Pads, Swing Beat]
Mhm... summer heat...
Sweatin' my balls off, tryna game...
Sigh... come fix me please...

[Verse 1]
[Vocal Style: Rap]
[Energy: Medium]
[Instrument: 808 Bass, Brass Section, Swing Rhythm]
Sun beatin' down, thirty degrees no escape
Living room's a sauna, this heat pump is fake
Balls glued to the chair while I'm tryna rank up
Controller slippin', vision blank, I give up

Called the damn tech, bring the thermistor through
You braindead fuck, make the water run cool
I need that chill flow in the pipes, mhm
Game in peace without meltin' in the sun again

[Pre-Chorus]
[Energy: Rising]
[Instrument: String Stabs, Drum Build, Glitch FX]
He said no problem, I got the part right here
Smile on his face but I knew this wappla's weird
Stepped out for a sec, grabbed a cold drink, LO
Heard a crash, my heart dropped, what the fuck you done bro

[Chorus]
[Energy: High]
[Vocal Style: Power]
Now my heat pump's bricked, turned to a defeat pump
Blowin' hot air like Bibi speechin', trump trump
Sigh... what have you done, you incompetent clown
Was s'posed to cool my summer, now it's burnin' me down

Yawn in the heat, sweat drippin' on the screen
Thermistor dreams shattered, everything's mid, this machine
It's minus twenty in my soul, no coolin' between
This pump ain't coolin' water, it's roastin' me, you dumb fuck

[Instrumental]
[Energy: High]
[Instrument: Brass Stabs, Glitchy Synth Solo, Swing Break]
[Instrumental, 4 bars]

[Verse 2]
[Vocal Style: Rap]
[Energy: Medium]
[Instrument: Dark Synth Pads, 808 Bass, Cyberpunk FX]
I was tryna get that crisp 1440p flow
High refresh rate, cool room, perfect gaming glow
Now it's blastin' desert winds mixed with Israel tunes
Background changed to Benjamin, whole system doomed you

Fat-fingered idiot, probably did it on purpose
Heat pump's a casino now, rollin' 25s, gorgeous
Pumpin' hot regret straight through every vent
Cybernetic nightmare, circuit dreams all spent

[Bridge]
[Mood: Dark, Melancholic]
[Energy: Low]
[Instrument: Sad Synth Brass, Distorted Piano, Digital Glitch]
I just wanted summer coolin', not this chaos, mhm
Now it's a war crime of a system, you dumbfuck
Sad trombones playin' when I try to sleep
Whispers halt dein maul when the temperature creeps

[Energy: Rising]
WideOmE... what have we become, you braindead cunt
Neon lights flicker, my sanity's on the run
Dance hall of disaster, electroswing of pain
This heat pump's a villain drippin' chrome in the rain

[Final Chorus]
[Energy: Maximum]
[Vocal Style: Belt, Aggressive]
Now my heat pump's bricked, full defeat pump legacy
Blowin' hot takes and football VAR conspiracy
Sigh... technician you did me dirty, worthless prick
Was s'posed to save the summer, now it's straight-up hurtin'

Yawn in the heat, balls officially gone
Thermistor turned traitor, singin' the wrong song
Mhm... good night pokiKiss, I'm signin' off
ICANT in this melted room, fuck you krimsonknite

[Outro]
[Energy: Low → Fade]
[Mood: Defeated, Comedic]
Sigh...
Could rename this whole summer to yawn...
Thermistor... why you do me like that, you piece of shit...
Mhm...`,
			clips: [
				{ src: '/audio/defeat-pump-bcc8593c-clip1.mp3', suno: 'https://suno.com/song/91c11184-a1d8-4d65-a95d-7242abdfb82a' },
				{ src: '/audio/defeat-pump-bcc8593c-clip2.mp3', suno: 'https://suno.com/song/b774d445-3dfc-441a-8e5e-a25cca6da7b1' }
			]
		},
		{
			label: 'V2 — Electro Swing / DnB / UKG',
			stylePrompt: 'Male rapper, aggressive comedic delivery, rapid-fire flow, shouted ad-libs, spoken word interludes. Electro swing drum and bass with UK garage influences, 155 BPM, energetic, amen breakbeat, 2-step shuffle, swing rhythm, brass stabs, sub-bass, dark cabaret synths, glitch FX, festival production, no guitar, no acoustic instruments, no ballad',
			lyrics: `[Intro]
[Mood: Dark Cabaret, Comedic]
[Energy: Low]
[Instrument: Brass Stabs, Synth Pads, Swing Beat]
Mhm... summer heat...
Sweatin' my balls off, tryna game...
Sigh... come fix me please...

[Verse 1]
[Vocal Style: Rap]
[Energy: Medium]
[Instrument: 808 Bass, Brass Section, Swing Rhythm]
Sun beatin' down, thirty degrees no escape
Living room's a sauna, this heat pump is fake
Balls glued to the chair while I'm tryna rank up
Controller slippin', vision blank, I give up

Called the damn tech, bring the thermistor through
You braindead fuck, make the water run cool
I need that chill flow in the pipes, mhm
Game in peace without meltin' in the sun again

[Pre-Chorus]
[Energy: Rising]
[Instrument: String Stabs, Drum Build, Glitch FX]
He said no problem, I got the part right here
Smile on his face but I knew this wappla's weird
Stepped out for a sec, grabbed a cold drink, LO
Heard a crash, my heart dropped, what the fuck you done bro

[Chorus]
[Energy: High]
[Vocal Style: Power]
Now my heat pump's bricked, turned to a defeat pump
Blowin' hot air like Bibi speechin', trump trump
Sigh... what have you done, you incompetent clown
Was s'posed to cool my summer, now it's burnin' me down

Yawn in the heat, sweat drippin' on the screen
Thermistor dreams shattered, everything's mid, this machine
It's minus twenty in my soul, no coolin' between
This pump ain't coolin' water, it's roastin' me, you dumb fuck

[Instrumental]
[Energy: High]
[Instrument: Brass Stabs, Glitchy Synth Solo, Swing Break]
[Instrumental, 4 bars]

[Verse 2]
[Vocal Style: Rap]
[Energy: Medium]
[Instrument: Dark Synth Pads, 808 Bass, Cyberpunk FX]
I was tryna get that crisp 1440p flow
High refresh rate, cool room, perfect gaming glow
Now it's blastin' desert winds mixed with Israel tunes
Background changed to Benjamin, whole system doomed you

Fat-fingered idiot, probably did it on purpose
Heat pump's a casino now, rollin' 25s, gorgeous
Pumpin' hot regret straight through every vent
Cybernetic nightmare, circuit dreams all spent

[Bridge]
[Mood: Dark, Melancholic]
[Energy: Low]
[Instrument: Sad Synth Brass, Distorted Piano, Digital Glitch]
I just wanted summer coolin', not this chaos, mhm
Now it's a war crime of a system, you dumbfuck
Sad trombones playin' when I try to sleep
Whispers halt dein maul when the temperature creeps

[Energy: Rising]
WideOmE... what have we become, you braindead cunt
Neon lights flicker, my sanity's on the run
Dance hall of disaster, electroswing of pain
This heat pump's a villain drippin' chrome in the rain

[Final Chorus]
[Energy: Maximum]
[Vocal Style: Belt, Aggressive]
Now my heat pump's bricked, full defeat pump legacy
Blowin' hot takes and football VAR conspiracy
Sigh... technician you did me dirty, worthless prick
Was s'posed to save the summer, now it's straight-up hurtin'

Yawn in the heat, balls officially gone
Thermistor turned traitor, singin' the wrong song
Mhm... good night pokiKiss, I'm signin' off
ICANT in this melted room, fuck you krimsonknite

[Outro]
[Energy: Low → Fade]
[Mood: Defeated, Comedic]
Sigh...
Could rename this whole summer to yawn...
Thermistor... why you do me like that, you piece of shit...
Mhm...`,
			clips: [
				{ src: '/audio/defeat-pump-c8fc9224-clip1.mp3', suno: 'https://suno.com/song/c0b2d5fe-39e6-43a9-aee7-1703aa4fa9fa' },
				{ src: '/audio/defeat-pump-c8fc9224-clip2.mp3', suno: 'https://suno.com/song/3d80e337-ce9a-4126-badb-7c021a1fc05d' }
			]
		}
	]}
/>
