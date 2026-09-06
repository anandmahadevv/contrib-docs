# gsoc-contrib Documentation Portal

Official technical documentation portal for [`gsoc-contrib`](https://github.com/anandmahadevv/contrib-cli) (`contrib`), the fast, lightweight contribution workspace manager for GitHub repositories.

## ✨ Features

- **CLI Reference**: Full syntax, flags, descriptions, and examples for all 14 CLI commands.
- **Interactive Search**: Instant client-side search across all command documentation.
- **Architecture**: In-depth explanations of blobless clones (`--filter=blob:none`) and git worktrees.
- **Security & Privacy**: Zero-telemetry policy, local storage sandboxing, and network audit overview.
- **Dark & Light Mode**: Built-in theme switcher with system preference detection and anti-FOUC script.

## 🚀 Running Locally

```bash
npm run dev
# or
npx serve -l 5173 .
```

Then open `http://localhost:5173` in your browser.

## 📦 Deployment

This repository is purely static HTML/CSS/JS with zero build steps or heavy dependencies. It can be deployed directly to:

- **Vercel**: Import this repository as an "Other" / static project. No build command or output directory configuration needed.
- **GitHub Pages**: Go to **Settings** > **Pages** > **Build and deployment** > Source: **Deploy from a branch** (`main` / `/ (root)`).
- **Cloudflare Pages / Netlify**: Direct static deployment from the root directory.

## 📄 License

[MIT](https://github.com/anandmahadevv/contrib-cli/blob/main/LICENSE) © [Anand](https://github.com/anandmahadevv)
