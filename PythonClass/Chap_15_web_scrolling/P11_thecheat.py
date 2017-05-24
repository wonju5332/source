"""
더 치트 사이트 크롤링 제작하기


hit_cnt = '조회 9'  --> 9로 치환해야함



soup.select(self,selector,..)

"""
from collections import namedtuple
from bs4 import BeautifulSoup
from selenium import webdriver
from collections import defaultdict
import re





class theCheatCrawler:
    CHROME_DRIVER_PATH = 'D:\\chromedriver\\'
    FILE_PATH = 'D:\\thecheat_data\\'
    ARTICLE_URL = 'http://thecheat.co.kr/{}'

    def __init__(self,pages):
        self.pages = pages   #5
        self.data = {}
        self.url_form = 'http://thecheat.co.kr/rb/?m=bbs&bid=cheat&p=2&type=cheat&page_num=&search_term=6&se=&p={}'
        self.set_chrome_driver()
        self.play_crawling()

    def set_chrome_driver(self):
        self.driver = webdriver.Chrome(theCheatCrawler.CHROME_DRIVER_PATH + 'chromedriver.exe')

    def fetch_list_url(self,article_url):
        params = list()
        user_dict = defaultdict(list)
        for url in article_url:
            self.driver.get(self.ARTICLE_URL.format(url))  # 게시글에 접속
            html = self.driver.page_source
            soup = BeautifulSoup(html, "html.parser")
            damageInfoSection= soup.find('div',class_='damageInfoSection')
            a = [ for i in damageInfoSection.find_all('tr')]
            print(a)
                # a = i.find_all[0]('th').get_text(strip=True)  #사기사건 발생일
                # b = i.find_all[1]('th').get_text(strip=True)  #사이트명(URL)
                # c = i.find_all[3]('th').get_text(strip=True)  #거래 물품 종류
                # d = i.find_all[4]('th').get_text(strip=True)  #피해금액
                # print(a,b,c,d)
            # fround_date = damageInfoSection.find('td').find('b').get_text(strip=True)

            # fround_date = soup.find(table,)
            # print(froud_date)
            # container > div > div.damageInfoArea > div:nth-child(3) > table > tbody > tr:nth-child(2) > td:nth-child(2)
            # container > div > div.damageInfoArea > div:nth-child(3) > table > tbody > tr:nth-child(2) > td:nth-child(4)



            hit_cnt = soup.select('div.userInfo > div.cont > div.fr > ul > li.inquiry')[0].text
            upload_date= soup.select('div.userInfo > div.userInfoHead > span')[0].text


            # print(item_type)
            # if hit_cnt is not None and upload_date is not None:
            #     user_dict['hit_cnt']=hit_cnt
            #     user_dict['upload_date']=upload_date

            # if hit_body is not None and upload_time_body is not None:
            #     self.data[upload_time_body.text] = hit_body.get_text(strip=True)
            #     print(self.data)


    def play_crawling(self):
        pages = self.pages
        try:
            for page in range(pages):
                self.driver.get(self.url_form.format(page))  #url주소
                html = self.driver.page_source
                soup = BeautifulSoup(html, "html.parser")  #1페이지에서의 html주소
                div_find = soup.find_all('div',class_='goods_div')
                article_url = [tag.find('a')['href'] for tag in div_find]   #/rb/?m=bbs&bid=cheat&type=cheat&uid=4568735
                self.fetch_list_url(article_url)

        except:
            print('정상 종료 되었습니다.')

crawler = theCheatCrawler(5)  #일단 매개변수는 페이지수만큼
crawler.play_crawling()