import time
import requests

from selenium import webdriver
from bs4 import BeautifulSoup


def get_imgurl(url):
    driver = webdriver.Chrome('/Users/ginahong/webtoon_dl/chromedriver')
    driver.get(url)
    # time.sleep(5)  # user can see something!

    html = driver.page_source

    allpage = BeautifulSoup(html, "html.parser")
    content = allpage.find("div", {"id": "daumContent"})
    mainpg = content.find("div", {"id": "cMain"})

    beforeimg = mainpg.find("div", {"class": "cont_view"})
    beforelinks = beforeimg.findAll("img")

    links = []
    for l in beforelinks:
        links.append(l['src'])

    return links
