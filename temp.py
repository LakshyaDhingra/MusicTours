from temp_functions import scrape, extract, URL, read, store
import time

while True:
    scraped = scrape(URL)
    ext = extract(scraped)
    store(ext)
    time.sleep(2)
