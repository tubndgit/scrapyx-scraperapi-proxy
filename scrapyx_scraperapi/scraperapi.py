# -*- coding: utf-8 -*-
__author__ = 'Henry B. <tubnd.younet@gmail.com>'

try:
    from scraper_api import ScraperAPIClient
except:
    pass

class ScraperApiProxyMiddleware(object):
    def __init__(self, settings):
        if not settings.getbool('SCRAPERAPI_ENABLED', True):
            raise NotConfigured
        
        self.SCRAPERAPI_KEY = settings.get('SCRAPERAPI_KEY', '')
        self.SCRAPERAPI_CLIENT = None   
        try: 
            self.SCRAPERAPI_CLIENT = ScraperAPIClient(self.SCRAPERAPI_KEY)         
        except:
            raise NotConfigured

    @classmethod
    def from_crawler(cls, crawler):
        o = cls(crawler.settings)
        return o

    def process_request(self, request, spider):
        new_url = self.SCRAPERAPI_CLIENT.scrapyGet(url=request.url, render=True)
        return request.replace(url=new_url)