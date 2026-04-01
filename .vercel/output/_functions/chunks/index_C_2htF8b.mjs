import { c as createComponent } from './astro-component_BDiEcpf7.mjs';
import 'piccolore';
import { x as maybeRenderHead, a2 as addAttribute, L as renderTemplate } from './sequence_5BlAyHOu.mjs';
import { r as renderComponent } from './entrypoint_CLZx3I2z.mjs';
import { s as sectionBackgrounds, r as renderScript, $ as $$Layout, a as $$Header, b as $$Footer } from './Footer_BMs7be-y.mjs';
import 'clsx';

const API_URL = "http://localhost:5000";
async function fetchComponentes() {
  try {
    const response = await fetch(`${API_URL}/api/componentes`);
    if (response.ok) {
      return await response.json();
    }
  } catch (error) {
    console.error("Error fetching componentes:", error);
  }
  return [];
}
async function getComponente(nombre) {
  const componentes = await fetchComponentes();
  return componentes.find((c) => c.nombre === nombre) || null;
}

const $$Hero = createComponent(async ($$result, $$props, $$slots) => {
  const heroBackground = sectionBackgrounds.hero;
  const componente = await getComponente("Hero");
  const titulo = componente?.titulo || "Nosotros Resolvemos";
  const subtitulo = componente?.subtitulo || "Tus Problemas";
  const contenido = componente?.contenido || "Soluciones estratégicas de alta complejidad para transformar tu incertidumbre en crecimiento.";
  const link = componente?.link || "/cotizaciones";
  return renderTemplate`${maybeRenderHead()}<section class="min-h-screen flex items-center justify-center px-4 relative overflow-hidden"${addAttribute({
    backgroundImage: `url('${heroBackground.imageUrl}')`,
    backgroundSize: "cover",
    backgroundPosition: "center",
    backgroundAttachment: "fixed"
  }, "style")}> <div class="absolute inset-0"${addAttribute({
    background: heroBackground.gradientOverlay
  }, "style")}></div> <div class="absolute top-10 right-10 w-40 h-40 bg-amber-300 rounded-full opacity-10 blur-3xl"></div> <div class="absolute bottom-10 left-10 w-40 h-40 bg-amber-400 rounded-full opacity-10 blur-3xl"></div> <div class="max-w-4xl mx-auto text-center relative z-10"> <h1 class="text-3xl md:text-4xl font-semibold text-white mb-4"> ${titulo} </h1> <h2 class="text-6xl md:text-8xl font-bold text-gold-400 mb-8"> ${subtitulo} </h2> <p class="text-xl md:text-2xl text-white/90 mb-8 max-w-2xl mx-auto"> ${contenido} </p> <div class="flex justify-center"> <a${addAttribute(link, "href")} target="_blank" class="bg-gold-400 text-navy-900 px-8 py-4 rounded-lg font-bold hover:bg-gold-300 transition text-lg shadow-lg border-2 border-gold-500"> ${componente?.extra_data || "¿Te Interesa Alguno de Nuestros Servicios?"} </a> </div> </div> </section>`;
}, "C:/Users/Naru/Desktop/mis-pruebas/src/components/Hero.astro", void 0);

