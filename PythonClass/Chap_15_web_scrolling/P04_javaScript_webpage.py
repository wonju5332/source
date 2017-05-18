
"""
기존 페이지번호가 바뀜에 따라 url주소가 바뀌던 홈페이지에선 필요없으나,
자바스크립트의 경우 홈페이지가 바뀌지 않으니, 다음의 과정을 추가적으로 진행해야 함

request_header = urllib.parse.urlencode({"page": i})    # 출력 >> page=1 .. 30
request_header = request_header.encode("utf-8")         # 출력 >> b'page=1' .. b'page=30'
url = urllib.request.Request(url_format,request_header) # 출력 >> <urllib.request.Request object at 0x00620A10>
res = urllib.request.urlopen(url).read().decode("utf-8")# 출력 >> 각 페이지에서의 html소스 출력
"""

print('문제 304. 서울시 응답소 게시판의 웹피이지')



# import urllib.request
#
# def fetch_list_url():
#     # params = list()
#     # for i in range(1,30):   #1번부터 30번페이지 까지 순환하라
#     url_format = "http://eungdapso.seoul.go.kr/Shr/Shr01/Shr01_lis.jsp"
#     request_header = urllib.parse.urlencode({"page": 1})  # 출력 >> page=1 .. 30
#     request_header = request_header.encode("utf-8") #위에서 출력한 값 자신을 utf-8로 인코딩하겠다.   b'page=1'
#     url = urllib.request.Request(url_format,request_header)  #url주소의 html과 페이지정보 두개 요청드립니다.   # 출력 >> <urllib.request.Request object at 0x00620A10>
#     res = urllib.request.urlopen(url).read().decode("utf-8")
# fetch_list_url()


print('문제 305. 위 1페이지의 html문서 중 li태그의 class="pclist_list_tit2"를 검색하라')
print('문제 306. 위 결과에 연장하여, a태그에 해당하는 부분만 검색되게 하시오')
print('문제 307. 정규식 모듈인 re를 이용해서 위의 결과에서 숫자만 뽑아내시오.')
print('문제 308. 현재 페이지의 모든 href의 숫자들이 출력되게 하시오.')
print('문제 309. 밑의 게시 페이지 번호 1번부터 30번까지의 href숫자값을 모두 가져오시오.')
print('문제 310. params라는 비어있는 리스트 변수에 위의 결과를 담고 리턴하게끔 위 함수를 수정하라.')
print('문제 311. 위 게시글에 대한 href숫자 20170504003012를 가지고 상세 게시판 글을 스크롤링 하는 fetch_href_url() 함수 생성하라.')
print('문제 312. 위 html문서에서 div태그의 form_table 클래스 부분만 검색하라.')
print('문제 314. 제목을 title2라는 변수에 담고 출력하시오.')
print('문제 315. 민원 내용을 question 이라는 변수에 담으시오.')
print('문제 316. 답변을 answer변수에 담으시오..')
print('문제 317. 방금 생성한 텍스트 파일을 가지고 R에서 워드 클라우드로 그리시오.')
import urllib.request
import re
import os
from bs4 import BeautifulSoup
def get_save_path():
    save_path = input("Enter the file name and file location :" )
    save_path = save_path.replace("\\", "/")
    if not os.path.isdir(os.path.split(save_path)[0]):   # input받은 주소 중 현재 존재하지 않는 폴더를 input했다면, 즉 isdir이 not이라면.
        os.mkdir(os.path.split(save_path)[0])            # 새로 생성해준다.    # ex) input --> d:\data7\ttt.txt 하면 data7이 새로 생김.
    return save_path

def fetch_list_url():
    params = list()
    for i in range(1,30):   #1번부터 30번페이지 까지 순환하라
        url_format = "http://eungdapso.seoul.go.kr/Shr/Shr01/Shr01_lis.jsp"
        request_header = urllib.parse.urlencode({"page": i})  # 출력 >> page=1 .. 30
        request_header = request_header.encode("utf-8") #위에서 출력한 값 자신을 utf-8로 인코딩하겠다.   b'page=1'
        url = urllib.request.Request(url_format,request_header)  #url주소의 html과 페이지정보 두개 요청드립니다.   # 출력 >> <urllib.request.Request object at 0x00620A10>
        res = urllib.request.urlopen(url).read().decode("utf-8")
        soup = BeautifulSoup(res,'html.parser')
        li_find = soup.find_all('li',class_='pclist_list_tit2')
        for idx in range(len(li_find)):
            href_find = li_find[idx].find("a")["href"]
            href_address = re.search("[0-9]{14}",href_find).group()   #숫자 0~9까지 해당하는 값 / 14개를 href_find로부터 가져와라.
            params.append(href_address)
    return params


def fetch_href_url():
    url_list = fetch_list_url()
    detail_url = "https://eungdapso.seoul.go.kr/Shr/Shr01/Shr01_vie.jsp"
    f = open(get_save_path(), 'w', encoding="utf-8")
    for address in url_list:
        request_header = urllib.parse.urlencode({"RCEPT_NO": '{}'.format(address)})
        request_header = request_header.encode("utf-8")
        url = urllib.request.Request(detail_url,request_header)
        res = urllib.request.urlopen(url).read().decode("utf-8")
        soup = BeautifulSoup(res, "html.parser")
        div_find = soup.find("div",class_="form_table")
        tables_find = div_find.find_all("table")
        td_find = tables_find[0].find_all("td")
        question_find = tables_find[1].find("div",class_="table_inner_desc")
        answer_find = tables_find[2].find("div", class_="table_inner_desc")

        get_date  = td_find[1].get_text()
        get_title = td_find[0].get_text()
        get_question = question_find.get_text(strip = True)
        get_answer = answer_find.get_text(strip = True)

        print(get_date,get_title)
        print(get_question)
        print(get_answer)
        f.write("==" * 30 + "\n")
        f.write(get_title+ "\n")
        f.write(get_date + "\n")
        f.write(get_question + "\n")
        f.write(get_answer + "\n")
        f.write("=="*30+"\n")
    f.close()
fetch_href_url()

