import requests
import selectorlib
from datetime import datetime

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
    try:
        with open("temp_data.txt", "a") as file:
            file.write(f"{now}, {extracted}" + "\n")
    except:
        with open("temp_data.txt", "w") as file:
            file.write(f"{now}, {extracted}" + "\n")


def read_file(extracted):
    now = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
    try:
        with open("temp_data.txt", "r") as file:
            file_content = file.read()
    except:
        with open("temp_data.txt", "w") as file:
            file.write(f"{now}, {extracted}" + "\n")
        with open("temp_data.txt", "r") as file2:
            file_content = file2.read()
    return file_content
