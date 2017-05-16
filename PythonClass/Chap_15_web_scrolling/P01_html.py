"""

HTML 예제
b.html
"""


from bs4 import BeautifulSoup

with open("D:\\python\\source\\PythonClass\\Chap_15_web_scrolling\\b.html") as kimnamhoon:
    soup = BeautifulSoup(kimnamhoon,'html.parser')
print(soup.title.text)


print('############################################################')
print('문제 270. b.html문서에서 p태그에 대한 html을 검색하시오')
print('############################################################')
# print(soup.p)
# print(soup.find('p'))  # p태그 첫번쨰것만
print(soup.find_all('p'))  #p태그 모두




print('############################################################')
print('문제 271. a.html문서에서 a태그에 대한 html을 검색하시오')
print('############################################################')

print(soup.find_all('a'))




print('############################################################')
print('문제 272. b.html문서에서 href링크의 url만 긁어오시오')
print('############################################################')


for link in soup.find_all('a'):
    print(link.get('href'))
# http://example.com/elsie
# http://example.com/lacie
# http://example.com/tillie



print('############################################################')
print('문제 273. text만 긁어오기')
print('############################################################')

with open("D:\\python\\source\\PythonClass\\Chap_15_web_scrolling\\b.html") as knh:
    soup = BeautifulSoup(knh,'html.parser')
print(soup.get_text())



print('############################################################')
print('문제 274. 위의 텍스트를 한줄로 나오게 하라.')
print('############################################################')


print(not soup.get_text(strip=True))   #false




print('############################################################')
print('문제 275. ecologicalpryamid.html문서 다운받아, D드라이브 밑에 넣어요')  #난 패키지폴더
print('############################################################')




print('############################################################')
print('문제 276. 위 html파일을 트리형으로 그림그려보기')
print('############################################################')


#url : https://software.hixie.ch/utilities/js/live-dom-viewer/




print('############################################################')
print('문제 277. 위 문서에서, text 1000000을 출력해보세요')
print('############################################################')

with open("D:\\python\\source\\PythonClass\\Chap_15_web_scrolling\\ecologicalpyramid.html") as eco:
    soup = BeautifulSoup(eco,'html.parser')
# print(soup.find(class_="클래스이름"))
result = soup.find(class_="number")
print(result.get_text())    #1000000


print('############################################################')
print('문제 278. 위 문서에서, number클래스에 있느 모든 텍스트 다 가져오시오.')
print('############################################################')

result_all = soup.find_all(class_="number")

num_list = list()
for i in result_all:
    print(i)
    num_list.append(i.get_text())
print(num_list)


print('############################################################')
print('문제 279. 위 결과에서 아래의 [1000]만 출력하라..')
print('############################################################')

result = soup.find_all(class_="number")[2]
print(result.get_text())




print('############################################################')
print('문제 280. ecological...html에서 fox 출력하라..')
print('############################################################')

#name클래스의 4번째
result = soup.find_all(class_="name")[4]
print(result.get_text())

#트리형식으로 찾아가보기
result = soup.find_all("ul")[2]
print(result.li.div.text)




print('############################################################')
print('문제 281. ecological...html안에 fox라는 텍스트가 있는지만 검색하시오.')
print('############################################################')

result = soup.find(text="fox")
print(result)




print('############################################################')
print('문제 282. ecological...html안에 deer를 검색하시오.')
print('############################################################')


result = soup.find(id="primaryconsumers")
print(result.li.div.text) #deer



print('############################################################')
print('문제 284. ecological...html안에 deer아래 1000이 검색하시오.')
print('############################################################')


result = soup.find_all('div',class_="number")[2]
print(result.string)

div_li_tags = soup.find_all(["div","li"])
all_css_class = soup.find_all(class_=["producerlist","primaryconsumerslist"])




print('############################################################')
print('문제 285. 레이디버그 게시판 ')
print('############################################################')

import urllib.request
from bs4 import BeautifulSoup
import re
import os


def fetch_list_url():
    list_url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
    url = urllib.request.Request(list_url)             #<urllib.request.Request object at 0x02EBE610>
    res = urllib.request.urlopen(url).read().decode("utf-8")
    # 위 두가지 작업을 거치면, url의 html문서를 res변수에 담을 수 있게 된다.
    soup_packtpage = BeautifulSoup(res, "html.parser")    #res에 담긴 html코드를 BeautifulSoup 모듈로 검색하기 위한 작업
    # 위의 ebs 게시판 url 로 접속했을때 담긴 html 코드를
    # soup_packtpage 에 담겠다
    e_reg = re.compile("(완젼)")#완젼 이라는 텍스트를 검색하기 위해, 컴파일을 하여, e_reg에 담음
    a = soup_packtpage.find(text=e_reg)
    print(a)


fetch_list_url()




print('############################################################')
print('문제 286. 레이디버그.html 의 a태그에 있는 애들 모두 출력 ')
print('############################################################')


def fetch_list_url():
    list_url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
    url = urllib.request.Request(list_url)
    res = urllib.request.urlopen(url).read().decode("utf-8")
    soup_packtpage = BeautifulSoup(res, "html.parser")
    # 위의 ebs 게시판 url 로 접속했을때 담긴 html 코드를
    # soup_packtpage 에 담겠다
    e_reg = re.compile("(완젼)")
    a = soup_packtpage.find(text=e_reg)
    print(a)
    soup = BeautifulSoup(res, 'html.parser')
    for link in soup.find_all('a'):
        print(link.get('href'))

fetch_list_url()


print('############################################################')
print('문제 287. 현재 페이지의 게시판 13개의 게시글이 전부 출력되게 하시오. ')
print('         현재 페이지의 게시판 13개의 게시글의 게시시점과 함께 전부 출력되게 하시오. ')
print('############################################################')


def fetch_list_url():
    list_url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
    url = urllib.request.Request(list_url)
    res = urllib.request.urlopen(url).read().decode("utf-8")
    soup = BeautifulSoup(res, 'html.parser')
    a = soup.find_all(class_='con')
    b = soup.find_all(class_='date')
    cnt = 0
    for i in a:
        print(b[cnt].text,i.get_text(strip=True))
        cnt += 1
    print(b[0])
fetch_list_url()



print('############################################################')
print('문제 288. 문제 287번 코드에 for loop를 추가해서 EBS레이디 버그 게시판 글들 모두를 스크롤링하시오 ')
print('############################################################')

#시청자 게시판 url
#http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?c.page= '1..' &hmpMnuId=0&searchKeywordValue=0&bbsId=10059819&searchKeyword=&searchCondition=&searchConditionValue=0&
#페이지 = 15
def fetch_list_url():
    for i in range(1,16):
        url_format = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?c.page={}&hmpMnuId=0&searchKeywordValue=0&bbsId=10059819&searchKeyword=&searchCondition=&searchConditionValue=0&".format(i)
        url = urllib.request.Request(url_format)
        res = urllib.request.urlopen(url).read().decode("utf-8")
        soup = BeautifulSoup(res, 'html.parser')
        sp_find = soup.find('div', class_='postList')   #딱 postlist만! 가져와서
        for tag in sp_find.find_all('li', class_='spot_'):    #postlist의 모든 li태그들의 spot_클래스를 싹 가져온 후 순환하라.
            print(tag.find('span', class_='date').get_text(),end=' ')   #span태그의 date 클래스의 코드 중 글자만 가져오며
            print(tag.find('p', class_='con').get_text(strip=True))     #p태그의 con 클래스의 글자를 가져오며 strip처리한 후 출력하라.
            print()
fetch_list_url()