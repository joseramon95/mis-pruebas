import sharp from 'sharp';
import fs from 'fs';
import path from 'path';

const sourceImage = '../E3.png';
const outputDir = './android/app/src/main/res';

const sizes = [
  { name: 'mipmap-mdpi', size: 48 },
  { name: 'mipmap-hdpi', size: 72 },
  { name: 'mipmap-xhdpi', size: 96 },
  { name: 'mipmap-xxhdpi', size: 144 },
  { name: 'mipmap-xxxhdpi', size: 192 },
];

const sizesForeground = [
  { name: 'mipmap-mdpi', size: 108 },
  { name: 'mipmap-hdpi', size: 162 },
  { name: 'mipmap-xhdpi', size: 216 },
  { name: 'mipmap-xxhdpi', size: 324 },
  { name: 'mipmap-xxxhdpi', size: 432 },
];

async function generateIcons() {
  const image = sharp(sourceImage);
  const metadata = await image.metadata();
  
  console.log(`Source: ${metadata.width}x${metadata.height}`);

  for (const { name, size } of sizes) {
    const dir = path.join(outputDir, name);
    if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
    
    await sharp(sourceImage)
      .resize(size, size)
      .png()
      .toFile(path.join(dir, 'ic_launcher.png'));
    
    await sharp(sourceImage)
      .resize(size, size)
      .png()
      .toFile(path.join(dir, 'ic_launcher_round.png'));
    
    console.log(`Generated ${name}: ${size}x${size}`);
  }

  for (const { name, size } of sizesForeground) {
    const dir = path.join(outputDir, name);
    await sharp(sourceImage)
      .resize(size, size)
      .png()
      .toFile(path.join(dir, 'ic_launcher_foreground.png'));
    console.log(`Generated foreground ${name}: ${size}x${size}`);
  }

  const anydpiDir = path.join(outputDir, 'mipmap-anydpi-v26');
  if (!fs.existsSync(anydpiDir)) fs.mkdirSync(anydpiDir, { recursive: true });

  const adaptiveIconXML = `<?xml version="1.0" encoding="utf-8"?>
<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">
    <background android:drawable="@color/ic_launcher_background"/>
    <foreground android:drawable="@mipmap/ic_launcher_foreground"/>
</adaptive-icon>`;
  
  fs.writeFileSync(path.join(anydpiDir, 'ic_launcher.xml'), adaptiveIconXML);
  fs.writeFileSync(path.join(anydpiDir, 'ic_launcher_round.xml'), adaptiveIconXML);

  const colorsXML = `<?xml version="1.0" encoding="utf-8"?>
<resources>
    <color name="ic_launcher_background">#0F172A</color>
</resources>`;
  
  const valuesDir = path.join(outputDir, 'values');
  if (!fs.existsSync(valuesDir)) fs.mkdirSync(valuesDir, { recursive: true });
  fs.writeFileSync(path.join(valuesDir, 'colors.xml'), colorsXML);

  console.log('Done! Icons generated successfully.');
}

generateIcons().catch(console.error);
