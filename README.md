
Personal website.

## Files and folders

- `app.yaml`: App Engine config.
- `templates/`: stores HTML pages and jinja2 templates
- `scripts/html-parser.py`: process the .tex files in the latex folder and covert them into HTML pages so that they can be used by the website. Specifically, it produces HTML pages from LaTeX files by running `htlatex` (generate-html.sh) and processes the HTML output with the Python module `BeautifulSoup`.
