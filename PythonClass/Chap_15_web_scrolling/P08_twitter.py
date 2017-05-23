from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import operator

class TwitterCrawler:
    CHROME_DRIVER_PATH = 'D:\\chromedriver\\'
    FILE_PATH = 'D:\\twitter_data\\'
    def __init__(self,search_word,start_date,end_date,routine):
        self.search_word = search_word
        self.start_date = start_date
        self.end_date = end_date
        self.routine = routine
        self.data = {}
        self.url_form = 'https://twitter.com/search?l=&q='+search_word+'%20since%3A'+start_date+'%20until%3A'+end_date+'&src=typd&lang=ko'
        self.set_chrome_driver()
        self.play_crawling()
    def set_chrome_driver(self):
        self.driver = webdriver.Chrome(TwitterCrawler.CHROME_DRIVER_PATH + 'chromedriver.exe')

    def page_scroll_down(self):
        for i in range(0,self.routine):
            self.driver.find_element_by_xpath("//body").send_keys(Keys.END)
            time.sleep(5)

    def data_to_file(self):
        with open(TwitterCrawler.FILE_PATH + self.search_word + ".txt", "w", encoding="utf-8") as file: #PATH\키워드.txt를 쓰기가능한 유니코드파일로 열면서
            print('데이터를 저장하는 중입니다.')  #프린트하며
            for key, value in sorted(self.data.items(), key=operator.itemgetter(0)):   #data 딕셔너리에, 정렬하여 넣겠다.
                # data.items() 에 key 와 value 가 들어있고 그리고 0 번째 요소로 정령하겠다.
                file.write("==" * 30 + "\n")
                file.write(key + "\n")
                file.write(value + "\n")
                file.write("==" * 30 + "\n")


                file.write(value + '\n') #밸류값을 파일에 작성한다.
            file.close()  #파일종료
            print('데이터 저장이 완료되었습니다.')


    def play_crawling(self,):
        try:
            self.driver.get(self.url_form)
            self.page_scroll_down()
            html = self.driver.page_source
            soup = BeautifulSoup(html,"html.parser")
            content_find = soup.find_all("div",class_="content")  #len(18)
            for tag in content_find:
                usertime = tag.find('small', class_='time').find('a')['title'] #타이틀 자체가 값이라서 get_text 안함
                text = tag.find('p')
                # print(text)
                if usertime is not None and text is not None:
                    self.data[usertime] = text.get_text(strip=True)
            self.data_to_file()
            self.driver.quit()
            print(self.data)
        except:
            print('정상 종료 되었습니다.')

crawler = TwitterCrawler('삼성', '2015-02-01', '2017-05-01', 100)
crawler.play_crawling()

