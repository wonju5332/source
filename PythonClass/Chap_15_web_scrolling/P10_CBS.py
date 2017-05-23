import urllib.request  # 웹브라우저에서 html 문서를 얻어오기위해 통신하는 모듈
from  bs4 import BeautifulSoup  # html 문서 검색 모듈
import os
import re

def fetch_list_url():
    params = []
    for j in range(1, 30):
        for i in range(0, 15):
            list_url = "http://www.cbs.co.kr/radio/pgm/board.asp?page=" + str(j) + "&pn=list&skey=&sval=&bgrp=2&bcd=00350012&pcd=board&pgm=111&mcd=BOARD2"

            url = urllib.request.Request(list_url)
            res = urllib.request.urlopen(url).read()

            soup = BeautifulSoup(res, "html.parser")
            soup_a = soup.find_all('a', class_='bd_link')[i]['href']

            # 숫자와 ,가 포함되어져 있는 부분을 검색해서 다시 , 로 구분해서 분리
            soup_num = re.search("[0-9,',']{11}", soup_a).group().split(',')
            params.append(soup_num)

    return params


def fetch_detail_url():
    params_2 = fetch_list_url()

    for tag in params_2:
        list_url = 'http://www.cbs.co.kr/radio/pgm/board.asp?pn=read&skey=&sval=&anum='+str(tag[1])+'&vnum='+str(tag[0])+'&bgrp=2&page=2&bcd=00350012&pcd=board&pgm=111&mcd=BOARD2'
        url = urllib.request.Request(list_url)
        res = urllib.request.urlopen(url).read()

        soup = BeautifulSoup(res, "html.parser")
        title = soup.find('td', class_='bd_menu_content').get_text()
        content = soup.find('td', class_='bd_article').get_text()
        print(title)
        print(content)

fetch_detail_url()