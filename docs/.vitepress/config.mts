import { defineConfig } from "vitepress";
import { tabsMarkdownPlugin } from "vitepress-plugin-tabs";

export default defineConfig({
  title: "Suno Music Lab",
  description: "AI-powered music creation with Suno",
  base: "/suno/",

  markdown: {
    config(md) {
      md.use(tabsMarkdownPlugin);
    },
  },

  head: [
    ["meta", { name: "theme-color", content: "#7c3aed" }],
    ["meta", { property: "og:type", content: "website" }],
    ["meta", { property: "og:title", content: "Suno Music Lab" }],
    [
      "meta",
      {
        property: "og:description",
        content: "AI-powered music creation with Suno",
      },
    ],
  ],

  themeConfig: {
    nav: [
      { text: "Home", link: "/" },
      { text: "Songs", link: "/songs/" },
      { text: "Guide", link: "/guide/" },
    ],

    sidebar: {
      "/songs/": [
        {
          text: "Song Catalog",
          items: [
            { text: "All Songs", link: "/songs/" },
            {
              text: "Beyond the Silence of the Stars",
              link: "/songs/beyond-the-silence-of-the-stars",
            },
            {
              text: "Drifting Past the Edge of Light",
              link: "/songs/drifting-past-the-edge-of-light",
            },
            { text: "Dubi Dubi Doo", link: "/songs/dubi-dubi-doo" },
            { text: "Fatman League", link: "/songs/fatman-league" },
            { text: "I Am Semieza", link: "/songs/i-am-semieza" },
            { text: "Pudding Heist", link: "/songs/pudding-heist" },
            {
              text: "Signals in the Static Haze",
              link: "/songs/signals-in-the-static-haze",
            },
            {
              text: "wideNessie Gaming",
              link: "/songs/widenessie-gaming",
            },
            {
              text: "wideNessie Gaming (Psytrance)",
              link: "/songs/widenessie-gaming-psytrance",
            },
          ],
        },
      ],
      "/guide/": [
        {
          text: "Guide",
          items: [
            { text: "Getting Started", link: "/guide/" },
            { text: "Song Format", link: "/guide/song-format" },
            { text: "Style Prompts", link: "/guide/style-prompts" },
            { text: "Meta-Tags Reference", link: "/guide/meta-tags" },
            { text: "Generation Tips", link: "/guide/generation-tips" },
          ],
        },
      ],
    },

    socialLinks: [
      { icon: "github", link: "https://github.com/Niller2005/suno" },
    ],

    footer: {
      message: "Built with VitePress",
    },

    search: {
      provider: "local",
    },
  },
});
