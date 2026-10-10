#!/usr/bin/env python3
"""Package only public HTML and its local dependencies for GitHub Pages."""
import json
import shutil
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
DEST = ROOT / 'dist'
PUBLIC_TYPES = {'.html', '.css', '.js', '.svg', '.png', '.jpg', '.jpeg', '.webp', '.avif', '.ico', '.woff', '.woff2'}
PUBLIC_TEXT = {'COURSE_SYLLABUS_AND_TIMESTAMPS.txt'}


class Dependencies(HTMLParser):
    def __init__(self):
        super().__init__()
        self.paths = set()

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key not in {'src', 'href', 'poster'} or not value:
                continue
            url = urlsplit(value)
            if not url.scheme and not url.netloc and url.path:
                if url.path.startswith('/'):
                    raise ValueError(f'Use a relative site URL: {value}')
                self.paths.add(unquote(url.path))


def collect(path, found):
    if path.is_symlink():
        raise ValueError(f'Deployment dependencies must not be symlinks: {path}')
    source = path.resolve()
    relative = source.relative_to(ROOT)
    if source in found:
        return
    if any(part.startswith('.') for part in relative.parts):
        raise ValueError(f'Private directory referenced by a public page: {relative}')
    if source.suffix.lower() not in PUBLIC_TYPES and source.name not in PUBLIC_TEXT:
        raise ValueError(f'Working material or unsupported dependency: {relative}')
    if not source.is_file():
        raise FileNotFoundError(f'Missing public dependency: {relative}')
    found.add(source)
    if source.suffix == '.html':
        parser = Dependencies()
        parser.feed(source.read_text())
        for reference in sorted(parser.paths):
            collect(source.parent / reference, found)


def build():
    # Resolve and validate everything before replacing the previous build.
    found = set()
    collect(ROOT / 'index.html', found)
    for video in json.loads((ROOT / 'videos.json').read_text()):
        collect(ROOT / video['folder'] / video['page'], found)
    if DEST.exists():
        if DEST.is_symlink():
            raise ValueError('Refusing to replace a symlink at dist/')
        shutil.rmtree(DEST)
    DEST.mkdir()
    for source in sorted(found):
        target = DEST / source.relative_to(ROOT)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
    (DEST / '.nojekyll').touch()
    print(f'Packaged {len(found)} public files in dist/. Working inputs are excluded.')


if __name__ == '__main__':
    build()
