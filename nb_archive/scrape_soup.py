from selenium.webdriver import Chrome
import pymongo
import time
import pandas as pd
from bs4 import BeautifulSoup
import json

browser = Chrome()

mc = pymongo.MongoClient()
db = mc['avalanche']
forecast_coll = db['forecasts']

def scrape_url(url, browser=browser, delay=5):
    """Returns the HTML source from a URL."""
    browser.get(url)
    time.sleep(delay)
    html = browser.page_source
    return html

def collect_page(url, browser=browser, coll=forecast_coll, delay=5):
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
    

def create_danger_info(page):
    '''Collects the relevant info from the webpage html'''
    area = soup.select_one(area_tag).text
    date_tomorrow = soup.select_one(date_tomorrow_tag).text
    danger_above = soup.select_one(danger_above_tag).text
    danger_near = soup.select_one(danger_near_tag).text
    danger_below = soup.select_one(danger_below_tag).text
    return {
            'date_tomorrow': date_tomorrow,
            #'date_today': date_today,
            'area': area,
            'danger_above_treeline': danger_above,
            'danger_near_treeline': danger_near,
            'danger_below_treeline': danger_below,
            }