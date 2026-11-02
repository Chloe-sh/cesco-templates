// 시안 HTML을 Edge 헤드리스로 캡처해 captures/<날짜>/ 에 JPEG 썸네일·전체 캡처를 만든다.
// 사용: node scripts/capture_reports.mjs [captures/261102/manifest.json] [--only g01,g02]
// 1) manifest.items 마다 PNG 2장(상단 1280×1600, 전체 1280×5200)을 임시 폴더에 찍고
// 2) scripts/resize_captures.ps1 (System.Drawing)로 JPEG 썸네일(640w)·전체(1000w, 하단 여백 트림)를 만든다.
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import { execFileSync } from 'node:child_process';

const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname.replace(/^\/([A-Za-z]:)/, '$1')), '..');
const args = process.argv.slice(2);
const manifestPath = path.resolve(ROOT, args.find(a => !a.startsWith('--')) || 'captures/261102/manifest.json');
const onlyArg = args.find(a => a.startsWith('--only='));
const only = onlyArg ? new Set(onlyArg.slice(7).split(',')) : null;

const EDGE = ['C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe', 'C:/Program Files/Microsoft/Edge/Application/msedge.exe', 'C:/Program Files/Google/Chrome/Application/chrome.exe'].find(p => fs.existsSync(p));
if (!EDGE) { console.error('Edge/Chrome 실행 파일을 찾지 못했습니다.'); process.exit(1); }

const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
const outDir = path.dirname(manifestPath);
const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'cesco-cap-'));

function shoot(file, w, h, out, hash) {
  const url = 'file:///' + path.resolve(ROOT, file).replace(/\\/g, '/').split('/').map((seg, i) => i === 0 ? seg : encodeURIComponent(seg)).join('/') + (hash ? '#' + hash : '');
  execFileSync(EDGE, [
    '--headless=new', '--disable-gpu', '--hide-scrollbars', '--no-first-run', '--allow-file-access-from-files',
    '--force-device-scale-factor=1', `--window-size=${w},${h}`, '--virtual-time-budget=8000',
    `--screenshot=${out}`, url
  ], { stdio: 'ignore', timeout: 90000 });
  if (!fs.existsSync(out)) throw new Error('캡처 실패: ' + file);
}

let n = 0;
for (const it of manifest.items) {
  if (only && !only.has(it.id)) continue;
  const t0 = Date.now();
  shoot(it.file, 1280, 1600, path.join(tmp, it.id + '_thumb.png'), it.hash);
  shoot(it.file, 1280, 5200, path.join(tmp, it.id + '_full.png'), it.hash);
  n++;
  console.log(`${it.id} ${it.title} (${Date.now() - t0}ms)`);
}
console.log(`PNG ${n}건 → ${tmp}`);

execFileSync('powershell.exe', ['-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', path.join(ROOT, 'scripts', 'resize_captures.ps1'), '-InDir', tmp, '-OutDir', outDir], { stdio: 'inherit' });
fs.rmSync(tmp, { recursive: true, force: true });
console.log('완료:', outDir);
