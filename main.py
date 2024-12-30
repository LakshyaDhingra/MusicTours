from functions import scrape, extract, URL, read, store, send_email
import time

while True:
    scraped = scrape(URL)
    ext = extract(scraped)

    if ext != "No upcoming tours":
        ext_content = read(ext)
        if not ext_content:
            store(ext)
            send_email(message="New tours out!")
    time.sleep(2)
