import fs from 'node:fs/promises';
import nodePath from 'node:path';

const LOG_DIR = "logs";
async function ensureLogDir() {
  try {
    await fs.mkdir(LOG_DIR, { recursive: true });
  } catch {
  }
}
function getLogFilePath() {
  const date = (/* @__PURE__ */ new Date()).toISOString().split("T")[0];
  return nodePath.join(LOG_DIR, `${date}.log`);
}
function formatLog(action, details) {
  const timestamp = (/* @__PURE__ */ new Date()).toISOString();
  return `[${timestamp}] ${action} | ${JSON.stringify(details)}
`;
}
async function logAction(action, details = {}) {
  ensureLogDir();
  const logEntry = formatLog(action, details);
  const logPath = getLogFilePath();
  fs.appendFile(logPath, logEntry).catch(() => {
  });
}

export { logAction as l };
