import { api } from './api';
import { config } from './config';

const MAX_WAIT_TIME = 60000;
const RETRY_INTERVAL = 5000;

export class App {
  private container: HTMLElement;

  constructor() {
    this.container = document.getElementById('app')!;
    this.init();
  }

  private async init() {
    await this.waitForApi();
    const isAuthenticated = await api.checkAuth();
    if (isAuthenticated) {
      this.showDashboard();
    } else {
      this.showLogin();
    }
  }

  private async waitForApi(): Promise<void> {
    this.showApiLoading();

    const startTime = Date.now();
    let attempts = 0;

    while (Date.now() - startTime < MAX_WAIT_TIME) {
      attempts++;
      this.updateApiLoadingProgress(attempts, Math.min((Date.now() - startTime) / 1000, MAX_WAIT_TIME / 1000));

      const isOnline = await api.ping();

      if (isOnline) {
        this.hideApiLoading();
        return;
      }

      await this.sleep(RETRY_INTERVAL);
    }

    this.showApiError('La API no está disponible. Verifica tu conexión.');
  }

  private showApiLoading() {
    this.container.innerHTML = `
      <div class="api-loading">
        <div class="loading-spinner"></div>
        <h2>Conectando con el servidor</h2>
        <p id="loadingStatus">Iniciando...</p>
        <div class="progress-bar">
          <div class="progress-fill" id="progressFill"></div>
        </div>
        <p class="loading-hint">Esto puede tardar si el servidor está despertando</p>
      </div>
    `;
  }

  private updateApiLoadingProgress(attempt: number, seconds: number) {
    const status = document.getElementById('loadingStatus');
    const progress = document.getElementById('progressFill');
    if (status) status.textContent = `Intentando conexión... (${attempt})`;
    if (progress) progress.style.width = `${Math.min((seconds / 120) * 100, 100)}%`;
  }

  private hideApiLoading() {
    const loading = this.container.querySelector('.api-loading');
    if (loading) loading.remove();
  }

  private showApiError(message: string) {
    this.container.innerHTML = `
      <div class="api-error">
        <div class="error-icon">!</div>
        <h2>Error de conexión</h2>
        <p>${message}</p>
        <button id="retryBtn">Reintentar</button>
      </div>
    `;

    document.getElementById('retryBtn')?.addEventListener('click', () => {
      this.init();
    });
  }

  private sleep(ms: number): Promise<void> {
    return new Promise(resolve => setTimeout(resolve, ms));
  }

  showLogin(error?: string) {
    this.container.innerHTML = `
      <div class="login-container">
        <div class="login-card">
          <h1>${config.appName}</h1>
          <form id="loginForm">
            <div class="form-group">
              <label for="username">Usuario</label>
              <input type="text" id="username" name="username" required autocomplete="username">
            </div>
            <div class="form-group">
              <label for="password">Contraseña</label>
              <input type="password" id="password" name="password" required autocomplete="current-password">
            </div>
            ${error ? `<p class="error">${error}</p>` : ''}
            <button type="submit" id="loginBtn">Iniciar Sesión</button>
          </form>
          <p class="powered">Conectado a: ${config.apiUrl}</p>
        </div>
      </div>
    `;

    document.getElementById('loginForm')?.addEventListener('submit', async (e) => {
      e.preventDefault();
      const btn = document.getElementById('loginBtn') as HTMLButtonElement;
      btn.disabled = true;
      btn.textContent = 'Cargando...';

      const username = (document.getElementById('username') as HTMLInputElement).value;
      const password = (document.getElementById('password') as HTMLInputElement).value;

      const result = await api.login(username, password);
      if (result.success) {
        this.showDashboard();
      } else {
        this.showLogin(result.error);
      }
    });
  }

  async showDashboard() {
    this.container.innerHTML = `
      <div class="dashboard">
        <header>
          <h1>${config.appName}</h1>
          <button id="logoutBtn">Cerrar Sesión</button>
        </header>
        <main>
          <div class="loading">Cargando datos...</div>
        </main>
      </div>
    `;

    document.getElementById('logoutBtn')?.addEventListener('click', async () => {
      await api.logout();
      this.showLogin();
    });

    try {
      const [socios, componentes] = await Promise.all([
        api.getSocios(),
        api.getComponentes()
      ]);
      this.renderDashboard(socios, componentes);
    } catch (error) {
      this.container.innerHTML = `
        <div class="dashboard">
          <header>
            <h1>${config.appName}</h1>
            <button id="logoutBtn">Cerrar Sesión</button>
          </header>
          <main>
            <p class="error">Error al cargar datos</p>
          </main>
        </div>
      `;
      document.getElementById('logoutBtn')?.addEventListener('click', async () => {
        await api.logout();
        this.showLogin();
      });
    }
  }

  private renderDashboard(socios: any[], componentes: any[]) {
    const main = this.container.querySelector('main')!;
    main.innerHTML = `
      <div class="stats">
        <div class="stat-card">
          <span class="stat-number">${socios.length}</span>
          <span class="stat-label">Socios</span>
        </div>
        <div class="stat-card">
          <span class="stat-number">${componentes.length}</span>
          <span class="stat-label">Componentes</span>
        </div>
      </div>
      
      <section class="section">
        <h2>Socios</h2>
        <div class="list">
          ${socios.length ? socios.map(s => `
            <div class="item">
              <div class="item-info">
                <strong>${s.title}</strong>
                <span>${s.description || 'Sin descripción'}</span>
              </div>
              ${s.contact?.link ? `<a href="${s.contact.link}" target="_blank" class="btn-whatsapp">WhatsApp</a>` : ''}
            </div>
          `).join('') : '<p>No hay socios registrados</p>'}
        </div>
      </section>

      <section class="section">
        <h2>Componentes</h2>
        <div class="list">
          ${componentes.map(c => `
            <div class="item">
              <div class="item-info">
                <strong>${c.nombre}</strong>
                <span>${c.titulo || 'Sin título'}</span>
              </div>
            </div>
          `).join('')}
        </div>
      </section>
    `;
  }
}

new App();
