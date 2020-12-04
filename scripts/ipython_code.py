# coding: utf-8
import requests
url = 'https://issuu.com/shannonmedia/docs/chmissuujulyaug/144'
r = requests.get(url)
r.text
u2 = 'http://search.issuu.com/api/2_0/document?q=jamie'
r = requests.get(u2)
r.status_code
j = r.json()
len(j)
j.keys()
jr = j['response']
len(jr)
jr.keys()
jr['numFound']
u3 = 'http://search.issuu.com/api/2_0/document?q=laura%20zolman%kirk'
fr = requests.get(u3)
results = fr.json()['response']
results.keys()
results['numFound']
results
r4 = requests.get('http://search.issuu.com/api/2_0/page?q=laura%20zolman%kirk').json()['response']
r4 = requests.get('http://search.issuu.com/api/2_0/page?q=username:shannonmedia').json()['response']
r4 = requests.get('http://search.issuu.com/api/2_0/document?q=username:shannonmedia').json()['response']
r4['numFound']
r4
r4 = requests.get('http://search.issuu.com/api/2_0/document?q=username:shannonmedia&pageSize=150').json()['response']
len(r4['docs'])
r5 = requests.get('http://search.issuu.com/api/2_0/document?q=username:shannonmedia&pageSize=550').json()['response']
len(r5['docs'])
r5 = requests.get('http://search.issuu.com/api/2_0/document?q=username:shannonmedia&startIndex=10').json()['response']
r5
all_docs = []
for i in range(0, 150, 10):
    print(i)

from time import sleep
for i in range(0, 150, 10):
    r = requests.get(f'http://search.issuu.com/api/2_0/document?q=username:shannonmedia&startIndex={i}').json()['response']['docs']
    all_docs += r
    sleep(1)
    print(i)

len(all_docs)
all_docs
r6 = requests.get('http://search.issuu.com/api/2_0/page?q=laura:&documentId=170127164139-5e5dbc04d6108d7a2ea48e3b98aa7dba').json()['response']
r6
r6 = requests.get('http://search.issuu.com/api/2_0/page?q=laura%20zolman:&documentId=170127164139-5e5dbc04d6108d7a2ea48e3b98aa7dba').json()['response']
r6
id2name = {d['documentId']:d['docname'] for d in all_docs}
id2name['170127164139-5e5dbc04d6108d7a2ea48e3b98aa7dba']
all_urls = []
for i, (d_id, d_name) in enumerate(id2name):
    r = requests.get(f'http://search.issuu.com/api/2_0/page?q=laura%20zolman:&documentId={d_id}').json()['response']
    for p in r['docs']:
        n = p['pageId']
        all_urls.append(f'https://issuu.com/shannonmedia/docs/{d_name}/{n}')
    print(i, len(all_urls))

for i, (d_id, d_name) in enumerate(id2name.items()):
    r = requests.get(f'http://search.issuu.com/api/2_0/page?q=laura%20zolman:&documentId={d_id}').json()['response']
    for p in r['docs']:
        n = p['pageId']
        all_urls.append(f'https://issuu.com/shannonmedia/docs/{d_name}/{n}')
    print(i, len(all_urls))
all_urls
for l in all_urls:
    if l.endswith('/4'):
        print(l)

for l in all_urls:
    if not l.endswith('/4'):
        print(l)

all_urls[0]
import urllib
urllib.parse.urlencode(all_urls[0])
urllib.parse.quote_plus(all_urls[0])
encoded = [urllib.parse.quote_plus(x) for x in all_urls]
encoded[0]
r = requests.get(f'https://issuu.com/oembed?url={encoded[0]}&iframe=true').json()
r
embeded = []requests.get(f'https://issuu.com/oembed?url={encoded[0]}&iframe=true').json()
embeded = []
for i, e in enumerate(encoded):
    embeded.append(requests.get(f'https://issuu.com/oembed?url={e}&iframe=true').json())
    print(i)

len(encoded)
len(all_urls)
len(set(all_urls))
all_urls
embeded[0]
len(set(e['html'] for e in embeded))
for x in set(e['html'] for e in embeded):
    print(x['html'])

for x in set(e['html'] for e in embeded):
    print(x)

len(all_urls)
len(embeded)
from collections import defaultdict
embeded_2_all_urls_grouped = defaultdict(list)
for full_url, iframe in zip(all_urls, embeded):
    embeded_2_all_urls_grouped.append(full_url)

for full_url, iframe in zip(all_urls, embeded):
    embeded_2_all_urls_grouped[iframe].append(full_url)

