# Nuru Tech: Business Services Website

A responsive, multi-section website for a fictional IT and software development agency in Kenya. It is built with only **HTML5, CSS3 and vanilla JavaScript**, with no frameworks, no libraries and no build step.

> All company details, prices, projects, statistics and testimonials are **sample content** written for this assignment. The email, phone number and location in the Contact section are clearly labelled placeholders.

---

## 1. Project introduction

Nuru Tech ("nuru" means "light" in Swahili) is an imaginary agency that sells six services: website development, web application development, UI/UX design, database design, website maintenance and technical support. The website lets a potential client learn about the company, compare prices, browse past work, read testimonials and send an enquiry.

## 2. Problem statement

Small businesses, clinics, schools and community groups often struggle to find a trustworthy technology partner. They need to understand what is offered, what it costs and whether the agency has done similar work, without having to phone or visit first. A clear, fast and accessible website answers those questions and turns visitors into enquiries.

## 3. Project objectives

- Build a complete, professional website using HTML5, CSS3 and vanilla JavaScript only.
- Practise semantic, accessible, HTML-first markup.
- Style a consistent design system with CSS variables, Flexbox and Grid.
- Make the site fully responsive using a mobile-first approach.
- Add useful interactivity with clean, commented JavaScript.
- Keep the code organised in separate HTML, CSS and JavaScript files.

## 4. Technologies used

| Technology | Used for |
|---|---|
| HTML5 | Page structure, semantic elements, forms, the native `<dialog>` element, an SVG icon sprite |
| CSS3 | Layout (Flexbox and Grid), variables, responsive design, transitions, keyframe animations |
| Vanilla JavaScript (ES6) | Menu, scrolling, filtering, slider, form validation, reveal animations |
| Google Fonts (optional) | Bricolage Grotesque and DM Sans. If they fail to load, system fonts are used |
| SVG | Logo, project images, avatars and icons (all local files, so nothing breaks offline) |

## 5. Project folder structure

```
business-services-website/
├── index.html              Page structure and all content
├── css/
│   └── style.css           All styling, organised in 14 numbered sections
├── js/
│   └── script.js           All behaviour, one init function per feature
├── assets/
│   ├── images/             Six project images and three client avatars (SVG)
│   └── icons/              logo.svg and favicon.svg
└── README.md               This document
```

## 6. Main website features

- Sticky navigation bar with logo, six links, a quote button and a mobile menu
- Hero section with two calls to action and a product preview built only from HTML and CSS
- About section with mission, vision, values and counting statistics
- Six service cards, each with an icon, description, three benefits and a button
- Three pricing packages in KES, with the Professional package visually emphasised
- Portfolio of six projects with category filters and a details dialog
- Testimonial slider with three sample clients
- Contact form with validation, plus placeholder business details and social links
- Footer with quick links, service links, social links, dynamic year and back-to-top buttons

## 7. How HTML is used

- **Semantic landmarks:** `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>`, `<figure>` and `<blockquote>` describe what each part of the page is.
- **Heading outline:** one `<h1>`, one `<h2>` per section and `<h3>` for cards, so screen readers can navigate by heading.
- **HTML-first content:** all text, cards, pricing and project details are written in the HTML. JavaScript only adds behaviour. For example, each project's extra details are in a hidden `<div>` inside its card, and the dialog simply copies them.
- **Forms:** every input has a real `<label>`, correct `type` and `autocomplete` values, and an error message element linked with `aria-describedby`.
- **Native `<dialog>`:** the project details window uses the built-in dialog element, which handles focus trapping and the Escape key.
- **Accessibility:** skip link, `alt` text on meaningful images, empty `alt` on decorative ones, `aria-expanded` on the menu button, `aria-pressed` on filters, and `aria-live` regions for status messages.
- **SVG sprite:** icons are defined once as `<symbol>` elements and reused with `<use>`, which avoids repeating the same code.

## 8. How CSS is used

