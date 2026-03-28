import { logAction } from '../../utils/logger';

export const prerender = false;

export const POST = async ({ request }: { request: Request }) => {
  try {
    const body = await request.json();
    const { action, ...details } = body;
    
    const ip = request.headers.get('x-forwarded-for')?.split(',')[0] 
      || request.headers.get('x-real-ip') 
      || 'unknown';
    
    await logAction(action, { ...details, ip });
    
    return new Response(JSON.stringify({ success: true }), { status: 200 });
  } catch {
    return new Response(JSON.stringify({ error: 'Invalid request' }), { status: 400 });
  }
};
