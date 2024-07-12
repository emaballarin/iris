import os

import setuptools


def _fread(fname: str):
    with open(
        os.path.join(os.path.dirname(__file__), fname), "r", encoding="utf-8"
    ) as fopen:
        return fopen.read()


setuptools.setup(
    name="iris",
    version="0.0.2",
    author="Adriano Donninelli",
    author_email="adriano.donninelli@hotmail.it",
    description="A command line tool to sync folders and files between local and remote paths",
    long_description=_fread("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/Junkybyte/iris",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=False,
    zip_safe=True,
    python_requires=">=3",
    install_requires=[
        "aiofile>=3.8.8",
        "asyncssh>=2.15.0",
        "PyYAML>=6.0.1",
        "rich>=13.7.1",
        "watchdog>=4.0.1",
    ],
    extras_require={
        "uvloop": ["uvloop>=0.19.0"],
    },
    entry_points={
        "console_scripts": [
            "iris = iris.iris:main",
            "iris-init = iris.iris:init_config",
        ]
    },
)
