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
        self.data_list = defaultdict(list)
        self.url_form = 'http://thecheat.co.kr/rb/?m=bbs&bid=cheat&p=2&type=cheat&page_num=&search_term=6&se=&p={}'
        self.set_chrome_driver()
        self.play_crawling()

    def set_chrome_driver(self):
        self.driver = webdriver.Chrome(theCheatCrawler.CHROME_DRIVER_PATH + 'chromedriver.exe')

    #첫 게시글 들어간 후, 아래의 루프페이지를 먼저 순회하여 dict형태의 detail 리턴   #[{goods:컴퓨터,피해액:30000원},{..}, ...{..} ]
    def loop_article(self,article_url):
        self.detail_list = list()
        detail_tuple = namedtuple('detail_info', ['GOODS', 'DAMAGE_MONEY','DAMAGE_SITE','SUSPECT_BANK'])
        detail_url = article_url[0]  #첫페이지-첫게시글에서 출력되는곳에서만 html을 불러옴
        self.driver.get(self.ARTICLE_URL.format(detail_url))
        html = self.driver.page_source
        soup = BeautifulSoup(html,"html.parser")
        IG_listArea = soup.find('div', class_='damageListArea').find('tbody')  # 원 게시글 아래의 나머지 게시글들로부터 출력하려고 함.
        for info in IG_listArea.find_all('tr'):
            goods = info.find('div',class_='goods_div').find('a').get_text(strip=True)  #        제품타입
            damage_money = info.find_all('li')[0].get_text(strip=True) #''값은 NaN값 ok          피해금액
            damage_site = info.find_all('li')[1].get_text(strip=True) #ok                        피해사이트
            suspect_bank = info.find('div', class_='bankNum_div').get_text(strip=True) #ok       거래은행 종류
            '''
            아래 dic을 defaultdict으로 바꿔야함. NaN값이 있는 키를 호출할 수 없는 상태임.
            '''
            detail = detail_tuple(goods,damage_money,damage_site,suspect_bank)
            self.detail_list.append(detail)
        print(self.detail_list[0])
        return self.detail_list


    # 각 게시글의 url을 순회하는 곳  #[조회수, 작성시간, 사건피해내용]
    def fetch_list_url(self,article_url):
        self.info_list = []
        article_tuple = namedtuple('Article_info',['HIT_CNT','UPLOAD_DATE'])
        for url in article_url:
            self.driver.get(self.ARTICLE_URL.format(url))  # 게시글에 접속
            html = self.driver.page_source
            soup = BeautifulSoup(html, "html.parser")
            hit_cnt = soup.select('div.userInfo > div.cont > div.fr > ul > li.inquiry')[0].text #ok  조회수
            upload_date= soup.select('div.userInfo > div.userInfoHead > span')[0].text #ok           작성시간
            # content_text = soup.find('div',id='vContent').get_text(strip=True) #ok                   피해사례 문장
            info = article_tuple(hit_cnt,upload_date) #Article_info(HIT_CNT='조회 7', UPLOAD_DATE='2017.05.27 19:42:56')
            self.info_list.append(info)
        print(self.info_list[0])
        return self.info_list

    def info_to_detail(self,detail,info):
        if len(detail) == len(info):          # key-value 세팅 전에 서로의 개수가 같아야 오류가 나지 않기 때문
            for idx in range(len(detail)-1): #0-58 총 59번
                self.data_list[info[idx]].append(detail[idx])   #data_list 는 클래스 __init__에 선언한 디폴트딕트이다.
        print(self.data_list[0])
        return self.data_list

    def play_crawling(self):
        pages = self.pages
        for page in range(1,pages):
            self.driver.get(self.url_form.format(page))  #url주소
            html = self.driver.page_source
            soup = BeautifulSoup(html, "html.parser")  #1페이지에서의 html주소
            div_find = soup.find_all('div',class_='goods_div')
            article_url = [tag.find('a')['href'] for tag in div_find]   #/rb/?m=bbs&bid=cheat&type=cheat&uid=4568735
            detail = self.loop_article(article_url)  #
            info = self.fetch_list_url(article_url)  # 각 게시글들의 url 주소리스트
            self.info_to_detail(detail,info)  #dict로 연결시켜주는 함수?
            print('#'*10,'파일 저장 중...','#'*10)
            self.data_to_file()
    #데이터 저장 함수
    def data_to_file(self):
        print(self.data_list)

        # with open(theCheatCrawler.FILE_PATH + "kma_crawled.txt", "a", encoding="utf-8") as file:
        #     file.write('======================================================\n')
        #     for key, value in self.data_list.items():
        #         file.write('>> ' + key[0] + ', ' + key[1] + '\n')
        #         for idx in value:
        #             file.write(idx)
        #
        #     file.write('======================================================\n\n')
        #     file.close()


crawler = theCheatCrawler(2)  #일단 매개변수는 페이지수만큼
crawler.play_crawling()