// Modelo: Configuración de imágenes de fondo por sección
export interface BackgroundConfig {
	section: string;
	imageUrl: string;
	gradientOverlay: string;
}

export const sectionBackgrounds: Record<string, BackgroundConfig> = {
	hero: {
		section: 'hero',
		imageUrl: '/e3-background.png',
		gradientOverlay: 'linear-gradient(135deg, rgba(15, 23, 42, 0.9) 0%, rgba(0, 51, 160, 0.85) 100%)',
	},
	carousel: {
		section: 'carousel',
		imageUrl: '/e3-background.png',
		gradientOverlay: 'linear-gradient(135deg, rgba(255, 255, 255, 0.9) 0%, rgba(0, 51, 160, 0.7) 100%)',
    },
	cta: {
		section: 'cta',
		imageUrl: 'https://images.unsplash.com/photo-1504384308090-c894fdcc538d?w=1200&auto=format&fit=crop&q=60',
		gradientOverlay: 'linear-gradient(135deg, rgba(15, 23, 42, 0.92) 0%, rgba(0, 51, 160, 0.85) 100%)',
	},
};
