from urllib.parse import urlparse
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class ForeignSite(object):
    JOURNALLWW = "journals.lww.com"
    THELANCET = "www.thelancet.com"

    def __init__(self, url, id, name, year):
        self.url = url
        self.id = id
        self.name = name
        self.year = year
        self.driver = webdriver.Chrome(ChromeDriverManager().install())


    def get_site_parser(self):
        self.driver.get(self.url)

        if self.JOURNALLWW in self.driver.current_url:
            return "lww"
        elif self.THELANCET in self.driver.current_url:
            return "lancet"

    def __split_url(self):
        return urlparse(self.url).netloc