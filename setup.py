import re
from os import path

from setuptools import find_packages, setup

def find_version(*file_path_parts):
    here = path.abspath(path.dirname(__file__))
    with open(path.join(here, *file_path_parts), "r") as fp:
        version_file_text = fp.read()

    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        version_file_text,
        re.M,
    )
    if version_match:
        return version_match.group(1)

    raise RuntimeError("Unable to find version string.")


setup(
    name="sentence_extractor",
    version=find_version("sentence_extractor", "__init__.py"),
    packages=["sentence_extractor"],
    python_requires="==3.7.*",
    author="Aiden-Jeon",
    author_email="ells2124@gmail.com",
    install_requires=[
        "wikiextractor",
        "pandas",
        "kss",
        "typer",
        "regex",
    ],
    entry_points={
        "console_scripts": [
            "wikiextract = sentence_extractor.main:entry_point",
        ],
    },
)
