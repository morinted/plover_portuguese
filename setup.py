#!/usr/bin/env python3

from setuptools import setup


setup(
    name = 'plover_portuguese',
    version = '0.1.0',
    description = 'Portuguese system for Plover',
    author = 'Ted Morin',
    author_email = 'morinted@gmail.com',
    license =  'GNU General Public License v2 or later (GPLv2+)',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    install_requires = [
        'plover>=4.0.0.dev0',
    ],
    py_modules = [
        'plover_portuguese',
    ],
    entry_points = '''

    [plover.system]
    Portuguese Stenotype = plover_portuguese

    ''',
    zip_safe = True,
)
