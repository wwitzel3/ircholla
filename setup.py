
"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ircholla',
    version='0.1',
    description='Simple IRC Holla bot.',
    long_description=long_description,
    url='https://github.com/wwitzel3/ircholla',
    author='Wayne Witzel III',
    author_email='wayne@riotousliving.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='irc notify development',
    py_modules=["ircholla"],
    extras_require={
        'test': ['py.test'],
    },
)
