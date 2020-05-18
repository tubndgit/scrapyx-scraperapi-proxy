# scrapyx-scraperapi-proxy

Scraper API middleware for Scrapy (http://scrapy.org/)
=======================================================


Install
--------

Checkout the source and run

    python setup.py install


settings.py
-----------

    # Activate the middleware
    SCRAPERAPI_ENABLED = True
    
    #The API key 
    SCRAPERAPI_KEY='your API key'

    DOWNLOADER_MIDDLEWARES = {
        'scrapy_scraperapi.ScraperApiProxy': 610,
    }


