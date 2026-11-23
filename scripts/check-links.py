from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import xml.etree.ElementTree as ET
root=Path('dist'); count=0; errors=[]
class Page(HTMLParser):
 def __init__(self,text):
  super().__init__();self.links=[];self.ids=set();self.headings=0;self.feed(text)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.add(a['id'])
  if tag=='h1':self.headings+=1
  for key in ['href','src']:
   if key in a:self.links.append(a[key])
pages={p:Page(p.read_text()) for p in root.rglob('*.html') if not p.name.startswith('__')}
for p,doc in pages.items():
 if doc.headings!=1: errors.append(f'{p}: {doc.headings} h1s')
 for link in doc.links:
  u=urlsplit(link)
  if u.scheme or u.netloc:continue
  dest=root/unquote(u.path).lstrip('/') if u.path.startswith('/') else p.parent/unquote(u.path)
  if not u.path:dest=p
  if dest.is_dir():dest=dest/'index.html'
  elif not dest.exists() and not dest.suffix:dest=dest/'index.html'
  count+=1
  if not dest.exists():errors.append(f'{p}: missing {link}')
  elif u.fragment and dest in pages and unquote(u.fragment) not in pages[dest].ids:errors.append(f'{p}: missing anchor {link}')
 for sample in ['Lorem ipsum','Your Company Name','markhorn.dev@gmail.com','Project One','StreamlineFS']:
  if sample in p.read_text():errors.append(f'{p}: sample {sample}')
for item in ET.parse(root/'rss.xml').findall('.//item'):
 u=urlsplit(item.findtext('link'));dest=root/u.path.strip('/')/'index.html'
 assert dest.exists(), f'RSS missing {dest}'
assert not errors, '\n'.join(errors)
print(f'PASS: {len(pages)} HTML pages, {count} local links/assets, RSS item destinations and sample-content scan')
