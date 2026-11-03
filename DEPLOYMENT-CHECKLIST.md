# LICAD Website — Deployment Checklist

- Repository: `https://github.com/LICAD-NU/LICAD-NU.github.io`
- URL: `https://LICAD-NU.github.io/`
- Workflow: `.github/workflows/deploy.yml`
- Pages: **Settings → Pages → Source: GitHub Actions**
- GitHub Desktop: **Commit to main**, then **Push origin**
- Keep your hidden `.git` folder when replacing files locally.
- The static build output is `dist/`, generated automatically by Astro. Never upload `dist/` manually.

## If deployment fails

1. Open the latest GitHub **Actions** run.
2. Open **build** and expand the first step with a red X.
3. Copy the complete error message.
4. Check `package.json` contains the override `"mdast-util-gfm-table": "2.0.0"`.
5. Check there is only one workflow: `.github/workflows/deploy.yml`.

The earlier `npm E404` error originated in the dependency tree, not the LICAD content.
