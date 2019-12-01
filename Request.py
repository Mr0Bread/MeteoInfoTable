import requests
from lxml import html
from bs4 import BeautifulSoup
import html5lib


class Request:
    def __init__(self):
        self.__login_data = {
            "login": "demo",
            "password": "demo"
        }

        self.__headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/78.0.3904.108 Safari/537.36 '
        }

    def get_info_for_table(self):
        with requests.session() as s:
            url = "http://www.lvceli.lv/cms/"
            r = s.post(url, data=self.__login_data, headers=self.__headers)

        soup = BeautifulSoup(r.content, "html5lib")
        self.table = soup.find("table", attrs={"class": "norm", "id": "table-1"})
