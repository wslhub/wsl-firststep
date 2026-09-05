"""Check generated documentation, including the nested-fence regression in #8."""
from __future__ import annotations

import configparser
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urljoin, urlsplit

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
SITE = (ROOT / (sys.argv[1] if len(sys.argv) > 1 else 'site')).resolve()
BASE = 'https://wslhub.com/wsl-firststep/'
errors: list[str] = []
pages = {}

for path in SITE.rglob('*.html'):
    pages[path] = BeautifulSoup(path.read_text(encoding='utf-8'), 'html.parser')

if not pages:
    sys.exit('No generated HTML. Run python -m mkdocs build --strict first.')

for source in sorted((ROOT / 'docs').rglob('*.md')):
    relative = source.relative_to(ROOT / 'docs')
    target = SITE / (relative.with_suffix('') / 'index.html' if relative.name != 'index.md' else relative.with_suffix('.html'))
    soup = pages.get(target)
    if soup is None:
        errors.append(f'Missing generated page: {target}')
        continue
    article = soup.select_one('article.md-content__inner')
    if article is None or len(article.find_all('h1')) != 1:
        errors.append(f'{relative}: expected one article title')
        continue
    if '```' in article.get_text():
        errors.append(f'{relative}: raw code fence is visible')
    if not soup.html or soup.html.get('lang') != 'ko':
        errors.append(f'{relative}: Korean document language missing')
    # Parse examples without executing user-facing commands.
    for language, code in re.findall(r'^```(json|ini)\n(.*?)^```', source.read_text(), re.M | re.S):
        try:
            if language == 'json':
                json.loads(code)
            else:
                config = configparser.ConfigParser(interpolation=None)
                config.read_string(code)
        except (ValueError, configparser.Error) as error:
            errors.append(f'{relative}: invalid {language}: {error}')

links_checked = 0
for path, soup in pages.items():
    relative = path.relative_to(SITE).as_posix()
    page_url = urljoin(BASE, relative[:-10] if relative.endswith('index.html') else relative)
    for tag in soup.select('a[href], img[src], script[src], link[href]'):
        raw = tag.get('href') or tag.get('src')
        url = urlsplit(urljoin(page_url, raw))
        # External URLs are checked separately; this is deterministic and offline.
        if url.netloc != 'wslhub.com' or not url.path.startswith('/wsl-firststep/'):
            continue
        local = SITE / unquote(url.path.removeprefix('/wsl-firststep/'))
        if local.is_dir() or url.path.endswith('/'):
            local /= 'index.html'
        if not local.is_file():
            errors.append(f'{relative}: broken link {raw}')
            continue
        links_checked += 1
        if url.fragment and local.suffix == '.html':
            destination = pages.get(local)
            fragment = unquote(url.fragment)
            if destination is None or destination.find(id=fragment) is None:
                errors.append(f'{relative}: missing anchor {raw}')

ubuntu = pages.get(SITE / 'firststep/ubuntu/index.html')
if ubuntu is None or len(ubuntu.select('article ol li pre code')) < 2:
    errors.append('Ubuntu regression #8: nested list code blocks are not rendered as pre/code')

search = SITE / 'search/search_index.json'
if not search.is_file():
    errors.append('Missing search index')
else:
    locations = {row['location'].split('#')[0] for row in json.loads(search.read_text())['docs']}
    for required in ('firststep/ubuntu/', 'firststep/wslc/', 'advanced/copy-distro/', 'devsetup/multiplexer/'):
        if required not in locations:
            errors.append(f'Missing search entry: {required}')

if errors:
    sys.exit('\n'.join(errors))
print(f'Validated {len(pages)} HTML files and {links_checked} local links/assets; nested fences, examples, and search passed.')
