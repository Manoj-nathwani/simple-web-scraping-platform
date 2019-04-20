import argos
import petsathome

def scrape(url, html):
    if 'argos.co.uk' in url:
        return argos.parse(html)
    elif 'petsathome.com' in url:
        return petsathome.parse(html)
    else:
        assert False, 'Scraper not configured'