#!/usr/bin/env python
import sys
from distutils.core import setup

setup(name='scrapyx-scraperapi-proxy',
        version='0.1',
        description='Scrapy scraperapi Proxy: scraperapi interfacing middleware for Scrapy',
        author='Henry B.',
        author_email='tubnd.younet@gmail.com',
        url='https://github.com/tubndgit/scrapyx-scraperapi-proxy',
        packages=['scrapyx_scraperapi'],
        install_requires = [
            'scraperapi-sdk'
        ],
    )