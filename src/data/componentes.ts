export interface Componente {
    nombre: string;
    titulo: string;
    subtitulo: string;
    contenido: string;
    link: string;
    extra_data: string;
}

const API_URL = import.meta.env.PUBLIC_API_URL || 'https://e3-admin-api.onrender.com';

export async function fetchComponentes(): Promise<Componente[]> {
    try {
        const response = await fetch(`${API_URL}/api/componentes`);
        if (response.ok) {
            return await response.json();
        }
    } catch (error) {
        console.error('Error fetching componentes:', error);
    }
    return [];
}

export async function getComponente(nombre: string): Promise<Componente | null> {
    const componentes = await fetchComponentes();
    return componentes.find(c => c.nombre === nombre) || null;
}
