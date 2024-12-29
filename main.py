from functions import scrape, extract, URL, read_file, store, send_email
import time

while True:
    scraped = scrape(URL)
    ext = extract(scraped)
    ext_content = read_file(ext)

    if ext != "No upcoming tours":
        if ext not in ext_content:
            store(ext)
            send_email(message="New tours out!")
    time.sleep(2)
