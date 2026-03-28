# Astro Landing Page Project

A modern, responsive landing page built with Astro and Tailwind CSS.

## Project Status

✅ **Complete** - All setup and development tasks completed

## Project Structure

```
E_3/
├── src/
│   ├── components/       # Reusable components (Header, Hero, Features, CTA, Footer)
│   ├── layouts/          # Layout template
│   ├── pages/            # Page routes (index.astro)
│   └── styles/           # Global Tailwind styles
├── public/               # Static assets
├── .github/              # GitHub configuration
├── .vscode/              # VS Code settings and tasks
├── astro.config.mjs      # Astro configuration
├── tailwind.config.mjs   # Tailwind CSS configuration
└── package.json
```

## Key Features

- ⚡ Zero JavaScript by default (static generation)
- 🎨 Tailwind CSS for responsive design
- 📱 Mobile-first responsive layout
- 🧩 Reusable component architecture
- 🚀 Production-ready optimized build

## Development Commands

```bash
npm run dev      # Start dev server
npm run build    # Build for production
npm run preview  # Preview production build
```

## Components Included

1. **Header.astro** - Sticky navigation bar with logo and CTA button
2. **Hero.astro** - Main hero section with headline and CTAs
3. **Features.astro** - Feature showcase with emoji icons (3-column grid)
4. **CTA.astro** - Call-to-action section
5. **Footer.astro** - Footer with links and copyright

## Available Tasks

- **Astro Dev Server** - Runs development server (background task)
- **Astro Build** - Builds production project

## Dev Server

The development server is configured to run automatically when the project is opened in VS Code. Access it at: `http://localhost:4321`

## Dependencies

- `astro` - Web framework
- `@tailwindcss/vite` - Tailwind integration
- `tailwindcss` - CSS framework

## Customization Tips

- Edit component styles directly in the `.astro` files using Tailwind classes
- Modify global styles in `src/styles/global.css`
- Update component content in respective files in `src/components/`
- Add new pages by creating `.astro` files in `src/pages/`

## Resources

- [Astro Docs](https://docs.astro.build)
- [Tailwind CSS Docs](https://tailwindcss.com/docs)
- [Astro Community Discord](https://astro.build/chat)

