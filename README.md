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


## Full team bibliography and author portraits

The initial publication section includes a **non-exhaustive seed dataset** of papers provided by the lab, with linked LICAD authors. The site supports unlimited publications and recognizes member names through `authorAliases` in `src/content/people/*.md`.

To import *all* papers from the PI and every current/former LICAD member, export their complete citations to a single BibTeX (`.bib`) or CSV (`.csv`) file (one publication per record; deduplicate shared papers). Run:

```bash
python3 scripts/import_publications.py path/to/licad-all-publications.csv
# OR for BibTeX:
python3 -m pip install bibtexparser
python3 scripts/import_publications.py path/to/licad-all-publications.bib
```

CSV columns: `title,authors,year,venue,doi,url,type,area`. The script skips records whose title+year slug already exists. Inspect imported records and correct dates, DOI links, and authors before pushing them. Add author name spellings to `authorAliases` so the website recognizes team coauthors automatically.

**Pictures:** Add an approved JPG/WEBP portrait under `public/images/team/`, e.g. `ardak-kashkynbayev.jpg`; then set `photo: "/images/team/ardak-kashkynbayev.jpg"` in the member's Markdown file. Until portraits are available, the publication cards display circular initials rather than unrelated photos.

**Note:** Citation counts and open-access indicators are intentionally not autogenerated without a trustworthy live source. Use the original publisher DOI metadata or exported reference data.


## Imported bibliography (101 records)

The supplied BibTeX bibliography is saved as `bibliography/licad-supplied.bib` and its 101 records were converted into `src/content/publications/*.md`. This represents every entry in the uploaded source, **not** necessarily all publications by all LICAD members. Check metadata and author identity; add portraits in `public/images/team/` and set the matching `photo` field in each person profile.


## Complete LICAD deployment package (November 2026)

This version includes 101 user-supplied BibTeX records; Cohen-style publication filters and coauthor portraits; nine supplied team photographs (AI-enhanced for six portraits); one placeholder for Aiym Kuralova; the public research, projects, collaborators, news, people, and contact pages; and GitHub Actions deployment. Bibliographic metadata has not been independently verified. Confirm consent for publication of member images before making the repository public.

### Replace an existing GitHub repository

The ZIP **contains files at the repository root**. After extracting, upload the contents (not the enclosing folder and not the ZIP itself). GitHub's browser upload does not delete old files or reliably include hidden folders; GitHub Desktop or Git CLI is recommended when replacing everything. Make sure `.github/workflows/deploy.yml` exists once, and set **Settings → Pages → Source: GitHub Actions**.

```bash
npm install
npm run build
```

GitHub Pages URL: https://LICAD-NU.github.io/

## Funded projects (updated November 2026)

Includes eight project records supplied by the user: two active and six finished, with project dates, participants, project categories and topic keywords. Project content lives in `src/content/projects/`; update a Markdown record to revise a project. The three illustrative research themes remain separate from the funded projects.


## GitHub Actions install fix (November 2026)

This project pins `mdast-util-gfm-table` to `2.0.0` through npm `overrides`.
A GitHub Actions install previously failed while requesting a non-existent `2.0.1` tarball.
The deployment workflow uses `npm install --no-package-lock --no-audit --no-fund`
to avoid any stale lockfile previously committed during manual uploads.

To update the existing organization repository using GitHub Desktop:

1. Clone `LICAD-NU/LICAD-NU.github.io` if you have not already.
2. In Finder, open the cloned repository with **Repository → Show in Finder**.
3. Remove stale project files in that cloned folder, but **never delete its hidden `.git` directory**.
4. Copy the **contents** of this ZIP into the cloned repository root. Do not add an outer folder.
5. Delete any accidental duplicated `.github/workflows/.github/...` directory.
6. Commit in GitHub Desktop and click **Push origin**.
7. Under GitHub Settings → Pages, select **GitHub Actions**, then inspect the latest Actions run.

Note: This ZIP was statically validated (content front matter, file paths and folder structure),
but npm package installation and an end-to-end Astro build could not be completed in the
artifact environment because registry network access was unavailable. A successful live
Actions run remains the final confirmation.
