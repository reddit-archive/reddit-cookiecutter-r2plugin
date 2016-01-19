import os
import shutil

PROJECT_ROOT = os.path.realpath(os.path.curdir)
HAS_STATIC_ASSETS = "{{ cookiecutter.has_static_assets }}"


if HAS_STATIC_ASSETS != "yes":
    os.unlink(os.path.join(PROJECT_ROOT, "Makefile.plugin"))
    shutil.rmtree(os.path.join(PROJECT_ROOT, "{{ cookiecutter.project_name }}", "public"))
