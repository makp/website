import os
import subprocess


def run_latex(tex_path):
    original_dir = os.path.dirname(os.path.abspath(tex_path))
    current_working_dir = os.getcwd()
    base = os.path.basename(tex_path)
    base_name, _ = os.path.splitext(base)

    os.chdir(original_dir)

    try:
        subprocess.run(['latex', base_name], check=True)
    except subprocess.CalledProcessError as e:
        print("Error running LaTeX:", e)
    finally:
        os.chdir(current_working_dir)


def run_biber(tex_path):
    original_dir = os.path.dirname(os.path.abspath(tex_path))
    current_working_dir = os.getcwd()
    base = os.path.basename(tex_path)
    base_name, _ = os.path.splitext(base)

    os.chdir(original_dir)

    try:
        subprocess.run(['biber', base_name], check=True)
    except subprocess.CalledProcessError as e:
        print("Error running Biber:", e)
    finally:
        os.chdir(current_working_dir)


def run_htlatex(tex_path):
    original_dir = os.path.dirname(os.path.abspath(tex_path))
    config_path = os.path.abspath('./scripts/myconfig.cfg')
    current_working_dir = os.getcwd()
    base = os.path.basename(tex_path)
    base_name, _ = os.path.splitext(base)

    os.chdir(original_dir)

    try:
        subprocess.run(['htlatex', base_name, config_path, '-css', '-NoFonts'], check=True)
    except subprocess.CalledProcessError as e:
        print("Error running htlatex:", e)
    finally:
        os.chdir(current_working_dir)
