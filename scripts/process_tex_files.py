#!/usr/bin/env python3

import argparse
import logging
from pathlib import Path
from bs4 import BeautifulSoup
import shutil


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Process LaTeX files to generate HTML.")

    parser.add_argument('path_to_tex', help="Path to the input LaTeX file.")

    script_dir = Path(__file__).parent
    default_config_path = script_dir / 'scripts' / 'config.cfg'
    parser.add_argument('--config', default=default_config_path, help="Path to htlatex config file.")

    parser.add_argument('--output_dir', default='templates/includes/', help="Path to save the processed HTML files.")
    return parser.parse_args()


def process_html(html_path, output_dir):
    """Clean up the generated HTML using BeautifulSoup."""
    with open(html_path) as f:
        soup = BeautifulSoup(f, 'html.parser')

    body_tag = soup.body
    body_tag.name = "div"
    body_tag['class'] = 'latex'

    maketitle_tag = soup.find('div', class_="maketitle")
    if maketitle_tag:
        maketitle_tag.decompose()

    weeks = soup.find_all("h4")
    for sec in weeks:
        label = sec.span.string.replace(" ", "")
        sec['id'] = label

    output_file = output_dir / (html_path.stem + '.html')
    with open(output_file, 'w+') as f:
        print(body_tag.prettify(), file=f)


def clean_temp_files(temp_folder):
    """Clean up temporary files and folders."""
    if temp_folder.exists():
        shutil.rmtree(temp_folder)


if __name__ == '__main__':
    # Setup Logging
    logging.basicConfig(level=logging.INFO)

    args = parse_arguments()

    # Convert Paths to Path Objects
    tex_path = Path(args.path_to_tex)
    config_path = Path(args.config)
    output_dir = Path(args.output_dir)

    # Check if LaTeX file exists
    if not tex_path.exists():
        logging.error("The specified LaTeX file does not exist.")
    else:
        temp_folder = Path("/tmp") / f"website_{tex_path.stem}"
        temp_folder.mkdir(parents=True, exist_ok=True)

        try:
            shutil.copy(tex_path, temp_folder)

            base_path = temp_folder / tex_path.name

            run_latex_commands(base_path)

            html_path = temp_folder / (tex_path.stem + '.html')
            process_html(html_path, output_dir)

            logging.info("HTML processing completed successfully.")

        except Exception as e:
            logging.error(f"An error occurred: {e}")
        finally:
            clean_temp_files(temp_folder)
