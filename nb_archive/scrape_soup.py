from selenium.webdriver import Chrome
import pymongo
import time
import pandas as pd
from bs4 import BeautifulSoup
import json
import random 

browser = Chrome()

mc = pymongo.MongoClient()
db = mc['avalanche']
forecast_coll = db['forecasts']


def collect_day_urls(years, browser):
    months = ['December','January','February','March','April']
    years_of_daily_urls = []
    for year in years:
        for month in months:
            month_url = (f'https://www.nwac.us/avalanche-forecast/archives/days/?csrfmiddlewaretoken'
        f'=kuOHmWVZlRxUjgCIf1kykA2GI7vn4W87saoPFa8Go5QfjYOCj6ybfMv74kwW2Mwx&month={month}&year={year}')
            browser.get(month_url)
            day_elements = browser.find_elements_by_css_selector('#main-content > div > a')
            for day_element in day_elements:
                day_url = day_element.get_attribute('href')
                years_of_daily_urls.append(day_url)
    return years_of_daily_urls

def get_mountain_urls_from_day_urls(day_url_list, browser,fp=None):
    '''Retreives forecast urls from list of urls.
        If filepath not specified, default is master_url_list.json in current directory.'''
    if fp == None:
        fp = 'master_url_list.json'
    with open(fp,'w') as f:
        for url in day_url_list:
            browser.get(url)
            mtn_els = browser.find_elements_by_class_name('forecast')
            for mtn_el in mtn_els:
                mtn_url = mtn_el.get_attribute('href')
                json.dump({'url':mtn_url},f)
                f.write('\n')
                time.sleep(random.random()*.5)


def scrape_url(url, browser, delay=5):
    """Returns the HTML source from a URL."""
    browser.get(url)
    time.sleep(delay)
    html = browser.page_source
    return html

def collect_page(url, browser, coll=forecast_coll, delay=5):
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
    danger_above_tag = '#treeline-above > div.span4.elev-day1-column > div.danger-description > h4'
    danger_near_tag ='#treeline-near > div.span4.elev-day1-column > div.danger-description > h4'
    danger_below_tag = '#treeline-below > div.span4.elev-day1-column > div.danger-description > h4'
    area_tag = '#main-content > h2'
    date_tomorrow_tag = '#elevation-levels-header > div.span4.desktop.elevation-day-name > p'
    #date_today_tag = '#main-content > div.forecast-info > div.forecast-date'
    soup = BeautifulSoup(page['html'],'lxml')
    area = soup.select_one(area_tag).text
    date_tomorrow = soup.select_one(date_tomorrow_tag).text
    #date_today = soup.select_one(date_today_tag).text #its in a string with other text, not very useful, can engineer this later
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