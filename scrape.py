
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