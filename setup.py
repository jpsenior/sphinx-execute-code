#!/usr/bin/env python
""" Distutils setup file """
from setuptools import setup

def readme():
    """ Returns Readme.rst as loaded RST for documentation """
    with open('Readme.rst', 'r') as filename:
        return filename.read()
setup(
    name='sphinx_execute_code',
    version='0.2a2',
    platforms=['any'],
    packages=['sphinx_execute_code'],
    url='https://github.com/jpsenior/sphinx-execute-code',
    license='MIT',
    author='JP Senior',
    author_email='jp.senior@gmail.com',
    description='Sphinx support for execution of python code from code blocks or files',
    long_description=readme(),
    install_requires=['docutils', 'sphinx'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Framework :: Sphinx :: Extension',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='sphinx extension directive execute code',
)