for full_url, iframe in zip(all_urls, embeded):
    embeded_2_all_urls_grouped[iframe['html']].append(full_url)


len(embeded_2_all_urls_grouped)
for full_url, iframes in embeded_2_all_urls_grouped.items():
    print(full_url, '/'.join(i for i in iframes))

for iframe, full_urls in embeded_2_all_urls_grouped.items():
    pages = [i.split('/')[-1] for i in full_urls]
    pages = [p for p in pages if p != '4']
    pages_s = ', '.join(p for p in pages)
    if not pages: continue
    s = f'{iframe}\nCheck out my work on page {pages_s}.'
    if len(pages) > 1:
        s = s.replace('page', 'pages')
        idx = s.rindex(' ')
        if len(pages) == 2:
            s = s[:idx-1] + ' and' + s[idx:]
        else:
            s = s[:idx] + ' and' + s[idx:]
    print(s, sep=',', file=open('dump.txt', 'a'))
    print(s, sep=',')

import pandas as pd
df = pd.read_csv('/Users/jessime.kirk/Downloads/Writing Portfolio - Sheet1.tsv')
df = pd.read_csv('/Users/jessime.kirk/Downloads/Writing Portfolio - Sheet1.tsv', sep='\t')
df.head()
get_ipython().run_line_magic('save', '/Users/jessime.kirk/Code/me/laura_website2/ipython_code.txt')
get_ipython().run_line_magic('save', '/Users/jessime.kirk/Code/me/laura_website2/ipython_code.txt 1-106')
from pathlib import Path
get_ipython().run_line_magic('pwd', '')
template = Path('_posts/template.md').read_text()
template
ex = df.loc[0]
ex
# d = {'title': ex['Title'], 'magazine': ex['Magazine'],
def make_tags(row):
    base = '  - {}\n'
    tags = row['Tags'].split(', ')
    tags += [row['Type of Edit'], row['Writer/Editor'], row['Editorial/Marketing']]
    tags = base.join(tags)
    return tags

make_tags(ex)
def make_tags(row):
    base = '  - {}\n'
    tags = row['Tags'].split(', ')
    tags += [row['Type of Edit'], row['Writer/Editor'], row['Editorial/Marketing']]
    tags = ''.join(base.format(t) for t in tags)
    return tags

make_tags(ex)
print(make_tags(ex))
d = {'title': ex['Title'], 'magazine': ex['Magazine'], 'tags': make_tags(ex), 'link': ex['Link']}
d
get_ipython().run_line_magic('pwd', '')
outpath = '{}_{}'.format(ex['Date'], ex['Title'].replace(' ', '_'))
outpath
Path(outpath).write_text(template.format(**d))
outpath = '_posts/{}_{}'.format(ex['Date'], ex['Title'].replace(' ', '_'))
outpath
for i, row in df.iterrows():
    d = {'title': row['Title'], 'magazine': row['Magazine'], 'tags': make_tags(row), 'link': row['Link']}
    break

template = Path('_posts/template.md').read_text()


make_tags(row)

Path('template.md').write_text()
Path('template.md').write_text(template)
for i, row in df.iterrows():
    if pd.isnull(row['Date']): continue
    d = {'title': row['Title'], 'magazine': row['Magazine'], 'tags': make_tags(row), 'link': row['Link']}
    outpath = '_posts/{}-{}.md'.format(row['Date'], row['Title'].replace(' ', '_').replace('/', '_'))
    Path(outpath).write_text(template.format(**d))
    if i == 10:
        break

i
type(i)
for i, row in df.iterrows():
    print(i)
    if i > 10:
        break

for i, row in df.iterrows():
    if pd.isnull(row['Date']): continue
    d = {'title': row['Title'], 'magazine': row['Magazine'], 'tags': make_tags(row), 'link': row['Link']}
    outpath = '_posts/{}-{}.md'.format(row['Date'], row['Title'].replace(' ', '_').replace('/', '_'))
    Path(outpath).write_text(template.format(**d))
    if i >= 10:
        break
    else:
        print(i)

template
template = Path('template.md').read_text()

for i, row in df.iterrows():
    if pd.isnull(row['Date']): continue
    d = {'title': row['Title'].replace(':', '-'), 'magazine': row['Magazine'], 'tags': make_tags(row), 'link': row['Link']}
    outpath = '_posts/{}-{}.md'.format(row['Date'], row['Title'].replace(' ', '_').replace('/', '_'))
    Path(outpath).write_text(template.format(**d))

get_ipython().run_line_magic('save', '/Users/jessime.kirk/Code/me/laura_website2/scripts/ipython_code.py 1-157')
