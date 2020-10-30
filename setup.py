import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="coinbasepro-pkg-dndungu",
    version="0.0.5",
    author="David Ndungu",
    author_email="david@ndungu.dev",
    description="Coinbasepro candles fetcher",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dndungu/coinbasepro",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
