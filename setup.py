#!/usr/bin/env python

from setuptools import setup

q_version = '2.0.19'

setup(
    name='q',
    url='https://github.com/harelba/q',
    license='LICENSE',
    version=q_version,
    author='Harel Ben-Attia',
    description="Run SQL directly on CSV or TSV files",
    author_email='harelba@gmail.com',
    install_requires=[
        'six>=1.11.0'
    ],
    packages=[
        'bin'
    ],
    entry_points={
        'console_scripts': [
            'q = bin.q:run_standalone'
        ]
    }
)
