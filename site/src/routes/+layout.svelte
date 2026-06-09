<script lang="ts">
	import './layout.css';
	import favicon from '$lib/assets/favicon.svg';

	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
	<meta name="theme-color" content="#7c3aed" />
	<meta property="og:type" content="website" />
	<meta property="og:title" content="Suno Music Lab" />
	<meta property="og:description" content="AI-powered music creation with Suno" />
</svelte:head>

<div class="flex min-h-screen flex-col">
	<!-- Navigation -->
	<nav class="border-b border-gray-200 bg-white dark:border-gray-700 dark:bg-gray-900">
		<div class="mx-auto flex max-w-5xl items-center justify-between px-4 py-3">
			<a href="/" class="text-lg font-bold text-violet-700 dark:text-violet-400">
				Suno Music Lab
			</a>
			<div class="flex items-center gap-6 text-sm font-medium">
				<a
					href="/"
					class="text-gray-600 transition-colors hover:text-violet-700 dark:text-gray-400 dark:hover:text-violet-400"
				>
					Home
				</a>
				<a
					href="/songs"
					class="text-gray-600 transition-colors hover:text-violet-700 dark:text-gray-400 dark:hover:text-violet-400"
				>
					Songs
				</a>
				<a
					href="/guide"
					class="text-gray-600 transition-colors hover:text-violet-700 dark:text-gray-400 dark:hover:text-violet-400"
				>
					Guide
				</a>
<a
	href="https://github.com/Niller2005/suno"
	target="_blank"
	rel="noopener noreferrer"
	aria-label="GitHub repository"
	class="text-gray-500 transition-colors hover:text-gray-700 dark:text-gray-500 dark:hover:text-gray-300"
>
	<svg class="h-5 w-5" viewBox="0 0 24 24" fill="currentColor">
						<path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0 0 24 12c0-6.63-5.37-12-12-12z"/>
					</svg>
				</a>
			</div>
		</div>
	</nav>

	<!-- Main content -->
	<main class="mx-auto w-full max-w-5xl flex-1 px-4 py-8">
		<div class="prose prose-gray max-w-none dark:prose-invert lg:prose-lg">
			{@render children()}
		</div>
	</main>

	<!-- Footer -->
	<footer class="border-t border-gray-200 bg-white py-6 text-center text-sm text-gray-500 dark:border-gray-700 dark:bg-gray-900 dark:text-gray-400">
		Built with SvelteKit
	</footer>
</div>
