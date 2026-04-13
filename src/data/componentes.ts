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
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), 8000);
        
        const response = await fetch(`${API_URL}/api/componentes`, {
            signal: controller.signal
        });
        
        clearTimeout(timeoutId);
        
        if (response.ok) {
            return await response.json();
        }
    } catch (error) {
        console.error('Error fetching componentes:', error);
    }
    return [];
}

export async function getComponente(nombre: string): Promise<Componente | null> {
    try {
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), 8000);
        
        const response = await fetch(`${API_URL}/api/componentes/${nombre}`, {
            signal: controller.signal
        });
        
        clearTimeout(timeoutId);
        
        if (response.ok) {
            return await response.json();
        }
    } catch (error) {
        console.error(`Error fetching componente ${nombre}:`, error);
    }
    return null;
}
