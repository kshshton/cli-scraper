import re
import requests
from bs4 import BeautifulSoup as soup


class Scraper:
    pages: dict = {}


    def add_page_by_url(self, url: str) -> None:
        if re.search(r'(www)?.?\w+\.\w+', url).group(0) is not None:
            self.pages[len(self.pages) + 1] = url
        else:
            print('Wrong url')


    def list_of_pages(self) -> None:
        for index, url in self.pages.items():
            print(f'{index}: {url}')


    def expand_html_of_page(self, key: int) -> None:
        if key in self.pages.keys():
            html = requests.get(self.pages[key]).text
            print(soup(html, 'html.parser').prettify())
        else:
            print("Key doesn't exist")


    def search_tag_on_page(self, tag: str, key: int) -> None:
        if key in self.pages.keys():
            html = requests.get(self.pages[key]).text
            _ = soup(html, 'html.parser')
            print(eval('_.' + tag))
        else:
            print("Key doesn't exist")


    def find_regex_on_page(self, regex: str, key: int) -> None:
        if key in self.pages.keys():
            html = requests.get(self.pages[key]).text
            target = soup(html, 'html.parser').text
            for match in re.finditer(rf'{regex}', target):
                print(match.group(0))
        else:
            print("Key doesn't exist")


