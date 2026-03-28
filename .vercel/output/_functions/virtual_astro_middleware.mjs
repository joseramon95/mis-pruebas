import { a6 as defineMiddleware, af as sequence } from './chunks/sequence_0AmfiE5n.mjs';
import 'piccolore';
import 'clsx';
import { l as logAction } from './chunks/logger_B6yKPYNL.mjs';

const onRequest$1 = defineMiddleware(async (context, next) => {
  const ip = context.request.headers.get("x-forwarded-for")?.split(",")[0] || context.request.headers.get("x-real-ip") || "unknown";
  logAction("VISIT", {
    ip,
    method: context.request.method,
    path: context.url.pathname,
    userAgent: context.request.headers.get("user-agent")?.slice(0, 200)
  });
  return next();
});

const onRequest = sequence(
	
	onRequest$1
	
);

export { onRequest };