const $$Carousel = createComponent(($$result, $$props, $$slots) => {
  const Astro2 = $$result.createAstro($$props, $$slots);
  Astro2.self = $$Carousel;
  const { items, title = "POR QUE ESCOGERNOS?", description = "Experimente la potencia de la arquitectura insular y la hidratación parcial para lograr tiempos de carga ultrarrápidos." } = Astro2.props;
  const carouselBackground = sectionBackgrounds.carousel;
  return renderTemplate`${maybeRenderHead()}<section id="carousel" class="py-20 px-4 relative overflow-hidden"${addAttribute({
    backgroundImage: `url('${carouselBackground.imageUrl}')`,
    backgroundSize: "cover",
    backgroundPosition: "center",
    backgroundAttachment: "fixed"
  }, "style")} data-astro-cid-wfe7xcno> <!-- Gradiente superpuesto --> <div class="absolute inset-0"${addAttribute({
    background: carouselBackground.gradientOverlay
  }, "style")} data-astro-cid-wfe7xcno></div> <div class="max-w-6xl mx-auto relative z-10" data-astro-cid-wfe7xcno> <h2 class="text-4xl font-bold text-center mb-4 text-navy-800" data-astro-cid-wfe7xcno> ${title} </h2> <p class="text-center text-navy-600 mb-12 max-w-2xl mx-auto font-medium" data-astro-cid-wfe7xcno> ${description} </p> <!-- Carousel Container --> <div class="relative" data-astro-cid-wfe7xcno> <!-- Carousel Wrapper --> <div class="overflow-hidden rounded-lg" data-astro-cid-wfe7xcno> <div id="carousel-track" class="flex transition-transform duration-500 ease-out" style="width: 100%;" data-astro-cid-wfe7xcno> ${items.map((item) => renderTemplate`<div class="min-w-full px-4 py-8 flex justify-center" data-astro-cid-wfe7xcno> <div class="w-full max-w-sm aspect-square" data-astro-cid-wfe7xcno> <div class="relative bg-gradient-to-br from-navy-800 via-navy-900 to-navy-800 rounded-2xl p-6 h-full flex flex-col overflow-hidden shadow-2xl hover:shadow-golden transition-all duration-500 hover:scale-[1.02] border border-gold-500/50" data-astro-cid-wfe7xcno> <div class="absolute top-0 right-0 w-32 h-32 bg-gradient-to-br from-gold-400/20 to-yellow-600/10 rounded-full blur-2xl" data-astro-cid-wfe7xcno></div> <div class="absolute bottom-0 left-0 w-24 h-24 bg-gradient-to-tr from-yellow-600/20 to-gold-400/10 rounded-full blur-xl" data-astro-cid-wfe7xcno></div> <div class="relative z-10 flex flex-col items-center h-full" data-astro-cid-wfe7xcno> <div class="w-20 h-20 rounded-full bg-gradient-to-br from-gold-400 via-yellow-500 to-gold-600 p-1 mb-4 shadow-lg" data-astro-cid-wfe7xcno> <div class="w-full h-full rounded-full bg-navy-900 flex items-center justify-center overflow-hidden" data-astro-cid-wfe7xcno> <img${addAttribute(item.image, "src")}${addAttribute(item.title, "alt")} class="w-full h-full object-cover" data-astro-cid-wfe7xcno> </div> </div> <h3 class="text-lg font-bold text-center mb-2 text-white" data-astro-cid-wfe7xcno> ${item.title} </h3> <p class="text-white/70 text-xs text-center leading-relaxed flex-1" data-astro-cid-wfe7xcno> ${item.description} </p> <div class="w-full pt-4 mt-auto" data-astro-cid-wfe7xcno> <div class="h-px bg-gradient-to-r from-transparent via-gold-500/50 to-transparent mb-4" data-astro-cid-wfe7xcno></div> <a${addAttribute(item.contact.link, "href")} target="_blank" class="flex items-center justify-center gap-2 bg-gradient-to-r from-gold-500 to-yellow-500 text-navy-900 px-4 py-2.5 rounded-lg font-bold text-sm hover:from-gold-400 hover:to-yellow-400 transition-all shadow-md border border-gold-400" data-astro-cid-wfe7xcno> <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24" data-astro-cid-wfe7xcno> <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z" data-astro-cid-wfe7xcno></path> </svg> ${item.contact.text} </a> </div> </div> </div> </div> </div>`)} </div> </div> </div> <!-- Navigation Buttons --> <button id="prev-btn" class="absolute left-0 top-1/2 -translate-y-1/2 -translate-x-16 bg-navy-800 text-white p-3 rounded-full hover:bg-navy-900 transition z-20 border-2 border-gold-500" data-astro-cid-wfe7xcno> <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" data-astro-cid-wfe7xcno> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" data-astro-cid-wfe7xcno></path> </svg> </button> <button id="next-btn" class="absolute right-0 top-1/2 -translate-y-1/2 translate-x-16 bg-navy-800 text-white p-3 rounded-full hover:bg-navy-900 transition z-20 border-2 border-gold-500" data-astro-cid-wfe7xcno> <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" data-astro-cid-wfe7xcno> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" data-astro-cid-wfe7xcno></path> </svg> </button> <!-- Indicators --> <div id="carousel-indicators" class="flex justify-center gap-2 mt-8" data-astro-cid-wfe7xcno> ${items.map((_, index) => renderTemplate`<button class="indicator-btn w-3 h-3 rounded-full transition-all"${addAttribute(index, "data-index")}${addAttribute(`Go to slide ${index + 1}`, "aria-label")}${addAttribute(index === 0 ? "background-color: #ca8a04; width: 24px;" : "background-color: #0d1b2e;", "style")} data-astro-cid-wfe7xcno></button>`)} </div> </div> </section> ${renderScript($$result, "C:/Users/Naru/Desktop/mis-pruebas/src/components/Carousel.astro?astro&type=script&index=0&lang.ts")}`;
}, "C:/Users/Naru/Desktop/mis-pruebas/src/components/Carousel.astro", void 0);

