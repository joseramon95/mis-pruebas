import fs from 'node:fs/promises';
import path from 'node:path';

const LOG_DIR = process.env.VERCEL ? '/tmp/logs' : 'logs';

async function ensureLogDir() {
  try {
    await fs.mkdir(LOG_DIR, { recursive: true });
  } catch {}
}

function getLogFilePath(): string {
  const date = new Date().toISOString().split('T')[0];
  return path.join(LOG_DIR, `${date}.log`);
}

function formatLog(action: string, details: Record<string, unknown>): string {
  const timestamp = new Date().toISOString();
  return `[${timestamp}] ${action} | ${JSON.stringify(details)}\n`;
}

export async function logAction(action: string, details: Record<string, unknown> = {}) {
  ensureLogDir();
  
  const logEntry = formatLog(action, details);
  const logPath = getLogFilePath();
  
  fs.appendFile(logPath, logEntry).catch(() => {});
}

export function createRequestLogger() {
  return async function({ request }: { request: Request }, next: () => Response): Promise<Response> {
    const ip = request.headers.get('x-forwarded-for')?.split(',')[0] 
      || request.headers.get('x-real-ip') 
      || 'unknown';
    const url = new URL(request.url);
    
    await logAction('VISIT', {
      ip,
      method: request.method,
      path: url.pathname,
      userAgent: request.headers.get('user-agent')?.slice(0, 200)
    });
    
    return next();
  };
}
