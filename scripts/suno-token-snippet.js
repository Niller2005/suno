/**
 * Suno Token Grabber — DevTools Snippet
 * 
 * HOW TO USE:
 * 1. Open Suno in Chrome (https://suno.com)
 * 2. Open DevTools → Sources → Snippets → "New snippet"
 * 3. Paste this entire file and save as "get-suno-token"
 * 4. Press Cmd+Enter (or Ctrl+Enter) to run it
 * 5. Click anything on Suno (e.g. "Create", or refresh the page)
 * 6. The token is now in your clipboard — run `scripts/set-suno-token` in terminal
 *
 * ALTERNATIVE — Bookmarklet:
 * Create a bookmark with this URL (all on one line):
 * javascript:(()=>{const o=window.fetch;window.fetch=async(...a)=>{const r=await o(...a),h=a[1]?.headers?.Authorization||a[1]?.headers?.authorization;if(h&&h.includes('Bearer')){await navigator.clipboard.writeText(h.replace('Bearer ',''));console.log('%cToken copied!','color:green;font-size:14px');window.fetch=o}return r};console.log('Click something on Suno to capture token...')})()
 */

(function() {
  const originalFetch = window.fetch;

  window.fetch = async function(...args) {
    const response = await originalFetch.apply(this, args);

    // Check request headers for Authorization
    const reqHeaders = args[1]?.headers || {};
    const auth = reqHeaders.Authorization || reqHeaders.authorization;

    if (auth && auth.includes('Bearer')) {
      const token = auth.replace('Bearer ', '').trim();
      await navigator.clipboard.writeText(token);
      console.log('%cSuno token copied to clipboard!', 'color: #00ff00; font-size: 14px; font-weight: bold;');
      console.log('Run in terminal: scripts/set-suno-token');
      // Restore original fetch so we don't keep copying
      window.fetch = originalFetch;
    }

    return response;
  };

  console.log('%cToken interceptor active.', 'color: orange;');
  console.log('Click anything on Suno to trigger an API call and copy the token.');
})();
