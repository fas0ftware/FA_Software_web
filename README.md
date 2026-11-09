# FA Software — Website

Single-page portfolio site for **FA Software**: software services for automation, data, bots, networking and security tools, and web.

Plain HTML, CSS and JavaScript. No frameworks, no build step.

## Features

- Strictly black and white design, mobile-first and responsive
- Light and dark mode: follows the system preference, has a toggle, and remembers the choice in `localStorage`
- Logo switches with the theme
- Projects shown as horizontally swipeable cards (CSS scroll-snap)
- Semantic HTML, alt texts, skip link and keyboard-friendly focus styles
- Respects `prefers-reduced-motion`; the theme toggle is hidden when JavaScript is off
- Tab icon follows the system theme (black logo on light tabs, white logo on dark tabs)
- Basic link-preview tags (Open Graph and Twitter card)

## Structure

```
index.html          Page content (hero, about, services, projects, contact)
css/style.css       All styles and theme tokens
js/main.js          Theme toggle
assets/
  logo-dark.png     Black logo, used on light backgrounds
  logo-light.png    White logo, used on dark backgrounds
tools/
  check_site.py     Sanity checks (broken links, missing files, alt texts, placeholders)
.github/workflows/
  check.yml         Runs the checks on every push
```

## Run locally

Open `index.html` in a browser, or serve the folder:

```bash
python3 -m http.server 8000
```

Then visit http://localhost:8000.

## Editing

- **Projects:** each card is an `<li class="project">` in `index.html`. Add `project--soon` to the class for the "Coming soon" style.
- **Theme colors:** CSS variables at the top of `css/style.css`.

## Checks

```bash
python3 tools/check_site.py            # errors fail, leftover placeholders only warn
python3 tools/check_site.py --strict   # run this before publishing
```

The checks cover missing local files, `#anchors` without a matching id, images without `alt`, links that open a new tab without `rel="noopener"`, duplicate ids and leftover `[PLACEHOLDER]` text.

## Before you publish

- [ ] Replace `[YOUR NAME]` in the About section (the strict check fails until you do).
- [ ] Check the project cards: a card is "Coming soon" only while its repository is private or does not exist yet. Remove `project--soon` and add the GitHub link once it is public.
- [ ] Once the final address and a preview image (about 1200×630 px) exist, add `og:url`, `og:image` and a `<link rel="canonical">` to the `<head>`.
- [ ] Fonts load from Google Fonts. If your visitors include people in the EU, consider hosting the two font files yourself so no visitor data goes to Google.

## Deploy (GitHub Pages)

Settings → Pages → Source: *Deploy from a branch* → `main` / root.

Note: GitHub Pages on a private repository requires a paid GitHub plan. On a free plan, the repository must be public to publish the site.

## Contact

- Email: anil.hyperborea@gmail.com
- GitHub: [fas0ftware](https://github.com/fas0ftware)
- Instagram: [@fa.software](https://instagram.com/fa.software)
