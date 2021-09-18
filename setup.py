#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
# Copyright (C) 2020-2021 Liming Xie
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
import os.path
import codecs   # To use a consistent encoding
import setuptools

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the relevant file
with codecs.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

#from hiquant.version import __version__
lines = open(here + '/hiquant/version.py', mode='r').readlines()
for line in lines:
    if line.startswith('__version__ = '):
        __version__ = line.replace('__version__ = ','').split('\'')[1]
        break

# Package name
pname = 'hiquant'

# Generate links
gurl = 'https://github.com/floatinghotpot/' + pname
gdurl = gurl + '/tarball/' + __version__

setuptools.setup(
    name = pname,

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version = __version__,
    description = 'Out-of-box python tool and framework for quantitative trading and study',
    long_description = long_description,
    long_description_content_type='text/markdown',

    # The project's main homepage.
    url = 'https://github.com/floatinghotpot/hiquant',
    download_url = 'https://github.com/floatinghotpot/hiquant',

    # Author details
    author = 'Liming Xie',
    author_email = 'liming.xie@gmail.com',

    # Choose your license
    license = 'GPLv3+',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',

        # Indicate which Topics are covered by the package
        'Topic :: Software Development',
        'Topic :: Office/Business :: Financial',

        # Pick your license as you wish (should match "license" above)
        ('License :: OSI Approved :: ' +
         'GNU General Public License v3 or later (GPLv3+)'),

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',

        # Operating Systems on which it runs
        'Operating System :: OS Independent',
    ],

    # What does your project relate to?
    keywords=[
        'stock',
        'fund',
        'finance',
        'spider',
        'quant',
        'quantitative',
        'investment',
        'trading',
        'algotrading',
        'data',
    ],

    platforms = 'any',
    python_requires='>=3.7',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=setuptools.find_packages(exclude=['cache', 'output', 'log', 'samples', 'docs']),

    # List run-time dependencies here.
    # These will be installed by pip when your
    # project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires = [
      'requests',
      'pandas',
      'akshare',
      'tabulate',
      'matplotlib',
      'mplfinance',
    ],

    # List additional groups of dependencies here
    # (e.g. development dependencies).
    # You can install these using the following syntax, for example:
    # $ pip install -e .[dev,test]
    # extras_require={},

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    # package_data={'sample': ['package_data.dat'],},

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('my_data', ['data/data_file'])],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    # entry_points={'console_scripts': ['sample=sample:main',],},
    entry_points={'console_scripts': ['hiquant=hiquant.cli:cli_main']},

    #scripts=['tools/hq.py'],
)
