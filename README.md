# Video Notes

A static developer study library for GitHub Pages. The root catalog groups six
video summaries into five topic collections. Every guide shares the same dark
theme, chapter navigation, readable code blocks, and screenshot viewer.

## Preview

No package installation is required. Use Python 3:

```sh
python3 scripts/build_site.py
python3 -m http.server 8000 --directory dist
```

Open `http://localhost:8000`. You can also serve the repository root during editing.
The `dist/` preview matches what the deployment publishes.

## Deploy to GitHub Pages

Push this project to a GitHub repository with a `main` branch. In the repository's
**Settings → Pages → Build and deployment**, select **GitHub Actions** as the source.
The included workflow deploys on pushes to `main`.

## Add or edit a guide

1. Name the video folder with ASCII letters, digits, and `_` instead of spaces or
   punctuation. Keep working inputs under `<video-folder>/.work/`.
2. Put the guide in its video folder, and selected public images in `assets/`.
3. Reuse `../assets/site.css`, `../assets/site.js`, and the shared guide layout.
4. Add the title, category, speaker, source, and exact page path to `videos.json`.
5. Regenerate the catalog with `python3 scripts/render_catalog.py`, then package
   it with `python3 scripts/build_site.py`.

The catalog is ordinary HTML: its topic links and guide links work without
JavaScript. Search, reading progress, image enlargement, code copying, and quiz
disclosures are optional enhancements. Full study content stays available when
JavaScript is disabled.

Read [AGENTS.md](AGENTS.md) for the complete project conventions.
