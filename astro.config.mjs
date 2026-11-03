import { defineConfig } from 'astro/config';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

// For an organization repository named YOUR_ORG.github.io, keep base: '/'.
// For a project repository named YOUR_REPO, set base: '/YOUR_REPO/'.
export default defineConfig({
  site: 'https://YOUR_ORG.github.io',
  base: '/',
  markdown: { remarkPlugins: [remarkMath], rehypePlugins: [rehypeKatex] },
});
