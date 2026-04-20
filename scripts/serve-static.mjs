import { createServer } from 'node:http';
import { promises as fs } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT_DIR = path.resolve(__dirname, '..');
const DEFAULT_HOST = process.env.PAPERREADER_HOST || '127.0.0.1';
const DEFAULT_PORT = Number(process.env.PORT || process.argv[2] || 8000);

const MIME_TYPES = new Map([
  ['.css', 'text/css; charset=utf-8'],
  ['.html', 'text/html; charset=utf-8'],
  ['.js', 'text/javascript; charset=utf-8'],
  ['.json', 'application/json; charset=utf-8'],
  ['.md', 'text/markdown; charset=utf-8'],
  ['.pdf', 'application/pdf'],
  ['.png', 'image/png'],
  ['.jpg', 'image/jpeg'],
  ['.jpeg', 'image/jpeg'],
  ['.svg', 'image/svg+xml; charset=utf-8'],
  ['.txt', 'text/plain; charset=utf-8']
]);

function safeDecodePathname(pathname) {
  try {
    return decodeURIComponent(pathname);
  } catch {
    return null;
  }
}

function resolveRequestPath(urlPathname) {
  const decodedPath = safeDecodePathname(urlPathname);
  if (!decodedPath) {
    return null;
  }

  const relativePath = decodedPath === '/' ? 'index.html' : decodedPath.replace(/^\/+/, '');
  const absolutePath = path.resolve(ROOT_DIR, relativePath);

  if (!absolutePath.startsWith(ROOT_DIR)) {
    return null;
  }

  return absolutePath;
}

async function serveFile(response, filePath) {
  try {
    const stats = await fs.stat(filePath);

    if (stats.isDirectory()) {
      return serveFile(response, path.join(filePath, 'index.html'));
    }

    const extension = path.extname(filePath).toLowerCase();
    const contentType = MIME_TYPES.get(extension) || 'application/octet-stream';
    const content = await fs.readFile(filePath);

    response.writeHead(200, {
      'Cache-Control': 'no-cache',
      'Content-Length': content.length,
      'Content-Type': contentType
    });
    response.end(content);
  } catch (error) {
    if (error && typeof error === 'object' && 'code' in error && error.code === 'ENOENT') {
      response.writeHead(404, { 'Content-Type': 'text/plain; charset=utf-8' });
      response.end('404 Not Found');
      return;
    }

    response.writeHead(500, { 'Content-Type': 'text/plain; charset=utf-8' });
    response.end('500 Internal Server Error');
  }
}

const server = createServer(async (request, response) => {
  const requestUrl = new URL(request.url || '/', `http://${request.headers.host || 'localhost'}`);
  const targetPath = resolveRequestPath(requestUrl.pathname);

  if (!targetPath) {
    response.writeHead(400, { 'Content-Type': 'text/plain; charset=utf-8' });
    response.end('400 Bad Request');
    return;
  }

  await serveFile(response, targetPath);
});

server.listen(DEFAULT_PORT, DEFAULT_HOST, () => {
  console.log(`PaperReader available at http://${DEFAULT_HOST}:${DEFAULT_PORT}`);
  console.log(`Serving static files from ${ROOT_DIR}`);
});
