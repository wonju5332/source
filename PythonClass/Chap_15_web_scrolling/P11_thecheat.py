from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import operator

class theCheatCrawler:
    CHROME_DRIVER_PATH = 'D:\\chromedriver\\'
    FILE_PATH = 'D:\\thecheat_data\\'
    def __init__(self,pages):
        self.pages = pages   #5
        self.data = {}
        self.url_form = 'http://thecheat.co.kr/rb/?m=bbs&bid=cheat&p=2&type=cheat&page_num=&search_term=6&se=&p={}'
        self.set_chrome_driver()
        self.play_crawling()
    def set_chrome_driver(self):
        self.driver = webdriver.Chrome(theCheatCrawler.CHROME_DRIVER_PATH + 'chromedriver.exe')

    def fetch_list_url(self):
        params = list()
        return params


    def play_crawling(self):
        pages = self.pages
        params = list()   #a태그의 링크주소를 담을 곳
        try:
            for page in range(pages):
                self.driver.get(self.url_form.format(page))  #url주소
                html = self.driver.page_source
                soup = BeautifulSoup(html, "html.parser")  #1페이지에서의 html주소
                div_find = soup.find_all('div',class_='goods_div')
                a = [tag.find('a')['href'] for tag in div_find]   #/rb/?m=bbs&bid=cheat&type=cheat&uid=4568735
                print(len(a))

        except:
            print('정상 종료 되었습니다.')

crawler = theCheatCrawler(5)  #일단 매개변수는 페이지수만큼
crawler.play_crawling()