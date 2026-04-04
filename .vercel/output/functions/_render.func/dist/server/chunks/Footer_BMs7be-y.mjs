import { c as createComponent } from './astro-component_BDiEcpf7.mjs';
import 'piccolore';
import { P as createRenderInstruction, a2 as addAttribute, b7 as renderHead, b8 as renderSlot, L as renderTemplate, x as maybeRenderHead } from './sequence_5BlAyHOu.mjs';
import 'clsx';

async function renderScript(result, id) {
  const inlined = result.inlinedScripts.get(id);
  let content = "";
  if (inlined != null) {
    if (inlined) {
      content = `<script type="module">${inlined}</script>`;
    }
  } else {
    const resolved = await result.resolve(id);
    content = `<script type="module" src="${result.userAssetsBase ? (result.base === "/" ? "" : result.base) + result.userAssetsBase : ""}${resolved}"></script>`;
  }
  return createRenderInstruction({ type: "script", id, content });
}

const $$Layout = createComponent(($$result, $$props, $$slots) => {
  const Astro2 = $$result.createAstro($$props, $$slots);
  Astro2.self = $$Layout;
  const { title, description = "PAGINA DE PRUEBA E^3" } = Astro2.props;
  return renderTemplate`<html lang="es"> <head><meta charset="utf-8"><link rel="icon" type="image/svg+xml" href="/favicon.svg"><meta name="viewport" content="width=device-width"><meta name="description"${addAttribute(description, "content")}><meta name="generator"${addAttribute(Astro2.generator, "content")}><title>${title}</title>${renderHead()}</head> <body class="bg-slate-50 text-slate-900"> ${renderSlot($$result, $$slots["default"])}</body></html>`;
}, "C:/Users/Naru/Desktop/mis-pruebas/src/layouts/Layout.astro", void 0);

const $$Header = createComponent(($$result, $$props, $$slots) => {
  return renderTemplate`${maybeRenderHead()}<header class="sticky top-0 z-50 bg-white/95 backdrop-blur-md shadow-sm border-b border-gray-100"> <nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"> <div class="flex justify-between items-center h-16"> <a href="/" class="flex items-center gap-3 group"> <img src="/e3.ico" alt="E3 Logo" class="w-10 h-10 transition-transform group-hover:scale-110"> <span class="text-xl font-bold text-gray-900 tracking-tight">E³ Consultoría</span> </a> <div class="hidden md:flex items-center gap-1"> <a href="#quienes-somos" class="px-4 py-2 text-gray-700 hover:text-primary font-medium rounded-lg hover:bg-gray-50 transition">
Quiénes Somos
</a> <a href="#mision-vision" class="px-4 py-2 text-gray-700 hover:text-primary font-medium rounded-lg hover:bg-gray-50 transition">
Misión y Visión
</a> <a href="#soluciones" class="px-4 py-2 text-gray-700 hover:text-primary font-medium rounded-lg hover:bg-gray-50 transition">
Soluciones
</a> <a href="#contacto" class="px-4 py-2 text-gray-700 hover:text-primary font-medium rounded-lg hover:bg-gray-50 transition">
Contacto
</a> </div> <a href="/cotizaciones" target="_blank" class="hidden md:inline-flex items-center gap-2 bg-navy-800 text-white px-6 py-2.5 rounded-lg font-semibold hover:bg-navy-900 transition-all hover:shadow-lg border-2 border-gold-500 hover:-translate-y-0.5">
Cotiza con Nosotros
</a> <button id="menu-btn" class="md:hidden p-2 rounded-lg hover:bg-gray-100 transition"> <svg class="w-6 h-6 text-gray-700" fill="none" stroke="currentColor" viewBox="0 0 24 24"> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path> </svg> </button> </div> <div id="mobile-menu" class="hidden md:hidden pb-4"> <div class="flex flex-col gap-1 pt-2 border-t border-gray-100"> <a href="#quienes-somos" class="px-4 py-2 text-gray-700 hover:text-primary hover:bg-gray-50 rounded-lg transition">Quiénes Somos</a> <a href="#mision-vision" class="px-4 py-2 text-gray-700 hover:text-primary hover:bg-gray-50 rounded-lg transition">Misión y Visión</a> <a href="#soluciones" class="px-4 py-2 text-gray-700 hover:text-primary hover:bg-gray-50 rounded-lg transition">Soluciones</a> <a href="#contacto" class="px-4 py-2 text-gray-700 hover:text-primary hover:bg-gray-50 rounded-lg transition">Contacto</a> </div> </div> </nav> </header> ${renderScript($$result, "C:/Users/Naru/Desktop/mis-pruebas/src/components/Header.astro?astro&type=script&index=0&lang.ts")}`;
}, "C:/Users/Naru/Desktop/mis-pruebas/src/components/Header.astro", void 0);

