"""Installation module for doceasy.
"""
from os import path
from pathlib import Path
from setuptools import setup, find_packages


setup(
    name='doceasy',  # Required
    url='https://github.com/jpcsmith/doceasy',
    author='Jean-Pierre Smith',
    author_email='rougesprit@gmail.com',
    description='Wrapper around docopt and schema',
    long_description=Path(
        path.join(path.abspath(path.dirname(__file__)), 'README.md')
    ).read_text(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    py_modules=['doceasy'],
    python_requires='>=3.5',
    use_scm_version=True,
    setup_requires=['setuptools_scm', 'wheel'],
    install_requires=['docopt', 'schema'],
    extras_require={
        'dev': ["pylint", "flake8", "mypy"],
        'test': ["pytest"],
    }
)
