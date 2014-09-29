#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
from os import path
from setuptools import setup


read = lambda filepath: codecs.open(filepath, 'r', 'utf-8').read()


setup(
    name='djangoadmin-list-filters',
    version='0.0.1',
    author='Witold Gren',
    author_email='witold.gren@gmail.com',
    description='This plugin create combobox or list filter in django admin panel.',
    long_description=read(path.abspath(path.join(path.dirname(__file__), 'README.md'))),
    license='LGPL',
    platforms=['Any'],
    keywords=['django', 'django-admin'],
    url='http://github.com/witold-gren/djangoadmin-list-filters',
    classifiers=[
        'Development Status :: Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing'
    ],
    install_requires=[
        'Django>=1.6',
    ],
    packages=['djangoadmin_list_filters',],
    zip_safe=False,
    include_package_data=True
)