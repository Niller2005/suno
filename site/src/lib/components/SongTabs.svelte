<script lang="ts">
	interface Clip {
		src: string;
		suno?: string;
	}

	interface SongVersion {
		label: string;
		clips: Clip[];
		stylePrompt: string;
		lyrics: string;
		genre?: string;
		bpm?: number;
		mood?: string;
		theme?: string;
		vocals?: string;
		duration?: string;
		keyFeatures?: string;
		source?: string;
	}

	interface GenerationEntry {
		date: string;
		genId: string;
		clips: { suno: string; file: string }[];
	}

	let {
		title,
		versions,
		defaultGenre = '',
		defaultBpm,
		defaultMood = '',
		defaultTheme = '',
		defaultVocals = '',
		defaultDuration = '',
		defaultKeyFeatures = '',
		defaultSource = '',
		generationTips = [] as string[],
		sourceMaterial = '',
		generations = [] as GenerationEntry[]
	}: {
		title: string;
		versions: SongVersion[];
		defaultGenre?: string;
		defaultBpm?: number;
		defaultMood?: string;
		defaultTheme?: string;
		defaultVocals?: string;
		defaultDuration?: string;
		defaultKeyFeatures?: string;
		defaultSource?: string;
		generationTips?: string[];
		sourceMaterial?: string;
		generations?: GenerationEntry[];
	} = $props();

	let activeTab = $state(0);
</script>

<svelte:head>
	<title>{title} — Suno Music Lab</title>
	<meta property="og:title" content="{title} — Suno Music Lab" />
</svelte:head>

<h1>{title}</h1>

