"""Setup script..."""
import pathlib
from setuptools import setup

from mypkg import __version__


# The directory containing this file
HERE = pathlib.Path(__file__).resolve().parent

# The text of the README file is used as a description
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="mypkg_wip",
    version=__version__,
    description="My description",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/realpython/reader",
    author="Ulrich Schmidt",
    author_email="uncsco@mail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.6", #
    packages=[
        'mypkg',
        'mypkg.std'
    ],
    include_package_data=True,
    install_requires=[],
    extras_require={
        #"test": ["pytest"],
        "rich": ["rich"],
        #// `python_version`: https://stackoverflow.com/a/60517114
        "dataclasses": ["dataclasses; python_version < '3.7'"],
        "excel": ["openpyxl"],
    },
    entry_points={
        "console_scripts": ["mypkg=my_lib.__main__:main"],
    },
)
