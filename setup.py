# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from distutils.core import setup
setup(
  name = 'nsepy',
  packages = ['nsepy', 'nsepy.derivatives', 'nsepy.debt'], # this must be the same as the name above
  version = '0.8',
  description = 'Library to download financial data in pandas dataframe',
  author = 'Swapnil Jariwala',
  author_email = 'sjerry4u@gmail.com',
  url = 'https://github.com/swapniljariwala/nsepy', # use the URL to the github repo
  entry_points='''
    [console_scripts]
    nsecli=nsepy.cli:cli
  ''',
  download_url = 'https://github.com/swapniljariwala/nsepy/archive/nsepy-v0.8.zip', 
  install_requires = ['beautifulsoup4', 'requests', 'numpy', 'pandas', 'six', 'click', 'lxml'],
  keywords = ['testing', 'logging', 'example'], # arbitrary keywords
  classifiers = [],
)
