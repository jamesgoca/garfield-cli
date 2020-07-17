import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="garfield",
    version="0.1",
    py_modules=["garfield"],
    author="James Gallagher",
    author_email="jamesg@jamesg.app",
    description="A CLI for the Garfield comic strip.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jamesgallagher432/garfield-cli",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points='''
        [console_scripts]
        garfield=garfield_cli:cli
    ''',
)
