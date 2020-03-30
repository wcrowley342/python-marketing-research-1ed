import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="test-pkg-python-marketing-research", # Replace with your own username
    version="0.9",
    author="Jason Schwarz",
    author_email="python-marketing@gmail.com",
    description="A test of package for Python for Marketing Research and Analytis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/python-marketing-research/python-marketing-research-1ed",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
