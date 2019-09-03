import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="adt_extension",
    version="0.1.1",
    author="Álvaro Ferreira Pires de Paiva",
    author_email="alvarofepipa@gmail.com",
    description="Python abstract data structure (ADT) extension",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alvarofpp/python-adt-extension",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
