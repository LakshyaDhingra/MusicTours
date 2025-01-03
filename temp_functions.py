import requests
import selectorlib
from datetime import datetime
import sqlite3

connection = sqlite3.connect("temp_data.db")

URL = "http://programmer100.pythonanywhere.com/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/39.0.2171.95 Safari/537.36'}


def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract2.yaml")
    # returns dictionary
    value = extractor.extract(source)["temperatures"]
    return value


def store(extracted):
    now = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
    cursor = connection.cursor()
    row = [now, extracted]
    row = [item.strip() for item in row]
    cursor.execute("INSERT INTO weather VALUES(?,?)", row)
    connection.commit()

