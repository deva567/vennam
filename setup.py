"""Setup script for vennam master"""

import os.path
from setuptools import setup

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

# This call to setup() does all the work
setup(
    name="vennam",
    version="1.2.11",
    description="This package will helps to convert DataFrame to Dictionary and provide Exploratory Data Analysis.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/deva567/vennam",
    author="Vennam",
    author_email="vennamdevendhar@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["vennam"],
    include_package_data=True,
    install_requires=[
        "pandas>=1.0.5",
        "wordcloud>=1.7.0",
        "nltk>=3.5",
        "matplotlib>=3.2.2",
        "Pillow>=7.1.2",
        "psycopg2>=2.8.5",
        "sqlalchemy>=1.3.17"
    ],
)