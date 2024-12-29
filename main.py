import requests
import selectorlib

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


def send_email():
    return None


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


scraped = scrape(URL)
ext = extract(scraped)
ext_content = read_file(ext)

if ext != "No upcoming tours":
    if ext not in ext_content:
        store(ext)
        send_email()
