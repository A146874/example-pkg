import setuptools

with open("README.md", 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'example-pkg-A146874',
    version = '0.0.1',
    author = "Chris Defreitas",
    author_email = "christopher_defreitas@progressive.com",
    description = "A sample package",
    long_description = long_description,
    url="https://github.com/A146874/example-pkg",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
