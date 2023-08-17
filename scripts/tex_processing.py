import os
import subprocess


def run_command(tex_path, command, *args):
    """
    Run a specified command with the given arguments.
    """
    tex_dir = os.path.dirname(os.path.abspath(tex_path))

    base = os.path.basename(tex_path)
    base_name, _ = os.path.splitext(base)

    try:
        subprocess.run([command, base_name, *args], check=True, cwd=tex_dir)
    except subprocess.CalledProcessError as e:
        print(f"Error running {command}:", e)


def run_latex(tex_path):
    run_command(tex_path, 'latex')


def run_biber(tex_path):
    """
    Run Biber on a .bcf file.
    """
    run_command(tex_path, 'biber')


# TODO: Consider using pandoc instead of htlatex.
def run_htlatex(tex_path):
    config_path = os.path.abspath('./scripts/myconfig.cfg')
    run_command(tex_path, 'htlatex', config_path, '-css', '-NoFonts')