const $$Features = createComponent(($$result, $$props, $$slots) => {
  const Astro2 = $$result.createAstro($$props, $$slots);
  Astro2.self = $$Features;
  const { items, title, description } = Astro2.props;
  return renderTemplate`${renderComponent($$result, "Carousel", $$Carousel, { "items": items, "title": title, "description": description })}`;
}, "C:/Users/Naru/Desktop/mis-pruebas/src/components/Features.astro", void 0);

const $$AboutUs = createComponent(async ($$result, $$props, $$slots) => {
  const componente = await getComponente("AboutUs");
  const titulo = componente?.titulo || "Quiénes Somos";
  const subtitulo = componente?.contenido || "E³: Consultora especializada en soluciones de alta complejidad";
  const extraData = componente?.extra_data ? JSON.parse(componente.extra_data) : {};
  return renderTemplate`${maybeRenderHead()}<section id="quienes-somos" class="py-20 px-4 bg-white"> <div class="max-w-6xl mx-auto"> <h2 class="text-4xl font-bold text-center mb-4 text-navy-800"> ${titulo} </h2> <p class="text-center text-navy-600 mb-12 max-w-2xl mx-auto font-medium"> ${subtitulo} </p> <div class="grid md:grid-cols-2 gap-12 items-center"> <div> <div class="text-6xl mb-6">🏛️</div> <h3 class="text-2xl font-bold text-navy-800 mb-4"> ${extraData.subtituloSeccion || "Solidez Económica y Estrategia Política"} </h3> <p class="text-slate-600 mb-4"> ${extraData.descripcion1 || 'En E³, respondemos con la disposición de Isaías ("Heme aquí") para resolver los desafíos más complejos de nuestros clientes. Somos una consultora especializada en transformar la incertidumbre en estructuras sólidas de crecimiento.'} </p> <p class="text-slate-600"> ${extraData.descripcion2 || "Nuestra fortaleza radica en la fusión del análisis económico riguroso con la precisión política, permitiendo que nuestros clientes construyan organizaciones verdaderamente resilientes y éticas."} </p> </div> <div class="bg-gradient-to-br from-navy-800 to-gold-500 rounded-lg p-8 text-white border-2 border-gold-400 shadow-xl"> <h4 class="text-xl font-bold mb-6">Nuestros Valores Fundacionales</h4> <ul class="space-y-3"> <li class="flex items-center gap-2"> <span class="text-gold-400">✓</span> <span>${extraData.valor1 || "Precisión en el análisis económico"}</span> </li> <li class="flex items-center gap-2"> <span class="text-gold-400">✓</span> <span>${extraData.valor2 || "Integridad en la acción estratégica"}</span> </li> <li class="flex items-center gap-2"> <span class="text-gold-400">✓</span> <span>${extraData.valor3 || "Solidez estructural garantizada"}</span> </li> <li class="flex items-center gap-2"> <span class="text-gold-400">✓</span> <span>${extraData.valor4 || "Resiliencia ante cualquier crisis"}</span> </li> <li class="flex items-center gap-2"> <span class="text-gold-400">✓</span> <span>${extraData.valor5 || "Ética como pilar fundamental"}</span> </li> </ul> </div> </div> <div class="mt-12 text-center bg-gold-50 rounded-lg p-8 border-l-4 border-r-4 border-navy-800 shadow-md"> <p class="text-2xl font-bold text-navy-800 italic"> ${extraData.lema || '"Estructura sobre la roca, resultados en la abundancia"'} </p> </div> </div> </section>`;
}, "C:/Users/Naru/Desktop/mis-pruebas/src/components/AboutUs.astro", void 0);

