import os, sys
from setuptools import setup, find_packages

def read_requirements():
    """Parse requirements from requirements.txt."""
    reqs_path = os.path.join('.', 'requirements.txt')
    with open(reqs_path, 'r') as f:
        requirements = [line.rstrip() for line in f]
    return requirements

setup(
    version='0.0.1',
    description='Sample package for Python-Guide.org',
    long_description=readme,
    author='Kensuke Mitsuzawa',
    install_requires=read_requirements(),
)
