from temp_functions import scrape, extract, URL, read_file, store
import time

while True:
    scraped = scrape(URL)
    ext = extract(scraped)
    ext_content = read_file(ext)
    store(ext)
    time.sleep(2)