const $$MisionVision = createComponent(async ($$result, $$props, $$slots) => {
  const componente = await getComponente("MisionVision");
  const titulo = componente?.titulo || "Misión y Visión";
  componente?.contenido || "";
  const extraData = componente?.extra_data ? JSON.parse(componente.extra_data) : {};
  const mision = extraData.mision || "Brindar soluciones estratégicas de alta complejidad mediante el rigor del análisis económico y la precisión política, transformando la incertidumbre en estructuras sólidas de crecimiento para nuestros clientes.";
  const vision = extraData.vision || "Ser la consultora referente en México en el diseño de soluciones de alta complejidad, donde la ciencia económica y la estrategia política se fusionan para edificar organizaciones resilientes, éticas y estructuralmente inquebrantables.";
  const lema = extraData.lema || '"Transformar el caos en estructura mediante la integridad y la acción estratégica."';
  const lemaAdicional = extraData.lemaAdicional || 'En E³, respondemos con la disposición de Isaías ("Heme aquí") para resolver los desafíos más complejos de nuestros clientes. Nuestra misión es fortalecer el núcleo vital de las organizaciones —la "santa semilla"—, aplicando una visión técnica y ética que garantiza solidez en el mercado y resiliencia ante cualquier crisis.';
  const lemaFinal = extraData.lemaFinal || "Estructura sobre la roca, resultados en la abundancia.";
  return renderTemplate`${maybeRenderHead()}<section id="mision-vision" class="py-20 px-4 bg-gradient-to-r from-navy-50 to-gold-50"> <div class="max-w-6xl mx-auto"> <h2 class="text-4xl font-bold text-center mb-12 text-navy-800"> ${titulo} </h2> <div class="grid md:grid-cols-2 gap-8 mb-12"> <div class="bg-white rounded-lg p-8 border-l-4 border-navy-800 shadow-lg hover:shadow-2xl transition-all border-r-2 border-gold-400"> <div class="flex items-center gap-3 mb-4"> <div class="w-10 h-10 text-gold-500"> <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"></path> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path> </svg> </div> <h3 class="text-2xl font-bold text-navy-800">Nuestra Misión</h3> </div> <p class="text-slate-600 leading-relaxed"> ${mision} </p> </div> <div class="bg-white rounded-lg p-8 border-l-4 border-gold-500 shadow-lg hover:shadow-2xl transition-all border-r-2 border-navy-800"> <div class="flex items-center gap-3 mb-4"> <div class="w-10 h-10 text-gold-500"> <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path> </svg> </div> <h3 class="text-2xl font-bold text-navy-800">Nuestra Visión</h3> </div> <p class="text-slate-600 leading-relaxed"> ${vision} </p> </div> </div> <div class="bg-white rounded-lg p-12 border-2 border-gold-500 text-center mb-12 shadow-xl shadow-gold-200/50"> <p class="text-2xl font-bold text-navy-800 italic mb-6"> ${lema} </p> <p class="text-slate-600 leading-relaxed mb-6"> ${lemaAdicional} </p> <p class="text-lg font-bold text-navy-700 pt-4 border-t-2 border-gold-500"> ${lemaFinal} </p> </div> <div class="bg-gradient-to-r from-navy-800 to-navy-900 rounded-lg p-8 text-white border-2 border-gold-500 shadow-xl"> <h3 class="text-2xl font-bold mb-6 flex items-center gap-2"> <div class="w-8 h-8 text-gold-400"> <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path> </svg> </div>
Nuestros Pilares
</h3> <div class="grid md:grid-cols-3 gap-6"> <div class="text-center"> <div class="w-14 h-14 mx-auto mb-3 text-gold-400"> <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"></path> </svg> </div> <p class="font-semibold">Precisión Analítica</p> <p class="text-sm text-white/70 mt-2">Rigor económico y estratégico</p> </div> <div class="text-center"> <div class="w-14 h-14 mx-auto mb-3 text-gold-400"> <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path> </svg> </div> <p class="font-semibold">Integridad Institucional</p> <p class="text-sm text-white/70 mt-2">Ética y solidez garantizada</p> </div> <div class="text-center"> <div class="w-14 h-14 mx-auto mb-3 text-gold-400"> <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path> </svg> </div> <p class="font-semibold">Crecimiento Resiliente</p> <p class="text-sm text-white/70 mt-2">Estructuras duraderas</p> </div> </div> </div> </div> </section>`;
}, "C:/Users/Naru/Desktop/mis-pruebas/src/components/MisionVision.astro", void 0);

