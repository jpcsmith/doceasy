"""Installation module for doceasy.
"""
from os import path
from pathlib import Path
from setuptools import setup, find_packages


setup(
    name='doceasy',  # Required
    description='Wrapper around docopt and schema',  # Optional
    url='https://github.com/jpcsmith/doceasy',  # Optional
    python_requires='>=3.5',

    # Optional long description in README.md
    long_description=Path(
        path.join(path.abspath(path.dirname(__file__)), 'README.md')
    ).read_text(),

    # Automatically extract version information from git tags
    use_scm_version=True,
    setup_requires=['setuptools_scm', 'wheel'],

    # This should be your name or the name of the organization which owns the
    # project.
    author='Jean-Pierre Smith',  # Optional

    # This should be a valid email address corresponding to the author listed
    # above.
    author_email='rougesprit@gmail.com',  # Optional

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    install_requires=['docopt', 'schema'],  # Optional

    extras_require={  # Optional
        'dev': [],
        'test': [],
    },
)
