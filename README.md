# Astro Landing Page

A modern, fast, and responsive landing page built with [Astro](https://astro.build) and [Tailwind CSS](https://tailwindcss.com).

## Features

- ⚡ **Lightning Fast** - Zero JavaScript by default, optimal performance
- 🎨 **Responsive Design** - Mobile-first approach with Tailwind CSS
- 📦 **Component-Based** - Reusable Astro components for easy maintenance
- 🚀 **Production Ready** - Optimized build with best practices

## 🚀 Project Structure

```text
/
├── public/                 # Static assets
├── src/
│   ├── components/         # Reusable Astro components
│   │   ├── Header.astro
│   │   ├── Hero.astro
│   │   ├── Features.astro
│   │   ├── CTA.astro
│   │   └── Footer.astro
│   ├── layouts/           # Layout templates
│   │   └── Layout.astro
│   ├── pages/             # Page routes
│   │   └── index.astro
│   └── styles/            # Global styles
│       └── global.css
├── astro.config.mjs       # Astro configuration
├── tailwind.config.mjs    # Tailwind CSS configuration
└── package.json
```

## Getting Started

### Prerequisites
- Node.js 18+ 
- npm or yarn

### Installation

```sh
npm install
```

### Development

Start the local development server:

```sh
npm run dev
```

The site will be available at `http://localhost:4321`

### Building

Build the production-ready site:

```sh
npm run build
```

The optimized output will be in the `./dist/` directory.

### Preview

Preview your production build locally:

```sh
npm run preview
```

## 🧞 All Commands

| Command                   | Action                                      |
| :------------------------ | :------------------------------------------ |
| `npm install`             | Install dependencies                       |
| `npm run dev`             | Start dev server at `localhost:4321`       |
| `npm run build`           | Build production site to `./dist/`         |
| `npm run preview`         | Preview build locally before deploying     |
| `npm run astro add`       | Add integrations via Astro CLI              |

## 📦 Technologies Used

- **Astro** - Modern static site builder
- **Tailwind CSS** - Utility-first CSS framework
- **TypeScript** - Type-safe development

## 🎨 Components

The landing page includes the following components:

- **Header** - Navigation bar with logo and CTA
- **Hero** - Eye-catching hero section with headline
- **Features** - Showcase of key features with icons
- **CTA** - Call-to-action section
- **Footer** - Footer with links and copyright

## 📖 Learn More

- [Astro Documentation](https://docs.astro.build)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- [Astro Discord Community](https://astro.build/chat)

## 📝 License

This project is open source and available under the MIT License.

