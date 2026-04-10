import { config } from './config';

export interface Socio {
  id?: number;
  nombre: string;
  descripcion: string;
  imagen: string;
  whatsapp: string;
  activo: boolean;
  orden: number;
}

export interface LoginResponse {
  success: boolean;
  error?: string;
}

export interface ApiError {
  message: string;
}

class ApiService {
  private baseUrl: string;

  constructor() {
    this.baseUrl = config.apiUrl;
  }

  async login(username: string, password: string): Promise<LoginResponse> {
    try {
      const formData = new FormData();
      formData.append('username', username);
      formData.append('password', password);

      const response = await fetch(`${this.baseUrl}/login`, {
        method: 'POST',
        body: formData,
        credentials: 'include'
      });

      if (response.status === 302) {
        const redirectedUrl = response.url;
        if (redirectedUrl.includes('dashboard')) {
          return { success: true };
        }
      }

      if (response.url.includes('login') && !response.url.includes('dashboard')) {
        return { success: false, error: 'Usuario o contraseña incorrectos' };
      }

      if (response.redirected) {
        return { success: true };
      }

      return { success: true };
    } catch (error) {
      console.error('Login error:', error);
      return { success: false, error: 'Error de conexión. Verifica tu internet.' };
    }
  }

  async logout(): Promise<void> {
    await fetch(`${this.baseUrl}/logout`, {
      method: 'GET',
      credentials: 'include'
    });
  }

  async checkAuth(): Promise<boolean> {
    try {
      const response = await fetch(`${this.baseUrl}/dashboard`, {
        credentials: 'include',
        redirect: 'follow'
      });
      return response.url.includes('dashboard') || response.status === 200;
    } catch {
      return false;
    }
  }

  async ping(): Promise<boolean> {
    try {
      const controller = new AbortController();
      const timeoutId = setTimeout(() => controller.abort(), 5000);

      const response = await fetch(`${this.baseUrl}/health`, {
        signal: controller.signal
      });

      clearTimeout(timeoutId);
      return response.ok;
    } catch {
      return false;
    }
  }

  async getSocios(): Promise<any[]> {
    const response = await fetch(`${this.baseUrl}/api/socios`, {
      credentials: 'include'
    });
    return response.json();
  }

  async getAllSocios(): Promise<any[]> {
    const response = await fetch(`${this.baseUrl}/api/socios/all`, {
      credentials: 'include'
    });
    if (!response.ok) throw new Error('Error al obtener socios');
    return response.json();
  }

  async createSocio(socio: Socio): Promise<{ success: boolean; id?: number; error?: string }> {
    try {
      const response = await fetch(`${this.baseUrl}/api/socios`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include',
        body: JSON.stringify(socio)
      });
      return response.json();
    } catch (error) {
      return { success: false, error: 'Error de conexión' };
    }
  }

  async updateSocio(id: number, socio: Socio): Promise<{ success: boolean; error?: string }> {
    try {
      const response = await fetch(`${this.baseUrl}/api/socios/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include',
        body: JSON.stringify(socio)
      });
      return response.json();
    } catch (error) {
      return { success: false, error: 'Error de conexión' };
    }
  }

  async deleteSocio(id: number): Promise<{ success: boolean; error?: string }> {
    try {
      const response = await fetch(`${this.baseUrl}/api/socios/${id}`, {
        method: 'DELETE',
        credentials: 'include'
      });
      return response.json();
    } catch (error) {
      return { success: false, error: 'Error de conexión' };
    }
  }

  async toggleSocio(id: number): Promise<{ success: boolean; activo?: boolean; error?: string }> {
    try {
      const response = await fetch(`${this.baseUrl}/api/socios/${id}/toggle`, {
        method: 'POST',
        credentials: 'include'
      });
      return response.json();
    } catch (error) {
      return { success: false, error: 'Error de conexión' };
    }
  }

  async getComponentes(): Promise<any[]> {
    const response = await fetch(`${this.baseUrl}/api/componentes`, {
      credentials: 'include'
    });
    return response.json();
  }
}

export const api = new ApiService();
