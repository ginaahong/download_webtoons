import time

from selenium import webdriver
from bs4 import BeautifulSoup


def daum_get_imgurl(url):
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

    name = allpage.title.text

    return links, name


def naver_get_imgurl(url):
    driver = webdriver.Chrome('/Users/ginahong/webtoon_dl/chromedriver')
    driver.get(url)
    # time.sleep(5)  # user can see something!

    html = driver.page_source

    allpage = BeautifulSoup(html, "html.parser")
    body = allpage.find("body")
    wrap = body.find("div", {"id": "wrap"})
    container = wrap.find("div", {"id": "container"})
    # print(container)

    content = container.find("div", {"class": "webtoon"})
    # print(content)
    cont2 = content.find("div", {"class": "section_cont wide"})

    viewarea = cont2.find("div", {"class": "view_area"})
    beforeimg = viewarea.find("div", {"class": "wt_viewer"})
    alllinks = beforeimg.findAll("img")

    l_array = []
    for l in alllinks:
        if(l.has_attr('id')):
            l_array.append(l['src'])

    comic_name = allpage.title.text
    comic_epi = cont2.find("div", {"class": "tit_area"}).find(
        "div", {"class": "view"}).find("h3").text

    name = comic_name + comic_epi

    return l_array, name
