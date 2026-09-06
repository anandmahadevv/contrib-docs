# gsoc-contrib Documentation Portal

Official technical documentation portal for [`gsoc-contrib`](https://github.com/anandmahadevv/contrib-cli) (`contrib`), the fast, lightweight contribution workspace manager for GitHub repositories.

🌐 **Live Documentation Portal:** [https://anandmahadevv.github.io/contrib-docs/](https://anandmahadevv.github.io/contrib-docs/)

---

## ✨ Features

- **⚡ Interactive Terminal Showcase**: Live simulated terminal demonstrations for `contrib start` (blobless 1.2s setup), `contrib dashboard` (TUI), `contrib sync`, and `contrib search`.
- **📊 Architecture Flowchart & Savings Calculator**: Clean visual SVG flowchart comparing traditional clones vs blobless worktrees, with an interactive calculator calculating bandwidth, time, and disk savings across repositories (React, Kubernetes, Linux, Requests).
- **📖 CLI Reference**: Full syntax, flags, descriptions, and examples for all 14 CLI commands.
- **🍳 Production Cookbook**: Advanced real-world recipes for massive monorepos (Kubernetes, PyTorch) with cone sparse mode, parallel multi-issue workspaces, compiled stacks (Rust, C++, Go), and headless CI test pipelines.
- **🛠️ Troubleshooting & FAQ**: Comprehensive solutions for corporate proxies & VPNs, GitHub API rate limits, interrupted checkout repairs, Git version requirements, and Windows long paths.
- **📜 Changelog & Releases**: Detailed version history from v0.4.0 down to v0.1.0 with feature badges and highlights.
- **🤝 Contributing Guide (Meta)**: Step-by-step dogfooding guide showing how to use `contrib` to contribute to `contrib` itself.
- **🧭 Next / Previous Sequential Navigation**: Smooth sequential page navigation at the bottom of every topic with keyboard shortcut support (`Alt + ←` / `Alt + →`).
- **📑 On This Page (TOC) Sidebar**: Sticky right-hand table of contents highlighting sections dynamically.
- **🔍 Dual Search**: Instant global search (`⌘K` / `Ctrl+K`) and in-page Google Docs-style find bar (`Ctrl+F`).
- **🌓 Dark & Light Mode**: Calibrated high-contrast theme switcher with system preference detection and anti-FOUC script.

---

## 🚀 Running Locally

```bash
npm run dev
# or
npx serve -l 5173 .
```

Then open `http://localhost:5173` in your browser.

---

## 📦 Deployment

This repository is purely static HTML/CSS/JS with zero build steps or heavy dependencies. It can be deployed directly to:

- **GitHub Pages**: Automated deployment on push to `main` branch.
- **Vercel**: Import this repository as a static project. No build command or output directory needed.
- **Cloudflare Pages / Netlify**: Direct static deployment from the root directory.

---

## 📄 License

[MIT](https://github.com/anandmahadevv/contrib-cli/blob/main/LICENSE) © [Anand](https://github.com/anandmahadevv)
