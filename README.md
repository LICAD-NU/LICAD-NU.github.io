# LICAD · Academic Research Lab Website

A responsive, multi-page **Astro + TypeScript + CSS + KaTeX** research laboratory site for the **Laboratory for Intelligent Control & Applied Dynamics (LICAD)** at **Nazarbayev University**. Design is independently implemented, inspired by modern academic group websites; no third-party site assets or source code were copied.

## Included
- Home, research, people, alumni, **collaborators**, publications, project/theme pages, news, and contact.
- **10 individual profiles:** 6 current members and 4 alumni, as provided.
- Editable Markdown content collections with typed schemas.
- Publication list with client-side search and year/type filters, DOI links and copyable BibTeX on detail pages.
- KaTeX rendering in Markdown using `remark-math` and `rehype-katex`, plus on-page example equations.
- Responsive CSS, mobile navigation, abstract SVG illustration, placeholder initials instead of invented portraits.
- GitHub Actions deployment workflow for GitHub Pages.

## Requirements
Node.js 20.3+ (Node 22 recommended) and npm.

## Run locally
```bash
npm install
npm run dev
```
Visit `http://localhost:4321`.

## Build
```bash
npm run build
npm run preview
npm run check
```

## Publish: recommended GitHub organization website
1. Create a **GitHub organization** (e.g. `licad-nu`, only if available).
2. Create a public repository **`YOUR_ORG.github.io`** inside that organization.
3. Edit `astro.config.mjs`: replace `YOUR_ORG` with the actual organization account. Leave `base: '/'`.
4. Edit `src/config/site.ts`: set the official lab contact email and GitHub organization URL when ready.
5. Push everything to the `main` branch. The included workflow runs `npm install` and does not require a lockfile. After running `npm install` locally, commit the generated `package-lock.json` for reproducible builds and optionally switch the workflow to `npm ci`.
6. In repository **Settings → Pages**, set **Source: GitHub Actions**.
7. GitHub Actions builds and publishes the website at `https://YOUR_ORG.github.io`.

For a **project repository** instead of an organization site, set `site: 'https://YOUR_ORG.github.io'` and `base: '/REPOSITORY_NAME/'` in `astro.config.mjs`. The site uses `import.meta.env.BASE_URL` for internal links and assets.

## Editing the team
Each person's Markdown file is under `src/content/people/`. `photo` is optional; if absent, the site shows initials. Add an image to `public/images/team/` and set e.g. `photo: "images/team/ardak.jpg"`. Use `status: current` or `former` and the corresponding group (`pi`, `postdoc`, `phd`, `research`, or `alumni`). Please confirm consent and preferred biographies before publishing members' details or photographs.

## Editing collaborators
The `/collaborators/` page reads the typed Markdown collection in `src/content/collaborators/`. Copy `_TEMPLATE.md.example` to `<name>.md`, then add confirmed name, institution, academic links, joint projects, research fields, and optional approved portrait. The directory starts empty intentionally: no collaborators have been invented or publicly attributed without your confirmation.

## Editing publications
Copy `src/content/publications/_TEMPLATE.md.example` to `src/content/publications/my-paper.md`, replace all example data and set `draft: false`. **No publications are inserted by default**, because no verified complete bibliography was supplied. Publication cards appear automatically, filterable by author, title, year, and type. Provide `bibtex: |` to enable the copy button. For LaTeX in Markdown use `$...$` or `$$...$$`.

## Projects and news
`src/content/projects/` contains three **illustrative themes**, not assertions of specific grants or completed projects. Update projects with real details as confirmed. Copy `src/content/news/_TEMPLATE.md.example` to `.md` and fill out a verified event when available.

## Before publishing
- [ ] Confirm the public lab name, school affiliation, and permission to publish members' names and university emails.
- [ ] Confirm member positions and alumni affiliations, especially the personal preferred name 'Al-Farabi'.
- [ ] Replace initials with approved portraits, if desired.
- [ ] Set the real GitHub organization and official lab email.
- [ ] Add approved collaborator profiles, institutions, and links.
- [ ] Add verified papers, authors, DOIs, BibTeX, and real project details.
- [ ] Optionally add analytics and a custom domain.

## Repository license
Code is available under the MIT license. Research content, names, portraits, and institutional branding are not automatically covered by that license. This starter uses an original typographic LICAD mark, not an official university logo.

## Build verification
The source project was assembled without installing npm packages in the generation environment. Run `npm install && npm run check && npm run build` on a machine with npm registry access before deployment.
