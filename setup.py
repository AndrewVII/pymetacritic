import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name="pymetacritic-AndrewVII",
    version="0.0.1",
    author="Andrew Gall",
    author_email="andrewgall12@gmail.com",
    description="A package to get album scores from metacritic",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AndrewVII/pymetacritic",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
