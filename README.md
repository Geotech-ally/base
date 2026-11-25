# Nuru Tech

![CI](https://github.com/Geotech-ally/base/actions/workflows/ci.yml/badge.svg)
![Deploy](https://github.com/Geotech-ally/base/actions/workflows/pages.yml/badge.svg)

Nuru Tech is a responsive business-services website for a fictional Kenyan technology agency. It presents agency services, pricing, projects, testimonials and a validated demonstration enquiry form.

The project uses only HTML5, CSS3 and vanilla JavaScript. It has no framework, package dependency, build step or backend.

**Recommended homepage:** <https://geotech-ally.github.io/base/>
**Repository topics:** `html`, `css`, `javascript`, `static-website`, `responsive-design`, `portfolio`, `kenya`, `business-website`, `accessibility`, `github-pages`

> Company contact details are set to `hello@nurutech.ac.ke`, `0768998191` and Bondo, Kenya. Projects and testimonials remain explicitly illustrative until verified source material is supplied. The GitHub profile is the only verified repository social link.

## Key features

- Responsive mobile-first layout
- Accessible navigation, forms, dialog and carousel
- Portfolio category filtering
- Kenyan and international phone validation
- Reduced-motion support and visible keyboard focus
- SEO metadata, local SVG assets and image fallbacks
- Demonstration contact form (no data is sent or stored)

## Technologies

| Technology | Purpose |
|---|---|
| HTML5 | Semantic page structure and native dialog |
| CSS3 | Design tokens, Flexbox, Grid and responsive layouts |
| JavaScript | Navigation, filtering, dialog, carousel and form validation |
| SVG | Logo, favicon, portfolio illustrations and avatars |
| GitHub Actions | CI validation and GitHub Pages deployment |

## Project structure

```text
.
├── index.html
├── css/style.css
├── js/script.js
├── assets/
│   ├── icons/
│   └── images/
├── tests/test_site.py
├── .github/
│   ├── workflows/
│   ├── ISSUE_TEMPLATE/
│   └── dependabot.yml
├── ROADMAP.md
└── CONTRIBUTING.md
```

## Local development

Requirements:

- Python 3.10 or newer
- Node.js 20 or newer
- A modern browser

No build step is required for the static site.

```bash
python3 -m http.server 8000
npm ci
npx playwright install chromium
```

Open <http://localhost:8000>. The root `index.html` can also be opened directly, although a local server is recommended.

## Testing

```bash
python3 -m unittest discover -s tests -v
npm run test:e2e
```

The static suite validates HTML structure, IDs and labels, local asset references, section and heading integrity, metadata and sitemap configuration. Playwright verifies navigation, portfolio filtering and form validation in Chromium; axe-core checks serious accessibility violations.

## Form submission

The form remains in demonstration mode until `data-form-endpoint` is set on `#contact-form`.

```html
<form id="contact-form" data-form-endpoint="https://api.example.com/contact">
```

The endpoint must accept an HTTPS `POST` containing JSON and return a successful `2xx` response. The JSON fields are `name`, `email`, `phone`, `service` and `message`. Configure CORS on the endpoint for the GitHub Pages origin. Do not put secrets or credentials in this static repository.

## Deployment

The workflow publishes the repository root to GitHub Pages using GitHub Actions.

1. In GitHub, open **Settings > Pages**.
2. Set **Source** to **GitHub Actions**.
3. Push to `main`; the Pages workflow deploys the site.
4. Confirm the deployment at <https://geotech-ally.github.io/base/>.

Do not use a separate `dist` or `build` directory: this project serves static files from the repository root.

## Browser compatibility

The page targets current versions of Chrome, Edge, Firefox and Safari. The native dialog API and modern CSS features require an up-to-date browser.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for setup, branch and commit conventions, testing requirements and pull request procedures.

## License

This project is licensed under the Apache License 2.0. See [LICENSE](LICENSE). Apache-2.0 permits use, modification and redistribution subject to its notice and patent provisions.

## Contact

No verified maintainer address is available in the repository. Replace the placeholder contact details in `index.html` before public production use.
