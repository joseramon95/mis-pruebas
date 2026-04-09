import { Capacitor } from '@capacitor/core';

export const config = {
  apiUrl: 'https://e3-admin-api.onrender.com',
  appName: 'E3 Admin'
};

export function isNative(): boolean {
  return Capacitor.isNativePlatform();
}
