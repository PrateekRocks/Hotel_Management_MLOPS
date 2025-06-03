from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Hotel Management",
    version="0.1",
    author="Prateek",
    packages=find_packages(),
    install_requires = requirements,
)