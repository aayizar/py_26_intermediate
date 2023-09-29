from io import open
from setuptools import setup

"""
:authors: DeepMalice
:license: Apache License, Version 2.0, see LICENSE file
:copyright: (c) 2021 Peopl3s
"""

version = '1.0.0'

# with open('README.md', encoding='utf-8') as f:
#     long_description = f.read()

long_description = """# DiffPy

DiffPy is a Python library for discrete mathematics. It aims to become
a fully functional computer algebra system (CAS), while keeping
the code as simple as possible so that it is understandable and easily extensible.  DiffPy
is written entirely in Python. DiffPy is also able to solve problems related to finding derivatives and integrals of complex functions

Contact us for more information:

    Tangatarov Nurzhan: https://t.me/Tngtarov
    Syzdykova Meyirim: https://t.me/meyirimq
    Tuleugalieva Bibi: https://t.me/bbshkaaq"""

setup(
    name='diffpy',
    version=version,
    
    author='DeepMalice',
    author_email='tangatarovnurzan2@gmail.com',

    description=(
        u'Python module for writing scripts for project management platform '
        u'Club House (clubhouse.io API wrapper)'
    ),
    long_description=long_description,
    long_description_content_type='text/markdown',
    
    url='https://github.com/Peopl3s/club_house_api',
    download_url='https://github.com/Peopl3s/club-house-api/archive/main.zip',

    packages=['diffpy'],
    install_requires=['numpy'],

    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
    ]
)