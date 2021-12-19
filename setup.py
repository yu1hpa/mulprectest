from setuptools import setup, find_packages
from os import path
from io import open

pwd = path.abspath(path.dirname(__file__))

with open(path.join(pwd, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='mulprectest',
    version='0.0.1',
    description='mulprec test library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/yu1hpa/mulprec/',
    author='yu1hpa',
    packages=find_packages(),
    install_requires=['sympy'],
)
