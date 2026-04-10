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

const AUTH_KEY = 'e3_admin_auth';

class ApiService {
  private baseUrl: string;

  constructor() {
    this.baseUrl = config.apiUrl;
  }

  private getAuth(): { username: string; password: string } | null {
    const auth = localStorage.getItem(AUTH_KEY);
    return auth ? JSON.parse(auth) : null;
  }

  private setAuth(username: string, password: string): void {
    localStorage.setItem(AUTH_KEY, JSON.stringify({ username, password }));
  }

  private clearAuth(): void {
    localStorage.removeItem(AUTH_KEY);
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

      if (response.status === 302 || response.redirected) {
        const redirectedUrl = response.url || response.redirected?.toString();
        if (redirectedUrl.includes('dashboard')) {
          this.setAuth(username, password);
          return { success: true };
        }
      }

      if (response.url.includes('login')) {
        return { success: false, error: 'Usuario o contraseña incorrectos' };
      }

      return { success: true };
    } catch (error) {
      console.error('Login error:', error);
      return { success: false, error: 'Error de conexión. Verifica tu internet.' };
    }
  }

  async logout(): Promise<void> {
    try {
      await fetch(`${this.baseUrl}/logout`, {
        method: 'GET',
        credentials: 'include'
      });
    } catch (e) {
      console.error('Logout error:', e);
    }
    this.clearAuth();
  }

  async checkAuth(): Promise<boolean> {
    const auth = this.getAuth();
    if (!auth) return false;

    try {
      const formData = new FormData();
      formData.append('username', auth.username);
      formData.append('password', auth.password);

      const response = await fetch(`${this.baseUrl}/login`, {
        method: 'POST',
        body: formData,
        credentials: 'include'
      });

      if (response.status === 302 || response.redirected) {
        const redirectedUrl = response.url || response.redirected?.toString();
        return redirectedUrl.includes('dashboard');
      }
      return false;
    } catch {
      return false;
    }
  }

  private getAuthHeaders(): HeadersInit {
    const auth = this.getAuth();
    if (auth) {
      const encoded = btoa(`${auth.username}:${auth.password}`);
      return { 'Authorization': `Basic ${encoded}` };
    }
    return {};
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
      credentials: 'include',
      headers: this.getAuthHeaders()
    });
    return response.json();
  }

  async getAllSocios(): Promise<any[]> {
    const response = await fetch(`${this.baseUrl}/api/socios/all`, {
      credentials: 'include',
      headers: this.getAuthHeaders()
    });
    if (!response.ok) throw new Error('Error al obtener socios');
    return response.json();
  }

  async createSocio(socio: Socio): Promise<{ success: boolean; id?: number; error?: string }> {
    try {
      const response = await fetch(`${this.baseUrl}/api/socios`, {
        method: 'POST',
        headers: { 
          'Content-Type': 'application/json',
          ...this.getAuthHeaders()
        },
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
        headers: { 
          'Content-Type': 'application/json',
          ...this.getAuthHeaders()
        },
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
        credentials: 'include',
        headers: this.getAuthHeaders()
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
        credentials: 'include',
        headers: this.getAuthHeaders()
      });
      return response.json();
    } catch (error) {
      return { success: false, error: 'Error de conexión' };
    }
  }

  async getComponentes(): Promise<any[]> {
    const response = await fetch(`${this.baseUrl}/api/componentes`, {
      credentials: 'include',
      headers: this.getAuthHeaders()
    });
    return response.json();
  }
}

export const api = new ApiService();