const $$CTA = createComponent(async ($$result, $$props, $$slots) => {
  const ctaBackground = sectionBackgrounds.cta;
  const componente = await getComponente("CTA");
  const titulo = componente?.titulo || "Listo Para Construir Algo Asombroso?";
  const contenido = componente?.contenido || "Comienza a construir tu próximo proyecto con E³ hoy.";
  const link = componente?.link || "https://wa.me/526677800166";
  const botonTexto = componente?.extra_data || "Comienza a Construir Ahora";
  return renderTemplate`${maybeRenderHead()}<section class="py-20 px-4 relative overflow-hidden"${addAttribute({
    backgroundImage: `url('${ctaBackground.imageUrl}')`,
    backgroundSize: "cover",
    backgroundPosition: "center",
    backgroundAttachment: "fixed"
  }, "style")}> <div class="absolute inset-0"${addAttribute({
    background: ctaBackground.gradientOverlay
  }, "style")}></div> <div class="absolute top-0 right-0 w-96 h-96 bg-amber-400 rounded-full opacity-10 blur-3xl -translate-y-1/2 translate-x-1/2"></div> <div class="absolute bottom-0 left-0 w-72 h-72 bg-amber-300 rounded-full opacity-5 blur-3xl translate-y-1/2 -translate-x-1/2"></div> <div class="max-w-4xl mx-auto text-center relative z-10"> <h2 class="text-4xl font-bold text-white mb-4"> ${titulo} </h2> <p class="text-xl text-white/80 mb-8 font-medium"> ${contenido} </p> <button${addAttribute(`window.open('${link}', '_blank')`, "onclick")} class="bg-gold-400 text-navy-900 px-8 py-4 rounded-lg font-bold hover:bg-gold-300 transition text-lg shadow-lg transform hover:scale-105 border-2 border-gold-500"> ${botonTexto} </button> </div> </section>`;
}, "C:/Users/Naru/Desktop/mis-pruebas/src/components/CTA.astro", void 0);

