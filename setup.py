import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="iris",
    version="0.0.2",
    author="Adriano Donninelli",
    author_email="adriano.donninelli@hotmail.it",
    description="A command line tool to sync folders and files between local and remote paths",
    long_description=long_description,
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
    python_requires='>=3',
    install_requires=[
        "aiofile>=3.8.1",
        "asyncssh>=2.14.2",
        "PyYAML>=6.0",
        "rich>=13.1.0",
        "watchdog>=2.2.1",
        "uvloop>=0.17.0",
    ],
    entry_points={
        'console_scripts': ['iris = iris.iris:main', 'iris-init = iris.iris:init_config']
    }
)
