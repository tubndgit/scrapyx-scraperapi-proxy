#!/usr/bin/env python
import sys
import os
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(name='scrapyx-scraperapi-proxy',
        version='0.1.1',
        packages=find_packages(),
        description='Scrapy scraperapi Proxy: scraperapi interfacing middleware for Scrapy',
        author='Henry B.',
        author_email='tubnd.younet@gmail.com',
        url='https://github.com/tubndgit/scrapyx-scraperapi-proxy',
        download_url = 'https://github.com/tubndgit/scrapyx-scraperapi-proxy/archive/master.zip', 
        packages=['scrapyx_scraperapi'],
        install_requires = [
            'scraperapi-sdk'
        ],
        license='MIT',
    )