const $$Contact = createComponent(async ($$result, $$props, $$slots) => {
  const componente = await getComponente("Contact");
  const titulo = componente?.titulo || "Contacto";
  const subtitulo = componente?.contenido || "¿Tienes preguntas? Nos encantaría escucharte. Envíanos un mensaje.";
  const link = componente?.link || "https://formspree.io/f/YOUR_FORMSPREE_ID";
  const extraData = componente?.extra_data ? JSON.parse(componente.extra_data) : { email: "PENDIENTE", telefono: "+52 PENDIENTE", ubicacion: "Culiacan, Sinaloa" };
  return renderTemplate`${maybeRenderHead()}<section id="contacto" class="py-20 px-4 bg-slate-50"> <div class="max-w-4xl mx-auto"> <div class="text-center mb-12"> <h2 class="text-4xl font-bold text-navy-800 mb-4">${titulo}</h2> <p class="text-lg text-navy-600"> ${subtitulo} </p> </div> <form id="contactForm"${addAttribute(link, "action")} method="POST" class="bg-white rounded-lg border-2 border-gold-500 p-8 shadow-xl shadow-gold-200/30"> <div class="grid md:grid-cols-2 gap-6 mb-6"> <div> <label for="name" class="block text-navy-800 font-semibold mb-2">Nombre Completo</label> <input type="text" id="name" name="name" required class="w-full px-4 py-2 border-2 border-gold-400 rounded-lg focus:outline-none focus:border-navy-800 focus:bg-gold-50 transition" placeholder="Tu nombre"> </div> <div> <label for="email" class="block text-navy-800 font-semibold mb-2">Correo Electrónico</label> <input type="email" id="email" name="email" required class="w-full px-4 py-2 border-2 border-gold-400 rounded-lg focus:outline-none focus:border-navy-800 focus:bg-gold-50 transition" placeholder="tu@email.com"> </div> </div> <div class="mb-6"> <label for="phone" class="block text-navy-800 font-semibold mb-2">Teléfono (Opcional)</label> <input type="tel" id="phone" name="phone" class="w-full px-4 py-2 border-2 border-gold-400 rounded-lg focus:outline-none focus:border-navy-800 focus:bg-gold-50 transition" placeholder="+52 000 000-0000"> </div> <div class="mb-6"> <label for="subject" class="block text-navy-800 font-semibold mb-2">Asunto</label> <input type="text" id="subject" name="subject" required class="w-full px-4 py-2 border-2 border-gold-400 rounded-lg focus:outline-none focus:border-navy-800 focus:bg-gold-50 transition" placeholder="¿En qué podemos ayudarte?"> </div> <div class="mb-8"> <label for="message" class="block text-navy-800 font-semibold mb-2">Mensaje</label> <textarea id="message" name="message" required rows="6" class="w-full px-4 py-2 border-2 border-gold-400 rounded-lg focus:outline-none focus:border-navy-800 focus:bg-gold-50 transition resize-none" placeholder="Cuéntanos tu mensaje..."></textarea> </div> <div class="flex justify-center"> <button type="submit" class="bg-navy-800 text-white px-10 py-3 rounded-lg font-bold hover:bg-navy-900 transition transform hover:scale-105 shadow-lg border-2 border-gold-500">
Enviar Mensaje
</button> </div> </form> <div class="grid md:grid-cols-3 gap-8 mt-12"> <div class="text-center"> <div class="w-12 h-12 mx-auto mb-4 flex items-center justify-center border-2 border-navy-800 rounded-full bg-gold-50"> <span class="text-xl text-gold-500">✉</span> </div> <h3 class="font-bold text-navy-800 mb-1">Email</h3> <p class="text-slate-600">${extraData.email || "PENDIENTE"}</p> </div> <div class="text-center"> <div class="w-12 h-12 mx-auto mb-4 flex items-center justify-center border-2 border-navy-800 rounded-full bg-gold-50"> <span class="text-xl text-gold-500">☎</span> </div> <h3 class="font-bold text-navy-800 mb-1">Teléfono</h3> <p class="text-slate-600">${extraData.telefono || "+52 PENDIENTE"}</p> </div> <div class="text-center"> <div class="w-12 h-12 mx-auto mb-4 flex items-center justify-center border-2 border-navy-800 rounded-full bg-gold-50"> <span class="text-xl text-gold-500">◉</span> </div> <h3 class="font-bold text-navy-800 mb-1">Ubicación</h3> <p class="text-slate-600">${extraData.ubicacion || "Culiacan, Sinaloa"}</p> </div> </div> </div> </section> ${renderScript($$result, "C:/Users/Naru/Desktop/mis-pruebas/src/components/Contact.astro?astro&type=script&index=0&lang.ts")}`;
}, "C:/Users/Naru/Desktop/mis-pruebas/src/components/Contact.astro", void 0);

