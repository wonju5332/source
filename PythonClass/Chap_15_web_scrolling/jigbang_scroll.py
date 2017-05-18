# https://www.zigbang.com/search/map

import urllib.request
from  bs4 import BeautifulSoup
from selenium import webdriver  #웹 애플리케이션의 테스트를 자동화하기 위한 프레임워크
from selenium.webdriver.common.keys import Keys
import time

binary = 'D:\chromedriver/chromedriver.exe'
# 웹 브라우저를 크롬을 사용할거라서, 크롬 드라이버를 다운받아 위 경로에 둔다.
# 팬텀 js로 하면 백그라운드로 실행할 수 있다.
browser = webdriver.Chrome(binary)  # 브라우저를 인스턴스화 한다.
browser.get("https://www.zigbang.com/search/map")  #네이버의 이미지 검색 url을 받아온다.
elem = browser.find_element_by_id("rooms-textfield")   #검색할 내용 들어가는 곳
# find_elements_by_class_name("")

# 검색어 입력
elem.send_keys("안산역") #케익을 입력후
browser.find_element_by_xpath("//*[@type='button'][@id='btn-room-search']").click()   #찾아보기 버튼 클릭함

# 반복할 횟수
for i in range(1, 2):
    browser.find_element_by_xpath("//body").send_keys(Keys.END)  #그냥 end키만 누른다고 페이지가 load되는게 아니다.
                                                                 #따라서, body부분을 활성화 시킨 후, end키를 2번 눌러라!
    browser.implicitly_wait(3)                                                #한번 누른 후, 이미지 새로생기는걸 기다릴겸, 5초정도 좀 쉬었다가라.

time.sleep(5)   #네트웍이 느릴까봐, 안정성을 위해
html = browser.page_source  #크롬브라우저에서 현재 불러온 소스를 가져온다.
soup = BeautifulSoup(html, "html.parser")   #뷰티풀 수프를 사용해서 html코드를 검색할 수 있도록 설정


# print(soup)
# print(len(soup))

def fetch_list_url():
    params = []
    imgList = soup.find_all("img", class_="lazy")  #이미지 주소가 있는곳이, img태그의 _img클래스이다.
    print(imgList)
    for im in imgList:
        try:
            params.append(im["src"])
        except KeyError:
            pass
    return params


def fetch_detail_url():
    params = fetch_list_url()
    # print(params)
    a = 1
    for p in params:
        # 다운받을 폴더경로 입력
        urllib.request.urlretrieve(p, "d:/naverImages/" + str(a) + ".jpg")
        a = a + 1
fetch_detail_url()
browser.quit()