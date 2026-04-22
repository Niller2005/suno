/**
 * Suno Cookie Grabber — DevTools Snippet
 *
 * HOW TO USE (Method 1 — intercept next API call):
 * 1. Open Suno in Chrome (https://suno.com)
 * 2. Open DevTools → Sources → Snippets → "New snippet"
 * 3. Paste this code and save as "get-suno-cookies"
 * 4. Press Cmd+Enter (or Ctrl+Enter) to run it
 * 5. Click anything on Suno (e.g. "Create") to trigger an API call
 * 6. Cookies are auto-copied from that request
 * 7. Run in terminal: scripts/set-suno-cookies
 *
 * ALTERNATIVE (Method 2 — copy from Network panel):
 * 1. DevTools → Network → click any request to studio-api.prod.suno.com
 * 2. Scroll to Request Headers → right-click "cookie" → Copy value
 * 3. Run: scripts/set-suno-cookies 'paste-here'
 *
 * This grabs all cookies so you can use auto-refresh auth (SUNO_COOKIE)
 * instead of manual hourly tokens.
 */

(function() {
  const originalFetch = window.fetch;

  window.fetch = async function(...args) {
    const response = await originalFetch.apply(this, args);

    const reqHeaders = args[1]?.headers || {};
    const cookie = reqHeaders.Cookie || reqHeaders.cookie;

    if (cookie) {
      await navigator.clipboard.writeText(cookie);
      console.log('%cCookies copied to clipboard!', 'color: #00ff00; font-size: 14px; font-weight: bold;');
      console.log('Run in terminal: scripts/set-suno-cookies');
      window.fetch = originalFetch;
    }

    return response;
  };

  console.log('%cCookie interceptor active.', 'color: orange;');
  console.log('Click anything on Suno to trigger an API call and copy cookies.');
})();
