import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/"

def scrape_url():
    response = requests.get(URL)
    print(response.text)

def main():
    scrape_url()


if __name__ == "__main__":
    main()