<!-- Tab navigation -->
<div class="mb-6 border-b border-gray-200 dark:border-gray-700" role="tablist">
	<div class="-mb-px flex flex-wrap gap-1">
		{#each versions as v, i}
			<button
				role="tab"
				aria-selected={activeTab === i}
				aria-controls="version-tab-{i}"
				class="cursor-pointer rounded-t-lg px-4 py-2.5 text-sm font-medium transition-colors
					{i === activeTab
						? 'border-b-2 border-violet-500 text-violet-700 dark:border-violet-400 dark:text-violet-400'
						: 'text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-200'}"
				onclick={() => (activeTab = i)}
			>
				{v.label}
			</button>
		{/each}
	</div>
</div>

{#each versions as v, i}
	<div id="version-tab-{i}" role="tabpanel" class:hidden={activeTab !== i}>
		{#if activeTab === i}
			<!-- Audio players -->
			{#each v.clips as clip, j}
				<div class="mb-4">
					{#if v.clips.length > 1}
						<p class="mb-1 text-sm font-medium text-gray-600 dark:text-gray-400">Clip {j + 1}</p>
					{/if}
					<audio controls preload="metadata" class="mb-1 w-full">
						<source src={clip.src} type="audio/mpeg" />
						<p>Your browser does not support the audio element.</p>
					</audio>
					{#if clip.suno}
						<p class="text-sm">
							<a
								href={clip.suno}
								target="_blank"
								rel="noopener noreferrer"
								class="text-violet-600 underline decoration-violet-300 decoration-2 underline-offset-2 transition-colors hover:text-violet-800 hover:decoration-violet-600 dark:text-violet-400 dark:decoration-violet-600 dark:hover:text-violet-300"
							>
								View on Suno →
							</a>
						</p>
					{/if}
				</div>
			{/each}

			<hr class="my-6 border-gray-200 dark:border-gray-700" />

			<!-- Details -->
			<h2 class="mb-3 text-lg font-bold text-gray-900 dark:text-gray-100">Details</h2>
			<div class="overflow-x-auto">
				<table class="min-w-full border-collapse">
					<tbody>
						<tr class="border-b border-gray-200 dark:border-gray-700">
							<th class="w-36 py-2 pr-4 text-left text-sm font-semibold text-gray-700 dark:text-gray-300">Genre</th>
							<td class="py-2 text-sm text-gray-900 dark:text-gray-100">{v.genre ?? defaultGenre}</td>
						</tr>
						<tr class="border-b border-gray-200 dark:border-gray-700">
							<th class="w-36 py-2 pr-4 text-left text-sm font-semibold text-gray-700 dark:text-gray-300">BPM</th>
							<td class="py-2 text-sm text-gray-900 dark:text-gray-100">{v.bpm ?? defaultBpm}</td>
						</tr>
						<tr class="border-b border-gray-200 dark:border-gray-700">
							<th class="w-36 py-2 pr-4 text-left text-sm font-semibold text-gray-700 dark:text-gray-300">Mood</th>
							<td class="py-2 text-sm text-gray-900 dark:text-gray-100">{v.mood ?? defaultMood}</td>
						</tr>
						<tr class="border-b border-gray-200 dark:border-gray-700">
							<th class="w-36 py-2 pr-4 text-left text-sm font-semibold text-gray-700 dark:text-gray-300">Theme</th>
							<td class="py-2 text-sm text-gray-900 dark:text-gray-100">{v.theme ?? defaultTheme}</td>
						</tr>
						<tr class="border-b border-gray-200 dark:border-gray-700">
							<th class="w-36 py-2 pr-4 text-left text-sm font-semibold text-gray-700 dark:text-gray-300">Vocals</th>
							<td class="py-2 text-sm text-gray-900 dark:text-gray-100">{v.vocals ?? defaultVocals}</td>
						</tr>
						<tr class="border-b border-gray-200 dark:border-gray-700">
							<th class="w-36 py-2 pr-4 text-left text-sm font-semibold text-gray-700 dark:text-gray-300">Duration</th>
							<td class="py-2 text-sm text-gray-900 dark:text-gray-100">{v.duration ?? defaultDuration}</td>
						</tr>
						<tr class="border-b border-gray-200 dark:border-gray-700">
							<th class="w-36 py-2 pr-4 text-left text-sm font-semibold text-gray-700 dark:text-gray-300">Key features</th>
							<td class="py-2 text-sm text-gray-900 dark:text-gray-100">{v.keyFeatures ?? defaultKeyFeatures}</td>
						</tr>
						{#if v.source ?? defaultSource}
							<tr class="border-b border-gray-200 dark:border-gray-700">
								<th class="w-36 py-2 pr-4 text-left text-sm font-semibold text-gray-700 dark:text-gray-300">Source</th>
								<td class="py-2 text-sm text-gray-900 dark:text-gray-100">{v.source ?? defaultSource}</td>
							</tr>
						{/if}
					</tbody>
				</table>
			</div>

			<hr class="my-6 border-gray-200 dark:border-gray-700" />

			<!-- Style Prompt -->
			<h2 class="mb-3 text-lg font-bold text-gray-900 dark:text-gray-100">Style Prompt</h2>
			<pre class="overflow-x-auto whitespace-pre-wrap rounded-lg bg-gray-100 p-4 text-sm leading-relaxed dark:bg-gray-800 dark:text-gray-200"><code>{v.stylePrompt}</code></pre>

			<hr class="my-6 border-gray-200 dark:border-gray-700" />

			<!-- Lyrics -->
			<h2 class="mb-3 text-lg font-bold text-gray-900 dark:text-gray-100">Lyrics</h2>
			<pre class="overflow-x-auto whitespace-pre-wrap rounded-lg bg-gray-100 p-4 text-sm leading-relaxed dark:bg-gray-800 dark:text-gray-200"><code>{v.lyrics}</code></pre>
		{/if}
	</div>
{/each}

<!-- Source Material -->
{#if sourceMaterial}
	<hr class="my-8 border-gray-200 dark:border-gray-700" />
	<h2 class="mb-4 text-xl font-bold text-gray-900 dark:text-gray-100">Source Material</h2>
	<div class="prose prose-sm max-w-none text-gray-700 dark:prose-invert dark:text-gray-300">
		{@html sourceMaterial}
	</div>
{/if}

<!-- Generation Tips -->
{#if generationTips.length > 0}
	<hr class="my-8 border-gray-200 dark:border-gray-700" />
	<h2 class="mb-4 text-xl font-bold text-gray-900 dark:text-gray-100">Generation Tips</h2>
	<ul class="list-disc space-y-2 pl-5 text-sm text-gray-700 dark:text-gray-300">
		{#each generationTips as tip}
			<li>{@html tip}</li>
		{/each}
	</ul>
{/if}

<!-- Generations Log -->
{#if generations.length > 0}
	<hr class="my-8 border-gray-200 dark:border-gray-700" />
	<h2 class="mb-4 text-xl font-bold text-gray-900 dark:text-gray-100">Generations</h2>
	<div class="space-y-3 text-sm text-gray-700 dark:text-gray-300">
		{#each generations as gen}
			<div>
				<p class="mb-1 font-medium">
					<strong>{gen.date}</strong> (gen <code class="rounded bg-gray-100 px-1 dark:bg-gray-800">{gen.genId}</code>)
				</p>
				<ul class="list-disc space-y-1 pl-5">
					{#each gen.clips as clip}
						<li>
							<a href={clip.suno} target="_blank" rel="noopener noreferrer" class="text-violet-600 underline decoration-violet-300 decoration-2 underline-offset-2 hover:text-violet-800 dark:text-violet-400 dark:decoration-violet-600 dark:hover:text-violet-300">
								Clip {clip.suno ? clip.suno.split('/').pop()?.slice(0, 8) : 'link'}
							</a>
							&mdash; {clip.file}
						</li>
					{/each}
				</ul>
			</div>
		{/each}
	</div>
{/if}

<style>
	.hidden {
		display: none;
	}
</style>