- **CSS variables** in `:root` hold colours, fonts, spacing, radii and shadows, so the whole theme can be changed in one place.
- **Mobile-first:** base styles are for phones. `min-width` media queries at 640px, 700px, 900px, 960px and 1060px add columns and larger layouts.
- **Flexbox** for the navigation, buttons, card internals and footer row. **Grid** for card grids, the about layout, pricing, portfolio and contact layout.
- **Sticky header** with `position: sticky`, plus a shadow added by JavaScript on scroll.
- **Design direction:** dark navy and white as the main colours, with blue and cyan accents, rounded cards and soft shadows.
- **Visual hierarchy:** the Professional package uses a dark card, a cyan border and a badge so it stands out.
- **Motion:** transitions on hover and focus, one load animation (the hero chart grows), and a short scroll reveal. All of it is switched off by `prefers-reduced-motion`.
- **Focus styles:** `:focus-visible` outlines work on both light and dark sections.

## 9. How JavaScript is used

All code is in `js/script.js`, wrapped in one function so nothing leaks into the global scope. Each feature has its own function.

| # | Feature | Idea behind it |
|---|---|---|
| 1 | Mobile menu | Toggles a class and `aria-expanded`; Escape closes it |
| 2 | Smooth scrolling | One click listener on the document; uses `scrollIntoView` and moves focus to the section |
| 3 | Sticky header | A scroll listener (throttled with `requestAnimationFrame`) adds a class |
| 4 | Active link | `IntersectionObserver` marks the section currently on screen |
| 5 | Portfolio filter | Compares `data-category` with the chosen `data-filter` and toggles `hidden` |
| 6 | Project dialog | Copies the card's hidden details into a `<dialog>` and opens it with `showModal()` |
| 7 | Testimonial slider | Moves a flex track with `translateX`; buttons, dots, arrow keys, swipe, auto-play with a pause button |
| 8 | Form validation | One rule per field, error messages, focus on the first error, simulated submission |
| 9 | Copyright year | `new Date().getFullYear()` |
| 10 | Scroll reveal and counters | `IntersectionObserver` adds a class; statistics count up once |
| 11 | Interactive buttons | "Request this service" and "Choose ..." buttons preselect the service and prefill the message |
| 12 | Image fallback | If an image fails to load, a neutral placeholder is shown |

**About the contact form:** there is **no backend**. The form validates input in the browser and then shows a success message after a short simulated delay. Nothing is sent or stored, and the page says so. To make it real, send the form data to a server endpoint or a form service inside the `submit` handler in `script.js`.

## 10. How to run the project locally

**Option A: open the file**
1. Unzip the project folder.
2. Double-click `index.html`. It opens in your default browser.

**Option B: local server (recommended for testing)**
1. Open a terminal in the project folder.
2. Run one of these:
   - Python: `python -m http.server 8000`
   - Node.js: `npx serve`
   - VS Code: install the **Live Server** extension, right-click `index.html`, choose **Open with Live Server**
3. Visit `http://localhost:8000` (or the address the tool prints).

No installation, build tool or internet connection is required. The only online resource is the optional Google Fonts stylesheet.

## 11. Challenges encountered and possible solutions

| Challenge | Solution used |
|---|---|
| Reliable images without depending on the internet | Created local SVG images and avatars, and added a JavaScript fallback for failed images |
| Sticky header covering section titles after a click | `scroll-padding-top` and `scroll-margin-top` in CSS, plus focus moved to the target section |
| Making the mobile menu usable without a mouse | Button with `aria-expanded`, Escape to close, menu closes after choosing a link |
| Scroll animations hiding content when JavaScript is off | The hidden starting state only applies when the `js` class is present on `<html>` |
| Animations bothering motion-sensitive users | `prefers-reduced-motion` disables animation and stops slider auto-play |
| Auto-moving slider being hard to read | Pauses on hover and focus, has a visible pause button, and hidden slides are `inert` |
| Validating Kenyan phone numbers | A regular expression accepting `07xx`, `01xx`, `+254` and general international formats |
| No server to receive form data | Clear demonstration message, and a note on where a real backend would connect |

**Possible improvements:** connect the form to a real backend, add a language switch (English and Swahili), add a dark-mode toggle, replace the sample SVG images with real project screenshots, and add automated tests.

## 12. Conclusion

This project shows how far plain HTML, CSS and JavaScript can go. Semantic HTML provides structure and accessibility, CSS provides a consistent and responsive design, and JavaScript adds focused interactivity without any framework. The result is a fast, maintainable website that works without a build step.

