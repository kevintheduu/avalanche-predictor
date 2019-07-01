from selenium.webdriver import Chrome
import pymongo
import time
import pandas as pd
from bs4 import BeautifulSoup
import json

browser = Chrome()

def scrape_url(url, browser=browser, delay=3):
    """Returns the HTML source from a URL."""
    browser.get(url)
    time.sleep(delay)
    html = browser.page_source
    return html

def collect_page(url, browser=browser, coll=coll, delay=3):
    """Scrapes and saves the source of a web page."""
    docs = list(coll.find({'url': url}))
    if len(docs) == 0:
        html = scrape_url(browser=browser,
                          url=url,
                          delay=delay)
        coll.insert_one({
            'url': url,
            'html': html,
        })
    doc = coll.find_one({'url' : url})
    return doc
    

def convert_avy_str_to_num(word):
    if word == 'Low':
        return 1
    elif word == 'Moderate':
        return 2
    elif word == 'Considerable':
        return 3
    elif word == 'High':
        return 4
    elif word == 'Extreme':
        return 5