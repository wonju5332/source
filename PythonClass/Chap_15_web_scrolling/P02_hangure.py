"""
한겨레 신문사 웹스크롤링 하기
해당 url주소 :
    http://search.hani.co.kr/Search?command=query&keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&
    media=news&sort=d&period=all&datefrom=2000.01.01&dateto=2017.05.17&pageseq=0
해당 url주소 py파일 : P02_hangure

주요 메소드 
         1. urllib.request 모듈
            : 웹 브라우져에서 html문서를 얻어오기 위해 통신하기 위한 모듈
         2. soup.find_all('태그명')
            : 전체 HTML소스 중 태그명에 해당하는 소스를 '시퀀스' 형태로 호출 
        3. soup.find("태그명")["하위 태그명"]
            : 태그명의 하위 

문자를 담는 주요 세트
        1. ansi code : 영문
        2. uni code(UTF-8) : 한글, 중국어   (2byte/글자 한개)

"""

import urllib.request  # 웹 브라우져에서 html문서를 얻어오기 위해 통신하기 위한 모듈
from bs4 import BeautifulSoup


# def fetch_list_url():
#     url_format = "http://search.hani.co.kr/Search?command=query&keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&media=news&sort=d&period=all&datefrom=2000.01.01&dateto=2017.05.17&pageseq=0"
#     url = urllib.request.Request(url_format)  # url요청에 따른 http통신 헤더값을 얻기 위함
#     res = urllib.request.urlopen(url).read().decode("utf-8")  # 영어가 아닌, 한글을 긁어오기 위해 디코딩
#     soup = BeautifulSoup(res, 'html.parser')  # res html문서를 Bs모듈로
#     dt_find = soup.find_all('dt')
#     for i in dt_find:
#         print(i)
#
#
# fetch_list_url()


print('##################################################################################################################')
print('#################################문제291. 위의 HTML문서에서 p태그에 해당하는 html문서들만 검색하시오 ###########################')
print('##################################################################################################################')

# def fetch_list_url():
#     url_format = "http://search.hani.co.kr/Search?command=query&keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&media=news&sort=d&period=all&datefrom=2000.01.01&dateto=2017.05.17&pageseq=0"
#     url = urllib.request.Request(url_format)  # url요청에 따른 http통신 헤더값을 얻기 위함
#     res = urllib.request.urlopen(url).read().decode("utf-8")  # 영어가 아닌, 한글을 긁어오기 위해 디코딩
#     soup = BeautifulSoup(res, 'html.parser')  # res html문서를 Bs모듈로
#     dt_find = soup.find_all('p')
#     for i in dt_find:
#         print(i)
#
#
# fetch_list_url()




print('##################################################################################################################')
print('#################################문제291. 위의 결과 리스트 요소 중 0번째 요소만 검색하시오 ###########################')
print('#################################문제292. 위 결과에서 P태그 밑의 a 태그속 href링크만 가져오시오! ###########################')
print('##################################################################################################################')

def fetch_list_url():
    url_format = "http://search.hani.co.kr/Search?command=query&keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&media=news&sort=d&period=all&datefrom=2000.01.01&dateto=2017.05.17&pageseq=0"
    url = urllib.request.Request(url_format)  # url요청에 따른 http통신 헤더값을 얻기 위함
    res = urllib.request.urlopen(url).read().decode("utf-8")  # 영어가 아닌, 한글을 긁어오기 위해 디코딩
    soup = BeautifulSoup(res, 'html.parser')  # res html문서를 Bs모듈로
    p_find = soup.find_all('p')[0]          #p태그 찾기
    p_find2 = soup.find_all('p')[1]          #p태그 찾기
    print(p_find)
    print(p_find2)
    href_find = p_find.find("a")["href"]    #P태그 안에서 a태그를 찾은 후, href주소만 가져와라
    print(href_find)                        #href 출력
    # return p_find


fetch_list_url()
print('##################################################################################################################')
print('#################################문제293. 현재 페이지의 href의 모든 요소를 다 검색하도록 for loop활용하시오.###########################')
print('##################################################################################################################')