---

# Demonstration guide for your lecturer

Suggested running order: about 8 to 10 minutes. Use the browser's developer tools (press **F12**) for the responsive and structure steps.

| Step | What to do | What to say |
|---|---|---|
| 1. Structure | Open `index.html` in the editor beside the browser. Scroll through the tags. | "The page is HTML-first: semantic landmarks, one `h1`, labelled forms, and content written directly in the markup." |
| 2. Folder structure | Show the project tree. | "HTML, CSS and JavaScript are separated, and images and icons are local assets." |
| 3. Navigation | Click each nav link. | "Smooth scrolling moves to each section, and the current section is highlighted as you scroll." |
| 4. Sticky header | Scroll down slowly. | "The header sticks to the top and gains a shadow. JavaScript only toggles a class." |
| 5. Mobile menu | Press **Ctrl+Shift+M** (device toolbar) and choose a phone size. Open and close the menu, then press Escape. | "The menu button updates `aria-expanded`, so assistive technology knows its state." |
| 6. Responsive design | Drag the viewport from phone to tablet to desktop width. | "The layout is mobile-first. Grid columns increase at media query breakpoints." |
| 7. Hero | Reload the page and watch the hero chart. | "This is the single load animation. It is built from HTML and CSS only." |
| 8. Statistics and reveal | Scroll to About. | "Sections fade in with `IntersectionObserver`, and the statistics count up once." |
| 9. Service buttons | Click **Request this service** on a card. | "The button scrolls to the form and preselects the service and a starter message." |
| 10. Pricing | Point out the Professional card, then click **Choose Professional**. | "The featured card uses a dark background, a cyan border and a badge. The button prefills the form." |
| 11. Portfolio filter | Click each filter, then open **View details** on a project. Press Escape. | "Filtering compares data attributes. The details come from hidden HTML and open in a native dialog." |
| 12. Slider | Use the arrows, dots, keyboard arrows and the pause button. | "It auto-plays, pauses on hover or focus, and respects reduced-motion settings." |
| 13. Form validation | Click **Send message** with the form empty. Then enter a bad email and phone number. Finally fill in valid data. | "Each field has its own rule. Errors are linked to inputs with `aria-describedby`. The form is a demonstration, so no data is sent." |
| 14. Footer | Show the year, then click **Back to top**. | "The year comes from `new Date()`, so it never needs editing." |
| 15. Reduced motion (optional) | In DevTools, open the Rendering panel and set **Emulate CSS prefers-reduced-motion: reduce**. Reload. | "Animations and auto-play are turned off for users who ask for less motion." |

## Concepts demonstrated

**HTML:** semantic elements, heading hierarchy, forms and labels, `<dialog>`, `data-*` attributes, HTML-first content, accessible names, SVG sprites.

**CSS:** custom properties, mobile-first media queries, Flexbox, Grid, `position: sticky`, pseudo-classes (`:hover`, `:focus-visible`, `:empty`), attribute selectors (`[aria-pressed="true"]`), transitions, keyframes, `prefers-reduced-motion`.

**JavaScript:** DOM selection and events, event delegation, `classList`, `dataset`, `IntersectionObserver`, `requestAnimationFrame`, regular expressions, `setTimeout`, `matchMedia`, the `<dialog>` API, and ARIA attributes updated from code.

## Likely lecturer questions

- **Why no framework?** The brief asks for HTML, CSS and vanilla JavaScript to show understanding of the web platform itself.
- **Is the form real?** No. It validates in the browser only. A backend would be needed to receive messages.
- **How is the site accessible?** Skip link, landmarks, labels, visible focus, keyboard support for every control, reduced-motion support and sufficient colour contrast.
- **How would you deploy it?** Upload the folder to any static host such as GitHub Pages, Netlify or Cloudflare Pages.
- **Where would you change the brand colours?** In the `:root` block at the top of `css/style.css`.

## Customising before submission

1. Replace the placeholder email, phone number and location in the Contact section of `index.html`.
2. Replace the social links with real profile addresses.
3. Change the company name in the header, footer, page title and logo if you prefer another name.
4. Swap the SVG project images for real screenshots (keep the same file names or update the `src` attributes).
