# Mahin

My personal website: [mahinzx.github.io](https://mahinzx.github.io/)

I'm studying Information Technologies at VILNIUS TECH. This site is where I keep my projects, notes and experience in one place.

## About this site

Built with Astro, TypeScript, Tailwind CSS and SolidJS. It includes project pages, notes, a work history, search and an RSS feed.

## Run locally

You'll need Node.js 24, npm and Python 3.

```bash
npm ci
npm run dev
```

To check the production build and local links:

```bash
npm run build
npm run test:static
```

## Update the content

- `src/pages/index.astro` — homepage introduction
- `src/consts.ts` — name, navigation and contact details
- `src/content/projects/` — projects
- `src/content/work/` — experience
- `src/content/blog/` — notes

The GitHub Actions workflow in `.github/workflows/deploy.yml` builds the site and deploys it to GitHub Pages on pushes to `main`.

## Credits

Based on [Astro Sphere](https://github.com/markhorn-dev/astro-sphere) by Mark Horn. Astro Sphere is available under the MIT license; the original license is included in [LICENSE](LICENSE).
