from pathlib import Path

import pandas as pd


def make_tags(row):
    base = '  - {}\n'
    tags = row['Tags'].split(', ')
    tags += row['Editorial/Marketing'].split(', ')
    tags += [row['Type of Edit'], row['Writer/Editor'], row['Favorites']]
    tags = ''.join(base.format(t) for t in tags if not pd.isnull(t))
    return tags

df = pd.read_csv('/Users/jessime.kirk/Downloads/Writing Portfolio - Sheet1.tsv', sep='\t')
template = Path('/Users/jessime.kirk/Code/me/laura_website/scripts/template.md').read_text()
for i, row in df.iterrows():
    if pd.isnull(row['Date']): continue
    d = {'title': row['Title'].replace(':', '-'),
         'subtitle': '### ' + row['Subtitle'] if not pd.isnull(row['Subtitle']) else '',
         'magazine': row['Magazine'],
         'tags': make_tags(row),
         'link': row['Link']}
    outpath = '_posts/{}-{}.md'.format(row['Date'], row['Title'].replace(' ', '_').replace('/', '_'))
    Path(outpath).write_text(template.format(**d))
