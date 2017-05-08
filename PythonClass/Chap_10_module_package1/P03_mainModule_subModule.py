##예제 top_level.py라는 이름으로 저장하고 실행하기
#>> name : __main__


##예제2. sub.py 라는 이름으로 저장하고 실행



print("begining of sub.py ...")
print('name : {0}'.format(__name__))
print("end of sub.py ...")

#예제3) test7.py 라는 이름으로 다음과 같이 실행


#문제 162. 위 import sub만으로 아래의 내용이 출력되는데, 그렇다면 아래 결과를 나오지 않게 할 수 있는 방법은?

# >>sub.py
#    import sub
#    if __name__ = "__main__":
#    실행문

