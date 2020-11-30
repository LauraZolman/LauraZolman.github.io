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
    
s = """0 0
1 1
2 1
3 8
4 8
5 8
6 15
7 18
8 18
9 18
10 19
11 19
12 19
13 25
14 25
15 31
16 33
17 33
18 41
19 41
20 41
21 41
22 41
23 41
24 46
25 46
26 47
27 47
28 47
29 47
30 47
31 47
32 47
33 47
34 48
35 48
36 50
37 55
38 63
39 63
40 63
41 63
42 63
43 63
44 63
45 63
46 63
47 65
48 65
49 65
50 65
51 65
52 65
53 65
54 65
55 65
56 65
57 65
58 74
59 74
60 74
61 74
62 74
63 74
64 74
65 74
66 77
67 80
68 80
69 80
70 80
71 82
72 82
73 91
74 91
75 91
76 91
77 91
78 91
79 91
80 91
81 91
82 94
83 94
84 104
85 104
86 104
87 104
88 104
89 108
90 110
91 110
92 110
93 111
94 114
95 119
96 123
97 125
98 125
99 125
100 127
101 131
102 134
103 134
104 134
105 134
106 136
107 145
108 146
109 146
110 146
111 146
112 146
113 153
114 153
115 156
116 156
117 166
118 166
119 166
120 166
121 166
122 166
123 166
124 166
125 166
126 167
127 167
128 167
129 167
130 167
131 167
132 167
133 167
134 167
135 169
136 169
137 169
138 171
139 173
140 173
141 173
142 173
143 177
144 177
145 177
146 177
147 177
148 177"""
lines = s.splitlines()
len(lines)
set(x.split()[1] for x in lines)
len(set(x.split()[1] for x in lines))
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
    print(iframe, '/'.join(i.split('/')[-1] for i in iframes))
    
for iframe, full_urls in embeded_2_all_urls_grouped.items():
    print(iframe, '/'.join(i.split('/')[-1] for i in full_urls))
    
for iframe, full_urls in embeded_2_all_urls_grouped.items():
    print(iframe, '/'.join(i.split('/')[-1] for i in full_urls), sep=',')
    
for iframe, full_urls in embeded_2_all_urls_grouped.items():
    print(f'{iframe\n Check out my work on page(s) {','.join(i.split('/')[-1] for i in full_urls)}.', sep=',')
    break
    
for iframe, full_urls in embeded_2_all_urls_grouped.items():
    print(f'{iframe}\n Check out my work on page(s) {','.join(i.split('/')[-1] for i in full_urls)}.', sep=',')
    break
    
for iframe, full_urls in embeded_2_all_urls_grouped.items():
    pages = ','.join(i.split('/')[-1] for i in full_urls)
    print(f'{iframe}\n Check out my work on page(s) {pages}.', sep=',')
    break
    
for iframe, full_urls in embeded_2_all_urls_grouped.items():
    pages = ','.join(i.split('/')[-1] for i in full_urls)
    print(f'{iframe}\nCheck out my work on page(s) {pages}.', sep=',')
    
get_ipython().run_line_magic('pwd', '')
get_ipython().run_line_magic('cd', '~/Code/me/laura_website2/')
for iframe, full_urls in embeded_2_all_urls_grouped.items():
    pages = ','.join(i.split('/')[-1] for i in full_urls)
    print(f'{iframe}\nCheck out my work on page(s) {pages}.', sep=',', file=open('dump.txt', 'a'))
    
for iframe, full_urls in embeded_2_all_urls_grouped.items():
    pages = ', '.join(i.split('/')[-1] for i in full_urls)
    print(f'{iframe}\nCheck out my work on page(s) {pages}.', sep=',', file=open('dump.txt', 'a'))
    
for iframe, full_urls in embeded_2_all_urls_grouped.items():
    pages = ', '.join(i.split('/')[-1] for i in full_urls)
    print(f'{iframe}\nCheck out my work on page(s) {pages}.', sep=',', file=open('dump.txt', 'a'))
    
for iframe, full_urls in embeded_2_all_urls_grouped.items():
    pages = ', '.join(i.split('/')[-1] for i in full_urls)
    if pages == '4': continue
    print(f'{iframe}\nCheck out my work on page(s) {pages}.', sep=',', file=open('dump.txt', 'a'))
    
for iframe, full_urls in embeded_2_all_urls_grouped.items():
    pages = ', '.join(i.split('/')[-1] for i in full_urls)
    if pages == '4': continue
    print(f'{iframe}\nCheck out my work on page(s) {pages}.', sep=',', file=open('dump.txt', 'a'))
    
for iframe, full_urls in embeded_2_all_urls_grouped.items():
    pages = [i.split('/')[-1] for i in full_urls]
    pages = ', '.join(p for p in pages if p != '4')
    if not pages: continue
    print(f'{iframe}\nCheck out my work on page(s) {pages}.', sep=',', file=open('dump.txt', 'a'))
    
for iframe, full_urls in embeded_2_all_urls_grouped.items():
    pages = [i.split('/')[-1] for i in full_urls]
    pages = ', '.join(p for p in pages if p != '4')
    if not pages: continue
    s = f'{iframe}\nCheck out my work on page {pages}.'
    if len(pages) > 1:
        s = s.replace('page', 'pages')
        idx = s.rindex(' ')
        if len(pages) == 2:
            s = s[:idx-1] + ' and' + s[idx:]
        else
            s = s[:idx] + ' and' + s[idx:]
    print(s, sep=',', file=open('dump.txt', 'a'))
    
