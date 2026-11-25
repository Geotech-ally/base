# Contributing

## Development requirements

- Git
- Python 3.10 or newer
- Node.js 20 or newer
- A modern browser

No build tool is required for the static site. Node.js is used only for browser tests.

## Local setup

```bash
git clone https://github.com/Geotech-ally/base.git
cd base
python3 -m http.server 8000
```

Open `http://localhost:8000`.

## Branch naming

- `feature/<short-description>`
- `fix/<short-description>`
- `docs/<short-description>`
- `test/<short-description>`

Keep changes focused and base them on current `main`.

## Commit conventions

Use concise imperative subject lines:

```text
Add portfolio keyboard navigation
Fix mobile navigation focus state
Document GitHub Pages deployment
```

For larger changes, add a short body describing motivation and behavior.

## Pull requests

1. Update or add tests for behavior changes.
2. Run `python3 -m unittest discover -s tests -v`.
3. Verify the site at phone and desktop widths.
4. Check keyboard navigation and reduced-motion behavior.
5. Update documentation and placeholders when relevant.
6. Complete the pull request template.

Do not commit `.env` files or credentials. The static site requires no environment variables.

## Testing requirements

Run `npm run test:all` before merging. This executes the Python static suite and Playwright/axe-core browser checks. Browser behavior should also be checked manually for navigation, filtering, dialogs, the carousel and form validation.

## Formatting

- Use two-space indentation in HTML, CSS and JavaScript.
- Preserve existing names and file organization.
- Keep JavaScript strict-mode and avoid global variables.
- Prefer semantic HTML and existing CSS variables.

## Bug reports

Use the bug report issue form and include exact reproduction steps, expected behavior, observed behavior and browser details.
