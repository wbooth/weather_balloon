from setuptools import setup, find_packages
from codecs import open
from os import path

# Get long description from README file
with open(path.join(path.abspath(path.dirname(__file__)), 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='weather_balloon',
    version='1.0.0',
    description='Weather Balloon',
    long_description=long_description,
    author='wbooth',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Education',
        'Topic :: Scientific/Engineering :: Atmospheric Science',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='altitude balloon',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['sense-hat']
)
