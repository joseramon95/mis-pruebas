import { defineMiddleware } from 'astro:middleware';
import { logAction } from './utils/logger';

export const onRequest = defineMiddleware(async (context, next) => {
  const ip = context.request.headers.get('x-forwarded-for')?.split(',')[0] 
    || context.request.headers.get('x-real-ip') 
    || 'unknown';
  
  logAction('VISIT', {
    ip,
    method: context.request.method,
    path: context.url.pathname,
    userAgent: context.request.headers.get('user-agent')?.slice(0, 200)
  });
  
  return next();
});
