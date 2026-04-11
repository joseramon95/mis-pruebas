export interface CasoExito {
    id: number;
    slug: string;
    titulo: string;
    descripcion: string;
    imagen: string;
    testimonio: {
        autor: string;
        cargo: string;
        texto: string;
    } | null;
}

export interface SolucionesData {
    titulo: string;
    subtitulo: string;
    casos: CasoExito[];
}

export interface CasoDetalle extends CasoExito {
    contenido: string;
    resultados: string[];
}