# def fetch_list_url():
#     url_format = "http://search.hani.co.kr/Search?command=query&keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&media=news&sort=d&period=all&datefrom=2000.01.01&dateto=2017.05.17&pageseq=0"
#     url = urllib.request.Request(url_format)  # url요청에 따른 http통신 헤더값을 얻기 위함
#     res = urllib.request.urlopen(url).read().decode("utf-8")  # 영어가 아닌, 한글을 긁어오기 위해 디코딩
#     soup = BeautifulSoup(res, 'html.parser')  # res html문서를 Bs모듈로
#     p_find = soup.find_all('p')  # p태그 찾기
#     idx = 0                      # idx
#     for p_tag in p_find:
#         href_find = p_find[idx].find("a")["href"]  # P태그 안에서 a태그를 찾은 후, href주소만 가져와라
#         print(href_find)  # href 출력
#         idx += 1
# fetch_list_url()



print('##################################################################################################################')
print('#################################문제294. p태그가 아닌, dt태그에서 href url을 가져오도록 코드를 수정하라.###########################')
print('##################################################################################################################')


# def fetch_list_url():
#     url_format = "http://search.hani.co.kr/Search?command=query&keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&media=news&sort=d&period=all&datefrom=2000.01.01&dateto=2017.05.17&pageseq=0"
#     url = urllib.request.Request(url_format)  # url요청에 따른 http통신 헤더값을 얻기 위함
#     res = urllib.request.urlopen(url).read().decode("utf-8")  # 영어가 아닌, 한글을 긁어오기 위해 디코딩
#     soup = BeautifulSoup(res, 'html.parser')  # res html문서를 Bs모듈로
#     dt_find = soup.find_all('dt')  # p태그 찾기
#     # print(dt_find)
#     for idx in range(20):
#         try:
#             href_find = dt_find[idx].find("a")["href"]
#             print(href_find)
#         except Exception:
#             continue
# fetch_list_url()


print('##################################################################################################################')
print('#################################문제295. 밑에 페이지 번호 20개 까지의 모든 href url을 가져오시오.###########################')
print('##################################################################################################################')


def fetch_list_url():
    params = list()
    for i in range(0,19):
        url_format = "http://search.hani.co.kr/Search?command=query&keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&media=news&sort=d&period=all&datefrom=2000.01.01&dateto=2017.05.17&pageseq={}".format(i)
        params.append(url_format)  #params리스트에 모든 url주소 담김
        # print(params)
        url = urllib.request.Request(params[i])  # url요청에 따른 http통신 헤더값을 얻기 위함
        res = urllib.request.urlopen(url).read().decode("utf-8")  # 영어가 아닌, 한글을 긁어오기 위해 디코딩
        soup = BeautifulSoup(res, 'html.parser')  # res html문서를 Bs모듈로
        dt_find = soup.find_all('dt')  # p태그 찾기
        for idx in range(20):
            try:
                href_find = dt_find[idx].find("a")["href"]
                # print(href_find)
            except Exception:
                continue
    return params
        # print(params)
        # return params
fetch_list_url()





print('##################################################################################################################')
print('#################################문제296. 상세기사 검색하는 url을 아무거나 하나 선택하고 이 url을 가지고###########################')
print('#################################문제297. 상세기사 내용을 출력하게 하는 fetch_list_url2() 라는 함수를 생성하라.###########################')
print('##################################################################################################################')

"""
이 소스는 0~20페이지 중 랜덤으로 하나 고른 후,
선택된 페이지에서의 기사들 중 하나의 기사를 랜덤으로 고른 후,
기사를 가져온다.

# """
# import random
# def fetch_list_url_article():
#     params = list()
#     for i in range(0,19):
#         url_format = "http://search.hani.co.kr/Search?command=query&keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&media=news&sort=d&period=all&datefrom=2000.01.01&dateto=2017.05.17&pageseq={}".format(i)
#         params.append(url_format)  #params리스트에 모든 url주소 담김
#     random.shuffle(params)
#     fetch_url = params[0]
#     print(fetch_url)
#     url = urllib.request.Request(fetch_url)  # url요청에 따른 http통신 헤더값을 얻기 위함
#     res = urllib.request.urlopen(url).read().decode("utf-8")  # 영어가 아닌, 한글을 긁어오기 위해 디코딩
#     soup = BeautifulSoup(res, 'html.parser')  # res html문서를 Bs모듈로
#     dt_find = soup.find_all('dt')  # p태그 찾기
#     article_list = list()
#     for idx in range(20):
#         try:
#             href_find = dt_find[idx].find("a")["href"]
#             article_list.append(href_find)
#         except Exception:
#             continue
#     random.shuffle(article_list)
#     fetch_article = article_list[0]
#     article_url = urllib.request.Request(fetch_article)
#     article_res = urllib.request.urlopen(article_url).read().decode("utf-8")
#     article_soup = BeautifulSoup(article_res, 'html.parser')
#     article_find = article_soup.find('div', class_="article-text")
#     print(type(article_find))   #<class 'bs4.element.Tag'>
#     print(article_find.get_text())  #type이 element.Tag여야만 get_text() 가 가능하다.
#
# fetch_list_url_article()





