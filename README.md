# FA Software — Website

Single-page portfolio site for **FA Software**: software services for automation, data, bots, networking and security tools, and web.

Plain HTML, CSS and JavaScript. No frameworks, no build step.

## Features

- Strictly black and white design, mobile-first and responsive
- Light and dark mode: follows the system preference, has a toggle, and remembers the choice in `localStorage`
- Logo switches with the theme
- Projects shown as horizontally swipeable cards (CSS scroll-snap)
- Semantic HTML, alt texts, skip link and keyboard-friendly focus styles

## Structure

```
index.html          Page content (hero, about, services, projects, contact)
css/style.css       All styles and theme tokens
js/main.js          Theme toggle
assets/
  logo-dark.png     Black logo, used on light backgrounds
  logo-light.png    White logo, used on dark backgrounds
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

## Deploy (GitHub Pages)

Settings → Pages → Source: *Deploy from a branch* → `main` / root.

Note: GitHub Pages on a private repository requires a paid GitHub plan. On a free plan, the repository must be public to publish the site.

## Contact

- Email: anil.hyperborea@gmail.com
- GitHub: [fas0ftware](https://github.com/fas0ftware)
- Instagram: [@fa.software](https://instagram.com/fa.software)
