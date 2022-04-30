"""Setup script..."""
import pathlib
from setuptools import setup

from my_lib import __version__


# The directory containing this file
HERE = pathlib.Path(__file__).resolve().parent

# The text of the README file is used as a description
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="my_lib_wip",
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
    packages=["my_lib"],
    include_package_data=True,
    install_requires=[],
    extras_require={
        #"test": ["pytest"],
        "rich": ["rich"],
    },
    #entry_points={"console_scripts": ["realpython=reader.__main__:main"]},
)
