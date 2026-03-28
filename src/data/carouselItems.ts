// Modelo: Datos del carrusel (patrón MVC)
export interface CarouselItem {
	id: number;
	title: string;
	description: string;
	image: string;
	contact: {
		text: string;
		link: string;
	};
}

export const featureItems: CarouselItem[] = [
	{
		id: 1,
		title: 'Una Disposición Absoluta',
		description: 'El Compromiso del "Heme Aquí". Mientras otros analizan desde la distancia, nosotros nos involucramos en el epicentro del desafío.',
		image: '/persona-no-bg.png',
		contact: {
			text: 'Contactar por WhatsApp',
			link: 'https://wa.me/521234567890'
		}
	},
	{
		id: 2,
		title: 'Ingeniería de Resiliencia',
		description: 'Estructuras Inquebrantables. Diseñamos sistemas que no solo resisten el cambio, sino que se fortalecen.',
		image: '/persona-no-bg.png',
		contact: {
			text: 'Solicitar información',
			link: 'https://wa.me/521234567890'
		}
	},
	{
		id: 3,
		title: 'Rigor Científico y Ética',
		description: 'Fusionamos ciencia económica con visión estratégica responsable.',
		image: '/persona-no-bg.png',
		contact: {
			text: 'Hablar con asesor',
			link: 'https://wa.me/521234567890'
		}
	}
];

