import requests
import selectorlib
import smtplib, ssl
import os
import sqlite3

connection = sqlite3.connect("data.db")

URL = "http://programmer100.pythonanywhere.com/tours/"
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
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    # returns dictionary
    value = extractor.extract(source)["tours"]
    return value


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")
    receiver = os.getenv("EMAIL2")
    my_context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


def store(extracted):
    cursor = connection.cursor()
    row = extracted.split(",")
    row = [item.strip() for item in row]
    cursor.execute("INSERT INTO events VALUES(?,?,?)", row)
    connection.commit()


def read(extracted):
    cursor = connection.cursor()
    row = extracted.split(",")
    row = [item.strip() for item in row]
    band, city, date = row
    cursor.execute("SELECT * FROM events WHERE Band=? AND City=? AND Date=?", (band, city, date))
    rows = cursor.fetchall()
    return rows
