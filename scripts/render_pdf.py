"""Render PDF pages to PNGs for visual QA."""
import os, shutil, subprocess, sys
from pathlib import Path

def find_pdftoppm():
    candidates = [shutil.which('pdftoppm')]
    deps = os.environ.get('CODEX_PDF_POPPLER_BIN')
    if deps:
        candidates.append(str(Path(deps) / 'pdftoppm.exe'))
    candidates += [
        r'C:\Users\Administrator\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe',
        r'C:\Users\Administrator\.codex\runtime\poppler\Library\bin\pdftoppm.exe',
    ]
    for item in candidates:
        if item and Path(item).exists() and Path(item).suffix.lower() == '.exe': return item
    raise FileNotFoundError('pdftoppm was not found; install Poppler or set CODEX_PDF_POPPLER_BIN.')

def main():
    if len(sys.argv) not in (3,4):
        raise SystemExit('Usage: render_pdf.py INPUT.pdf OUTPUT_DIR [DPI]')
    src, out = Path(sys.argv[1]), Path(sys.argv[2]); dpi = sys.argv[3] if len(sys.argv)==4 else '150'
    out.mkdir(parents=True, exist_ok=True)
    prefix = out / 'page'
    subprocess.run([find_pdftoppm(), '-png', '-r', dpi, str(src), str(prefix)], check=True)
    print(f'Rendered pages to {out}')

if __name__ == '__main__': main()
