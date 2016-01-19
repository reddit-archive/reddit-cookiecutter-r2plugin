#!/usr/bin/python

from setuptools import setup, find_packages

setup(
    name="{{ cookiecutter.project_name }}",
    description="{{ cookiecutter.project_slug }}, a plugin for reddit",
    version="0.0",
    packages=find_packages(),
    install_requires=[
        "r2",
    ],
    entry_points={
        "r2.plugin": [
            "{{ cookiecutter.project_slug }} = {{ cookiecutter.project_name }}:{{ cookiecutter.plugin_name }}",
        ],
    },
    zip_safe=False,
)