const sectionBackgrounds = {
  hero: {
    imageUrl: "/e3-background.png",
    gradientOverlay: "linear-gradient(135deg, rgba(13, 27, 46, 0.92) 0%, rgba(5, 13, 23, 0.88) 100%)"
  },
  carousel: {
    imageUrl: "/e3-background.png",
    gradientOverlay: "linear-gradient(135deg, rgba(255, 255, 255, 0.85) 0%, rgba(13, 27, 46, 0.85) 100%)"
  },
  cta: {
    imageUrl: "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?w=1200&auto=format&fit=crop&q=60",
    gradientOverlay: "linear-gradient(135deg, rgba(13, 27, 46, 0.95) 0%, rgba(5, 13, 23, 0.92) 100%)"
  }
};

const $$Footer = createComponent(($$result, $$props, $$slots) => {
  return renderTemplate`${maybeRenderHead()}<footer class="bg-navy-900 text-white/80"> <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"> <div class="py-16 border-t-4 border-gold-500"> <div class="grid lg:grid-cols-4 gap-12"> <div class="lg:col-span-1"> <a href="/" class="flex items-center gap-3 mb-6"> <img src="/e3.ico" alt="E3 Logo" class="w-10 h-10"> <span class="text-xl font-bold text-white">E³ Consultoría</span> </a> <p class="text-white/60 text-sm leading-relaxed">
Transformamos la incertidumbre en estructuras sólidas de crecimiento mediante soluciones estratégicas de alta complejidad.
</p> </div> <div> <h4 class="text-white font-semibold mb-6">Empresa</h4> <ul class="space-y-3 text-sm"> <li><a href="#quienes-somos" class="text-white/60 hover:text-gold-400 transition">Quiénes Somos</a></li> <li><a href="#mision-vision" class="text-white/60 hover:text-gold-400 transition">Misión y Visión</a></li> <li><a href="#soluciones" class="text-white/60 hover:text-gold-400 transition">Soluciones</a></li> <li><a href="#contacto" class="text-white/60 hover:text-gold-400 transition">Contacto</a></li> </ul> </div> <div> <h4 class="text-white font-semibold mb-6">Legal</h4> <ul class="space-y-3 text-sm"> <li><a href="/privacidad" class="text-white/60 hover:text-gold-400 transition">Política de Privacidad</a></li> <li><a href="/terminos" class="text-white/60 hover:text-gold-400 transition">Términos de Servicio</a></li> <li><a href="/cookies" class="text-white/60 hover:text-gold-400 transition">Cookies</a></li> </ul> </div> <div> <h4 class="text-white font-semibold mb-6">Síguenos</h4> <div class="flex gap-4"> <a href="https://twitter.com" target="_blank" rel="noopener noreferrer" aria-label="Twitter" class="w-10 h-10 bg-navy-800 border border-gold-500/30 rounded-lg flex items-center justify-center hover:bg-gold-500 hover:text-navy-900 transition"> <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"></path></svg> </a> <a href="https://github.com" target="_blank" rel="noopener noreferrer" aria-label="GitHub" class="w-10 h-10 bg-navy-800 border border-gold-500/30 rounded-lg flex items-center justify-center hover:bg-gold-500 hover:text-navy-900 transition"> <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"></path></svg> </a> <a href="https://linkedin.com" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn" class="w-10 h-10 bg-navy-800 border border-gold-500/30 rounded-lg flex items-center justify-center hover:bg-gold-500 hover:text-navy-900 transition"> <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"></path></svg> </a> </div> </div> </div> </div> <div class="border-t border-gold-500/30 py-8"> <div class="flex flex-col md:flex-row justify-between items-center gap-4"> <p class="text-sm text-white/50">© 2026 E³ Consultoría. Todos los derechos reservados.</p> <div class="flex items-center gap-6 text-sm text-white/50"> <a href="/privacidad" class="hover:text-gold-400 transition">Política de Privacidad</a> <a href="/terminos" class="hover:text-gold-400 transition">Términos</a> </div> </div> </div> </div> </footer>`;
}, "C:/Users/Naru/Desktop/mis-pruebas/src/components/Footer.astro", void 0);

export { $$Layout as $, $$Header as a, $$Footer as b, renderScript as r, sectionBackgrounds as s };
