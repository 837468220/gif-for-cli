#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright 2018 Google LLC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from setuptools import setup, find_packages
import os

import gif_for_cli


# Python doesn't seem to have a consistent way of including non-Python files
# from outside a package directory, nor an obvious way to map a subpackage to
# a different directory.
symlink_path = 'gif_for_cli/third_party'
try:
    os.unlink(symlink_path)
except:
    pass

os.symlink('../third_party', symlink_path)

packages = find_packages()
packages.remove('third_party')


setup(
    name='gif-for-cli',
    version=gif_for_cli.__version__,
    description="Render an animated GIF to your command line terminal.",
    author='Seán Hayes',
    author_email='sth@google.com',
    url='https://github.com/google/gif-for-cli',
    keywords='gif cli terminal ascii ansi',
    packages=packages,
    include_package_data=True,
    entry_points = {
        'console_scripts': ['gif-for-cli=gif_for_cli.__main__:main'],
    },
    install_requires=[
        'Pillow>=5.1.0', # PIL Software License
        'requests>=2.18.4', # Apache License 2.0
        'x256>=0.0.3', # MIT License
    ],
    tests_require=[
        'coverage>=4.5.1',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.5',
        'Topic :: Artistic Software',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion',
        'Topic :: Multimedia :: Graphics :: Presentation',
        'Topic :: Multimedia :: Graphics :: Viewers',
        'Topic :: Multimedia :: Video :: Conversion',
        'Topic :: Multimedia :: Video :: Display',
        'Topic :: Terminals',
        'Topic :: Utilities',
    ],
)

os.unlink(symlink_path)
