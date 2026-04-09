import { config } from './config';

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
        credentials: 'include',
        headers: {
          'Accept': 'application/json'
        }
      });

      if (response.redirected && response.url.includes('dashboard')) {
        return { success: true };
      }

      if (response.url.includes('login') && !response.url.includes('dashboard')) {
        return { success: false, error: 'Usuario o contraseña incorrectos' };
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
        credentials: 'include'
      });
      return response.url.includes('dashboard');
    } catch {
      return false;
    }
  }

  async ping(): Promise<boolean> {
    try {
      const controller = new AbortController();
      const timeoutId = setTimeout(() => controller.abort(), 5000);

      const response = await fetch(`${this.baseUrl}/login`, {
        method: 'GET',
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

  async getComponentes(): Promise<any[]> {
    const response = await fetch(`${this.baseUrl}/api/componentes`, {
      credentials: 'include'
    });
    return response.json();
  }
}

export const api = new ApiService();
