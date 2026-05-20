# Octopus Bridge — REST API Documentation

[![Built with Docsify](https://img.shields.io/badge/built%20with-docsify-42b983)](https://docsify.js.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

The official, public REST API reference for **Octopus Bridge, Inc.** — the omni-channel commerce bridge.

This repository contains the source markdown and a [Docsify](https://docsify.js.org/) renderer. The site is published via **GitHub Pages**.

🌐 **Live docs:** _add your GitHub Pages URL here once published_
📧 **Support:** api@octopusbridge.com

---

## What's inside

```
.
├── index.html                 # Docsify single-page renderer
├── assets/
│   ├── style.css              # Custom Octopus Bridge theme
│   ├── favicon.svg            # Brand mark
│   └── logo.svg               # Replace with your real logo
├── docs/
│   ├── _sidebar.md            # Left-hand navigation
│   ├── coverpage.md           # Landing splash
│   ├── index.md               # Overview page
│   ├── quickstart.md          # 5-minute getting-started
│   ├── authentication.md      # Section 1
│   ├── shop.md                # Section 2
│   ├── products.md            # Section 3
│   ├── images.md              # Section 4
│   ├── variants.md            # Section 5
│   ├── locations.md           # Section 6
│   ├── inventory.md           # Section 7
│   ├── collections.md         # Section 8
│   ├── collects.md            # Section 9
│   ├── orders.md              # Section 10
│   ├── purchase-orders.md     # Section 11
│   ├── customers.md           # Section 12
│   ├── transactions.md        # Section 13
│   ├── faq.md                 # Section 14
│   ├── mapping.md             # Section 15
│   ├── samples.md             # Section 16
│   └── changelog.md
├── .nojekyll                  # tells GitHub Pages to skip Jekyll
└── README.md
```

---

## Publish to GitHub Pages — step by step

> No build step. No CI. Just push and flip a switch.

### 1. Create a new public repository on GitHub

1. Go to <https://github.com/new>.
2. Owner: your account or the **Octopus Bridge** organization.
3. Repository name: `octopus-bridge-api-docs` (or anything you prefer).
4. Visibility: **Public** ✅ (required for free GitHub Pages).
5. **Do not** initialize with a README, .gitignore or license — this repo already has them.
6. Click **Create repository**.

### 2. Push this folder

From the repository root on your machine:

```bash
cd octopus-bridge-docs

git init
git branch -M main
git add .
git commit -m "Initial publish — Octopus Bridge REST API v1.0"

git remote add origin https://github.com/<YOUR-ORG>/octopus-bridge-api-docs.git
git push -u origin main
```

### 3. Enable GitHub Pages

1. Go to **Settings → Pages** in your repo.
2. Under **Source**, choose **Deploy from a branch**.
3. Select branch **`main`** and folder **`/ (root)`**.
4. Click **Save**.
5. Wait ~30-60 seconds — GitHub will print a green banner with your URL, typically:

   ```
   https://<YOUR-ORG>.github.io/octopus-bridge-api-docs/
   ```

That's it. The site is live and public.

### 4. (Optional) Wire up a custom domain

If you own `developers.octopusbridge.com`:

1. Create a `CNAME` file at the repo root containing exactly:
   ```
   developers.octopusbridge.com
   ```
2. In your DNS provider, add a CNAME record pointing `developers.octopusbridge.com` → `<YOUR-ORG>.github.io`.
3. In **Settings → Pages → Custom domain**, enter the domain and tick **Enforce HTTPS**.

---

## Editing the docs

All content lives in `/docs` as plain Markdown. Edit a file, commit, push — the live site updates within a minute. No build step.

### Add a new page

1. Create `docs/my-new-page.md`.
2. Add a link to `docs/_sidebar.md`.
3. Commit & push.

### Local preview

```bash
# Option A — Python (built-in)
cd octopus-bridge-docs
python3 -m http.server 3000
# then open http://localhost:3000

# Option B — Docsify CLI (nicer)
npm i -g docsify-cli
docsify serve .
```

---

## Replacing the logo

Drop your real Octopus Bridge logo into `assets/logo.svg` (or `.png`) and reference it in `docs/coverpage.md` and `assets/style.css` (the `.sidebar .app-name-link::before` rule).

---

## License

Documentation © Octopus Bridge, Inc. — _All rights reserved_ for the API content itself.
The site scaffolding (HTML/CSS) is released under the [MIT License](LICENSE).
