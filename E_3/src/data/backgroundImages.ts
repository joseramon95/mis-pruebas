// Modelo: Configuración de imágenes de fondo por sección
export interface BackgroundConfig {
	section: string;
	imageUrl: string;
	gradientOverlay: string; // Gradiente semi-transparente
}

export const sectionBackgrounds: Record<string, BackgroundConfig> = {
	hero: {
		section: 'hero',
		imageUrl: '/e3-background.png',
		gradientOverlay: 'linear-gradient(135deg, rgba(30, 27, 75, 0.85) 0%, rgba(14, 165, 233, 0.75) 100%)',
	},
	carousel: {
		section: 'carousel',
		imageUrl: '/e3-background.png',
		gradientOverlay: 'linear-gradient(135deg, rgba(255, 255, 255, 0.85) 0%, rgba(14, 165, 233, 0.75) 100%)',
    },
	cta: {
		section: 'cta',
		imageUrl: 'https://images.unsplash.com/photo-1504384308090-c894fdcc538d?w=1200&auto=format&fit=crop&q=60',
		gradientOverlay: 'linear-gradient(135deg, rgba(30, 27, 75, 0.88) 0%, rgba(59, 130, 246, 0.8) 100%)',
	},
};
