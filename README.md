# My Website

[https://laurazolman.github.io/](https://laurazolman.github.io/)

## How to Update from Gsheet

1. Make sure you have access to [Writing Portfolio](https://docs.google.com/spreadsheets/d/1YRB5ekpn2D9mlNk65wi3ZeaK1QnpcLm2HVl1I9Fj48k/edit#gid=0).
1. Download the gsheet as a `.tsv` file. Take note of the exact path you download it too. By default, it should download to something like `/Users/laura.zolman/Downloads/Writing Portfolio - Sheet1.tsv`, but you can rename it to anything and put it in any folder.
1. At the top of the `scripts/update_from_writing_portfolio.py` file, there's a variable called `TSV_PATH`. Change the path to reflect the location of the gsheet you just downloaded. Here's what `TSV_PATH` currently [looks like](https://github.com/LauraZolman/LauraZolman.github.io/blob/master/scripts/update_from_writing_portfolio.py#L6).
1. To update the script, we're going to have to run some commands. Open a terminal. Press `Cmd + Space` to open Spotlight Search, type "terminal", and hit `return`. A new, blank window should open.
1. Navigate to the git repository for this website. If you cloned the repository with GitHub Desktop, the path might be at something like `/Users/laura.zolman/GitHub/laura_website`. In order to navigate there from the terminal, type `cd ~/GitHub/laura_website` (or the equivalent path) and hit `return`.
1. Once you're successfully in the root directory of the website, you can execute the update script to load new content. Still from the terminal, type `python3 scripts/update_from_writing_portfolio.py` and hit `return`.
1. If you're using GitHub you should see that local changes have been generate (reflecting the new updates from the gsheet). Assuming these changes look the way you want them, use the `Sync` button in GitHub Desktop to push your changes to GitHub.
1. Go to the [GitHub repo](https://github.com/LauraZolman/LauraZolman.github.io). You should see that the last `commit` was within the last minute, indicating that your changes have been successfully pushed.
1. You can monitor the [deployment page](https://github.com/LauraZolman/LauraZolman.github.io/deployments/activity_log?environment=github-pages) to see when your updates go live. Once this page has been updated, you can go back to [https://laurazolman.github.io/](https://laurazolman.github.io/) and verify that everything looks right.


Below is more documentation on how to get started with the tools used to generate this site.

## Minimal Mistakes remote theme starter

Fork this repo for the quickest method of getting started with the [Minimal Mistakes Jekyll theme](https://github.com/mmistakes/minimal-mistakes).

Contains basic configuration to get you a site with:

- Sample posts.
- Sample top navigation.
- Sample author sidebar with social links.
- Sample footer links.
- Paginated home page.
- Archive pages for posts grouped by year, category, and tag.
- Sample about page.
- Sample 404 page.
- Site wide search.

Replace sample content with your own and [configure as necessary](https://mmistakes.github.io/minimal-mistakes/docs/configuration/).

---

### Troubleshooting

If you have a question about using Jekyll, start a discussion on the [Jekyll Forum](https://talk.jekyllrb.com/) or [StackOverflow](https://stackoverflow.com/questions/tagged/jekyll). Other resources:

- [Ruby 101](https://jekyllrb.com/docs/ruby-101/)
- [Setting up a Jekyll site with GitHub Pages](https://jekyllrb.com/docs/github-pages/)
- [Configuring GitHub Metadata](https://github.com/jekyll/github-metadata/blob/master/docs/configuration.md#configuration) to work properly when developing locally and avoid `No GitHub API authentication could be found. Some fields may be missing or have incorrect data.` warnings.
