import requests
import selectorlib
import smtplib, ssl
import os

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
    try:
        with open("data.txt", "a") as file:
            file.write(extracted + "\n")
    except:
        with open("data.txt", "w") as file:
            file.write(extracted + "\n")


def read_file(extracted):
    try:
        with open("data.txt", "r") as file:
            file_content = file.read()
    except:
        with open("data.txt", "w") as file:
            file.write(extracted + "\n")
        with open("data.txt", "r") as file2:
            file_content = file2.read()
    return file_content