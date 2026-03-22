# Repository Guidelines

## Project Structure & Module Organization
This repository is a MkDocs documentation site for short development notes. Content lives under `docs/`, organized by topic such as `docs/javascript/`, `docs/react/`, and `docs/dotnet/`. The site entry point is `docs/index.md`, shared tags are in `docs/tags.md`, and custom styling lives in `docs/assets/styles/extra.css`. Site configuration and navigation behavior are defined in `mkdocs.yml`. GitHub Pages deployment is handled by `.github/workflows/gh-pages.yml`.

## Build, Test, and Development Commands
Use the local virtual environment when available.

- `source .venv/bin/activate` activates the project environment.
- `mkdocs serve` runs the docs site locally with live reload.
- `mkdocs build --strict` builds the site and fails on broken links or config issues.
- `python -m pip install mkdocs==1.* mkdocs-material==9.* mkdocs-awesome-pages-plugin==2.*` installs the toolchain used in CI.

## Coding Style & Naming Conventions
Write Markdown that is brief, practical, and easy to scan. Follow the pattern used on the home page: problem, solution, and a small code snippet when useful. Use clear H1/H2 headings, short bullet lists, and fenced code blocks. New note filenames should stay descriptive and date-prefixed when following the existing pattern, for example `2025-09-28_async-await.md`. Keep topic README files as lightweight section overviews.

## Testing Guidelines
There is no separate unit test suite in this repository. The primary validation step is `mkdocs build --strict`; run it before opening a PR. Check new pages locally with `mkdocs serve` to confirm navigation, search, and code formatting render correctly. Treat broken links, missing assets, and malformed Markdown as release blockers.

## Commit & Pull Request Guidelines
Recent history uses short, informal commit subjects such as `nav update` and `Site Updates`. Keep commits small, scoped, and readable; a concise imperative summary is preferred, and date-based note batches are acceptable when grouped intentionally. Pull requests should include a short description, the sections or files changed, and screenshots only when styling or layout changed. Link the related issue when one exists.

## Publishing Notes
Pushes to `master` trigger the GitHub Pages workflow, which builds with strict mode and deploys to `gh-pages`. Avoid merging content that has not been validated locally first.
