#!/usr/bin/env python3

import os.path
import subprocess
from bs4 import BeautifulSoup

path_web = '/home/makmiller/Documents/mydocs/websites/website-main/'
path_conf = path_web + 'scripts/myconfig.cfg'
path_dest = path_web + 'templates/includes/'


def processHTML(path_to_tex):
    subprocess.call(['./generate-html.sh', path_to_tex, path_conf])  # compile tex file

    path_base = os.path.splitext(os.path.basename(path_to_tex))[0]  # basename without extension
    path_dir = os.path.dirname(path_to_tex)  # dirname
    path_to_soup = os.path.join(path_dir, path_base + '.html')

    # use Python built-in HTML parser
    soup = BeautifulSoup(open(path_to_soup), 'html.parser')

    body_tag = soup.body        # extract body tag

    # <body> --> <div class='latex'>
    body_tag.name = "div"
    body_tag['class'] = 'latex'

    # Delete div tag generated by the LaTeX \maketitle cmd and its
    # contents
    maketitle_tag = soup.find('div', class_="maketitle")
    if maketitle_tag:
        maketitle_tag.decompose()

    weeks = soup.find_all("h4")
    for sec in weeks:
        label = sec.span.string.replace(" ", "")
        sec['id'] = label

    output_file = path_dest + path_base + '.html'
    with open(output_file, 'w+') as f:
        print(body_tag.prettify(), file=f)


path_res = os.path.join(path_web, 'latex/research/research.tex')
path_pubs = os.path.join(path_web, 'latex/my-pubs/my-pubs.tex')

path_sched1 = os.path.join(path_web, 'latex/schedules/schedule_s22_phil255/schedule_s22_phil255.tex')
# path_sched2 = os.path.join(path_web, 'latex/schedules/schedule_f18_phil342/schedule_f18_phil342.tex')
# path_sched3 = os.path.join(path_web, 'latex/schedules/schedule_s20_phil212/schedule_s20_phil212.tex')
# path_sched4 = os.path.join(path_web, 'latex/schedules/schedule_s19_phil460/schedule_s19_phil460.tex')
# path_sched5 = os.path.join(path_web, 'latex/schedules/schedule_f21_phil255/schedule_f21_phil255.tex')
path_sched6 = os.path.join(path_web, 'latex/schedules/schedule_s22_phil342/schedule_s22_phil342.tex')


# processHTML(path_res)
# processHTML(path_pubs)
processHTML(path_sched1)
# processHTML(path_sched2)
# processHTML(path_sched3)
# processHTML(path_sched4)
processHTML(path_sched6)