const prerender = false;
const $$Index = createComponent(async ($$result, $$props, $$slots) => {
  const Astro2 = $$result.createAstro($$props, $$slots);
  Astro2.self = $$Index;
  const API_URL = "https://e3-admin-api.onrender.com";
  const CACHE_MAX_AGE = 60 * 60 * 24 * 7;
  Astro2.response.headers.set("Cache-Control", `public, max-age=${CACHE_MAX_AGE}, s-maxage=${CACHE_MAX_AGE}, stale-while-revalidate=${CACHE_MAX_AGE}`);
  let items = [];
  let title = "La Arquitectura de la Certeza en Entornos de Alta Complejidad";
  let description = "En un mercado definido por la volatilidad, E³ construye la infraestructura del éxito. No solo ofrecemos asesoría: transformamos la incertidumbre en activos de crecimiento mediante tres pilares innegociables.";
  try {
    const [sociosRes, componenteRes] = await Promise.all([
      fetch(`${API_URL}/api/socios`),
      fetch(`${API_URL}/api/componentes/Features`)
    ]);
    if (sociosRes.ok) {
      items = await sociosRes.json();
    }
    if (componenteRes.ok) {
      const componente = await componenteRes.json();
      if (componente) {
        title = componente.titulo || title;
        description = componente.contenido || description;
      }
    }
  } catch (error) {
    console.error("Error fetching data:", error);
  }
  if (items.length === 0) {
    items = [{
      id: 1,
      title: "Cargando...",
      description: "Obteniendo datos del servidor",
      image: "/persona-no-bg.png",
      contact: { text: "Contactar", link: "#" }
    }];
  }
  return renderTemplate`${renderComponent($$result, "Layout", $$Layout, { "title": "PAGINA DE PRUEBA E³", "description": "Innovación y excelencia en soluciones web" }, { "default": async ($$result2) => renderTemplate` ${renderComponent($$result2, "Header", $$Header, {})} ${renderComponent($$result2, "Hero", $$Hero, {})} ${renderComponent($$result2, "Features", $$Features, { "items": items, "title": title, "description": description })} ${renderComponent($$result2, "AboutUs", $$AboutUs, {})} ${renderComponent($$result2, "MisionVision", $$MisionVision, {})} ${renderComponent($$result2, "CTA", $$CTA, {})} ${renderComponent($$result2, "Contact", $$Contact, {})} ${renderComponent($$result2, "Footer", $$Footer, {})} ` })}`;
}, "C:/Users/Naru/Desktop/mis-pruebas/src/pages/index.astro", void 0);
const $$file = "C:/Users/Naru/Desktop/mis-pruebas/src/pages/index.astro";
const $$url = "";

const _page = /*#__PURE__*/Object.freeze(/*#__PURE__*/Object.defineProperty({
    __proto__: null,
    default: $$Index,
    file: $$file,
    prerender,
    url: $$url
}, Symbol.toStringTag, { value: 'Module' }));

const page = () => _page;

export { page };