for iframe, full_urls in embeded_2_all_urls_grouped.items():
    pages = [i.split('/')[-1] for i in full_urls]
    pages = ', '.join(p for p in pages if p != '4')
    if not pages: continue
    s = f'{iframe}\nCheck out my work on page {pages}.'
    if len(pages) > 1:
        s = s.replace('page', 'pages')
        idx = s.rindex(' ')
        if len(pages) == 2:
            s = s[:idx-1] + ' and' + s[idx:]
        else:
            s = s[:idx] + ' and' + s[idx:]
    print(s, sep=',', file=open('dump.txt', 'a'))
    
for iframe, full_urls in embeded_2_all_urls_grouped.items():
    pages = [i.split('/')[-1] for i in full_urls]
    pages = ', '.join(p for p in pages if p != '4')
    if not pages: continue
    s = f'{iframe}\nCheck out my work on page {pages}.'
    if len(pages) > 1:
        s = s.replace('page', 'pages')
        idx = s.rindex(' ')
        if len(pages) == 2:
            s = s[:idx-1] + ' and' + s[idx:]
        else:
            s = s[:idx] + ' and' + s[idx:]
    print(s, sep=',', file=open('dump.txt', 'a'))
    print(s, sep=',')
    break
    
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
    break
    
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
template
for i, row in df.iterrows():
    if not row['Date']: continue
    d = {'title': row['Title'], 'magazine': row['Magazine'], 'tags': make_tags(row), 'link': row['Link']}
    outpath = '_posts/{}_{}'.format(row['Date'], row['Title'].replace(' ', '_'))
    Path(outpath).write_text(template.format(**d))
    
for i, row in df.iterrows():
    if not row['Date']: continue
    d = {'title': row['Title'], 'magazine': row['Magazine'], 'tags': make_tags(row), 'link': row['Link']}
    outpath = '_posts/{}_{}'.format(row['Date'], row['Title'].replace(' ', '_')).replace('/', '_')
    Path(outpath).write_text(template.format(**d))
    
for i, row in df.iterrows():
    if not row['Date']: continue
    d = {'title': row['Title'], 'magazine': row['Magazine'], 'tags': make_tags(row), 'link': row['Link']}
    outpath = '_posts/{}_{}.md'.format(row['Date'], row['Title'].replace(' ', '_')).replace('/', '_')
    Path(outpath).write_text(template.format(**d))
    
for i, row in df.iterrows():
    if pd.isnull(row['Date']): continue
    d = {'title': row['Title'], 'magazine': row['Magazine'], 'tags': make_tags(row), 'link': row['Link']}
    outpath = '_posts/{}_{}.md'.format(row['Date'], row['Title'].replace(' ', '_').replace('/', '_'))
    Path(outpath).write_text(template.format(**d))
    
for i, row in df.iterrows():
    if pd.isnull(row['Date']): continue
    d = {'title': row['Title'], 'magazine': row['Magazine'], 'tags': make_tags(row), 'link': row['Link']}
    outpath = '_posts/{}-{}.md'.format(row['Date'], row['Title'].replace(' ', '_').replace('/', '_'))
    Path(outpath).write_text(template.format(**d))
    
make_tags(row)
template
print template
print(template)
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
    d = {'title': row['Title'], 'magazine': row['Magazine'], 'tags': make_tags(row), 'link': row['Link']}
    outpath = '_posts/{}-{}.md'.format(row['Date'], row['Title'].replace(' ', '_').replace('/', '_'))
    Path(outpath).write_text(template.format(**d))
    if i >= 20:
        break
        
for i, row in df.iterrows():
    if pd.isnull(row['Date']): continue
    d = {'title': row['Title'], 'magazine': row['Magazine'], 'tags': make_tags(row), 'link': row['Link']}
    outpath = '_posts/{}-{}.md'.format(row['Date'], row['Title'].replace(' ', '_').replace('/', '_'))
    Path(outpath).write_text(template.format(**d))
    if i >= 20:
        break
    else:
        print(i)
        
for i, row in df.iterrows():
    if pd.isnull(row['Date']): continue
    d = {'title': row['Title'], 'magazine': row['Magazine'], 'tags': make_tags(row), 'link': row['Link']}
    outpath = '_posts/{}-{}.md'.format(row['Date'], row['Title'].replace(' ', '_').replace('/', '_'))
    Path(outpath).write_text(template.format(**d))
    if i >= 20:
        break
    else:
        print(i, outpath)
        
df.head()
for i, row in df.iterrows():
    if pd.isnull(row['Date']): continue
    d = {'title': row['Title'], 'magazine': row['Magazine'], 'tags': make_tags(row), 'link': row['Link']}
    outpath = '_posts/{}-{}.md'.format(row['Date'], row['Title'].replace(' ', '_').replace('/', '_'))
    Path(outpath).write_text(template.format(**d))
    if i >= 30:
        break
    else:
        print(i, outpath)
        
for i, row in df.iterrows():
    if pd.isnull(row['Date']): continue
    d = {'title': row['Title'], 'magazine': row['Magazine'], 'tags': make_tags(row), 'link': row['Link']}
    outpath = '_posts/{}-{}.md'.format(row['Date'], row['Title'].replace(' ', '_').replace('/', '_'))
    Path(outpath).write_text(template.format(**d))
    
for i, row in df.iterrows():
    if pd.isnull(row['Date']): continue
    d = {'title': row['Title'].replace(':', '-'), 'magazine': row['Magazine'], 'tags': make_tags(row), 'link': row['Link']}
    outpath = '_posts/{}-{}.md'.format(row['Date'], row['Title'].replace(' ', '_').replace('/', '_'))
    Path(outpath).write_text(template.format(**d))
    
get_ipython().run_line_magic('save', '/Users/jessime.kirk/Code/me/laura_website2/scripts/ipython_code.py 1-157')
