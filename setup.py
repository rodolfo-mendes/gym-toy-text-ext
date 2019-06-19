import setuptools

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

classifiers = [
    "Development Status :: 2 - Pre-Alpha",
    "Environment :: Console",
    "Intended Audience :: Education",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Topic :: Scientific/Engineering :: Artificial Intelligence"
]

setup(name="gym-toy-text-ext",
    version="0.0.dev2",
    author="rodmsmendes",
    author_email="rodolfo@reinforcementlearning4.fun",
    description="Toy Text Extended. An extension of the Gym's Toy Text environment.",
    long_description=long_description,
    long_description_context_type="text/markdown",
    license="MIT License",
    url="https://github.com/rodmsmendes/gym-toy-text-ext",
    classifiers=classifiers,
    packages=setuptools.find_packages(),
    install_requires=["gym"])
