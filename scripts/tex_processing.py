import os
import subprocess


def run_command(tex_path, command, *args):
    original_dir = os.path.dirname(os.path.abspath(tex_path))
    current_working_dir = os.getcwd()
    base = os.path.basename(tex_path)
    base_name, _ = os.path.splitext(base)

    os.chdir(original_dir)

    try:
        subprocess.run([command, base_name, *args], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {command}:", e)
    finally:
        os.chdir(current_working_dir)


def run_latex(tex_path):
    run_command(tex_path, 'latex')



def run_biber(tex_path):
    run_command(tex_path, 'biber')


def run_htlatex(tex_path):
    config_path = os.path.abspath('./scripts/myconfig.cfg')
    run_command(tex_path, 'htlatex', config_path, '-css', '-NoFonts')