print('##################################################################################################################')
print('#################################문제300.fetch_list_url() 함수가 리턴하는 params의 url값들을 ###########################')
print('#################################fetch_list_url2() 에서 호출해 오게 하시오.###########################')
print('#################################문제301.위 스크립트에 for loop를 입혀서 ###########################')
print('#################################상세기사 출력하도록 하시오. ###########################')
"""
모든 페이지의 모든 기사들의 상세기사 내용 스크롤링하기
"""
# def fetch_list_url():
#     params = list()             #빈 리스트 선언
#     for i in range(0,19):       #페이지 0~19, 즉 20페이지를 순회하겠다.
#         url_format = "http://search.hani.co.kr/Search?command=query&keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&media=news&sort=d&period=all&datefrom=2000.01.01&dateto=2017.05.17&pageseq={}".format(i)
#         params.append(url_format)  # 빈 리스트에 모든 url주소를 추가한다.
#     return params
# fetch_list_url()
#
#
#
#
# def fetch_list_url2():
#     params2 = fetch_list_url()  #url주소 리스트를 받아옴.
#     for i in params2:
#         url = urllib.request.Request(i)
#         res =  urllib.request.urlopen(url).read().decode("utf-8")
#         soup = BeautifulSoup(res, 'html.parser')
#         dt_find = soup.find_all('dt')  # p태그 찾기
#         article_list = list()
#         for idx in range(20):
#             try:
#                 href_find = dt_find[idx].find("a")["href"]
#                 article_list.append(href_find)
#             except Exception:
#                 continue
#         for article in article_list:
#             article_url = urllib.request.Request(article)
#             article_res = urllib.request.urlopen(article_url).read().decode("utf-8")
#             article_soup = BeautifulSoup(article_res, 'html.parser')
#             article_find = article_soup.find('div', class_="article-text")
#             print(article_find.get_text(strip=True))
#
# fetch_list_url2()
#





print('##################################################################################################################')
print('#################################문제302. 인공지능을 검색한 한겨레 신문사 기사 전체를 d드라이브 밑에 ###########################')
print('######################################## data7 이라는 폴더에 생성되게 하시오. ############################')


import os

def get_save_path():
    save_path = input("Enter the file name and file location :" )
    save_path = save_path.replace("\\", "/")
    if not os.path.isdir(os.path.split(save_path)[0]):   # input받은 주소 중 현재 존재하지 않는 폴더를 input했다면, 즉 isdir이 not이라면.
        os.mkdir(os.path.split(save_path)[0])            # 새로 생성해준다.    # ex) input --> d:\data7\ttt.txt 하면 data7이 새로 생김.
    return save_path

def fetch_list_url():
    params = list()             #빈 리스트 선언
    for i in range(0,19):       #페이지 0~19, 즉 20페이지를 순회하겠다.
        url_format = "http://search.hani.co.kr/Search?command=query&keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&media=news&sort=d&period=all&datefrom=2000.01.01&dateto=2017.05.17&pageseq={}".format(i)
        params.append(url_format)  # 빈 리스트에 모든 url주소를 추가한다.
    return params

def fetch_list_url2():
    params2 = fetch_list_url()  #url주소 리스트를 받아옴.
    f = open(get_save_path(),'w',encoding="utf-8")   #save_path를 호출하며, write할것이고, 유니코드로 인코딩!
    print(type(f))
    for i in params2:
        url = urllib.request.Request(i)
        res = urllib.request.urlopen(url).read().decode("utf-8")
        soup = BeautifulSoup(res, 'html.parser')
        dt_find = soup.find_all('dt')  # p태그 찾기
        article_list = list()
        for idx in range(20):
            try:
                href_find = dt_find[idx].find("a")["href"]
                article_list.append(href_find)
            except Exception:
                continue
        for article in article_list:
            article_url = urllib.request.Request(article)
            article_res = urllib.request.urlopen(article_url).read().decode("utf-8")
            article_soup = BeautifulSoup(article_res, 'html.parser')
            article_find = article_soup.find('div', class_="article-text")
            result = article_find.get_text(strip=True, separator = '\n')
            f.write(result+"\n")
    f.close()

fetch_list_url2()
