import os

import setuptools

rootdir = os.path.abspath(os.path.dirname(__file__))
long_description = open(os.path.join(rootdir, 'README.md')).read()

setuptools.setup(
    name="airbnb-london-eda",
    version="0.1",
    author="Laura Stoddart",
    author_email="laurastoddart@hotmail.com",
    description="A comparison of London airbnb data 2019 vs 2020.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lstodd/airbnb-london-eda.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)