// Modelo: Datos del carrusel (patrón MVC)
export interface CarouselItem {
	id: number;
	title: string;
	description: string;
	icon: string;
}

export const featureItems: CarouselItem[] = [
	{
		id: 1,
		title: 'Una Disposición Absoluta',
		description: 'El Compromiso del "Heme Aquí". Mientras otros analizan desde la distancia, nosotros nos involucramos en el epicentro del desafío. Respondemos con disposición inmediata, sabiendo que el tiempo es el recurso más valioso de nuestros clientes.',
		icon: '💪',
	},
	{
		id: 2,
		title: 'Ingeniería de Resiliencia',
		description: 'Estructuras Inquebrantables. Nos especializamos en edificar organizaciones estructuralmente inquebrantables. Mediante el rigor del análisis económico, diseñamos sistemas que no solo resisten el cambio, sino que se fortalecen a través de él.',
		icon: '🏛️',
	},
	{
		id: 3,
		title: 'Rigor Científico y Ética',
		description: 'La Fusión del Rigor Científico y la Ética Inflexible. Fusionamos la ciencia económica con una visión estratégica responsable, garantizando que cada decisión sea técnicamente impecable e éticamente sólida.',
		icon: '⚖️',
	},
];

