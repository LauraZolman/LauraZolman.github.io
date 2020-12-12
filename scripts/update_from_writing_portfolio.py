from pathlib import Path

import pandas as pd


TSV_PATH = '/Users/jessime.kirk/Downloads/Writing Portfolio - Sheet1.tsv'


def clear_files_from_folder(folder):
    folder_path = Path(__file__).resolve().parent.parent / folder
    for path in folder_path.iterdir():
        if path.is_file():
            path.unlink()


def get_tags(row):
    tags = row['Tags'].split(', ')
    tags += row['Editorial/Marketing'].split(', ')
    tags += [row['Type of Edit'], row['Writer/Editor'], row['Favorites']]
    tags = [t for t in tags if not pd.isnull(t)]
    return tags


def make_tags_string(tags):
    base = '  - {}\n'
    tags = ''.join(base.format(t) for t in tags)
    return tags


def make_subtitle(sub):
    return '> ' + sub if not pd.isnull(sub) else ''


def generate_tag_pages(tags):
    clear_files_from_folder('_pages/tags')
    tags.remove('Favorite')  # This page is special; doesn't need regenerating
    template_path = 'scripts/tag_template.md'
    template = Path(template_path).read_text()
    for tag in tags:
        outpath = '_pages/tags/{}-archive.md'.format(tag)
        Path(outpath).write_text(template.format(tag=tag, tag_lower=tag.lower()))

def run():
    clear_files_from_folder('_posts')
    df = pd.read_csv(TSV_PATH, sep='\t')
    template_path = 'scripts/template.md'
    template = Path(template_path).read_text()
    all_tags = set()
    for i, row in df.iterrows():
        if pd.isnull(row['Date']): continue
        tags = get_tags(row)
        d = {'title': row['Title'].replace(':', '-'),
             'subtitle': make_subtitle(row['Subtitle']),
             'magazine': row['Magazine'],
             'tags': make_tags_string(tags),
             'link': row['Link']}
        all_tags.update(tags)
        outpath = '_posts/{}-{}.md'.format(
            row['Date'],
            row['Title'].replace(' ', '_').replace('/', '_'))
        Path(outpath).write_text(template.format(**d))
    generate_tag_pages(all_tags)


if __name__ == '__main__':
    run()
