print('##################################################################################################################')
print('#################################문제303. 중앙일보에서 인공지능으로 검색한 기사를 모두 스크롤링 하시오. ###########################')
print('####################################################################')
"""
중앙일보 인공지능 검색했을때 url포맷
    :http://search.joins.com/JoongangNews?page=1&Keyword=인공지능&SortType=New&SearchCategoryType=JoongangNews
각 페이지당 기사의 링크주소가 있는 html구조 
    :<strong class="headline mg"><a href="http://news.joins.com/article/21579002"
    

소스설명 : 
    인공지능 검색한 모든 페이지의 모든 기사들의 내용을 스크롤 한 후, article.txt에 저장한다.
"""
from bs4 import BeautifulSoup
import os
import urllib.request


def get_save_path():
    save_path = input("Enter the file name and file location :" )
    save_path = save_path.replace("\\", "/")
    if not os.path.isdir(os.path.split(save_path)[0]):   # input받은 주소 중 현재 존재하지 않는 폴더를 input했다면, 즉 isdir이 not이라면.
        os.mkdir(os.path.split(save_path)[0])            # 새로 생성해준다.    # ex) input --> d:\data7\ttt.txt 하면 data7이 새로 생김.
    return save_path

def fetch_list_url():
    params = list()
    for i in range(1,20):
        url_format = urllib.request.quote("http://search.joins.com/JoongangNews?page={}&Keyword=인공지능&SortType=New&SearchCategoryType=JoongangNews".format(i), '/:?&=_')
        params.append(url_format)
    return params

def fetch_list_article():
    url_list = fetch_list_url()
    article_url_list = list()
    f = open(get_save_path(),'w',encoding="utf-8")
    for url in url_list:
        page_url = urllib.request.Request(url)
        url_open = urllib.request.urlopen(page_url).read().decode("utf-8")
        soup = BeautifulSoup(url_open, 'html.parser')
        span_find = soup.find_all('span',class_='thumb')
        for idx in range(20):
            try:
                href_find = span_find[idx].find("a")["href"]
                article_url_list.append(href_find)
            except Exception:
                continue

        for article_url in article_url_list:
            article_url_request = urllib.request.Request(article_url)
            article_url_open = urllib.request.urlopen(article_url_request).read().decode("utf-8")
            soup = BeautifulSoup(article_url_open,'html.parser')
            article_find = soup.find('div', class_="article_body")
            result = article_find.get_text(strip=True, separator='\n')
            print(result)
            f.write(result + "\n")
    f.close()

    # print(article_url_list)            # okay

fetch_list_article()
