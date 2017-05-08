"""
import의 역할은 정확하게는 다른 모듈 내의코드에 대한 접근을 가능하게 하는 것이다.
import가 접근 가능하게 하는 코드에는 변수, 함수, 클래스 등이 모두 포함된다.

calculator.py라는 이름으로 저장

new 버튼을 눌러서 새로운 창을 열고 아래의 내용을 코딩한 후 위의 위치와 같은 위치에 calc_tester.py라는 이름으로 저장

import calculator
print( calculator.plus(10,5))

앞에서 썼던 문법 :

import 모듈명

import calculator

print(calculator.plus(10,5))

좀 더 편하게 코딩 : from 모듈명 import 변수 또는 함수

from calculator import plus
from calculator import minus
from calculator import multiply
from calculator import divide

print(plus(10,5)

)

p168 import * 와 같은 코드는 사용하지 않는 것이 좋다. 

이유? 코드가 복잡해지고 모듈의 수가 많아지면 어떤 모듈에 또는 어떤 함수를 불러오고 있는지 파악하기 힘들어진다.


좀~~~~~~더 편하게 코딩 :
                            import calculator as c
                            print(c.plus(10,5))
"""


from PythonClass.Chap_10_module_package1 import calculator as c
print(c.plus(10,5))


##문제 159. 오전에 만들었던 준호의 최대공약수 구하는 함수를 모듈화 하시오 !
# 3개의 함수 스크립트를 junho.py라는 이름으로 저장하기.

from PythonClass.Chap_10_module_package1 import junho as j
j.list(100,50,30,20)  # 파이참에서는 Run으로 돌려야한다.


# 모듈 생성 구문 안에 아래의 내용을 추가한다.

#       if __name__=="__main__":   # 모듈을 불러올 때 이 문장이후의 문장은 수행되지 않도록 한다.  (junho.py에 넣으라는 뜻)


#문제. 160. 표준편차를 출력하는 함수를 모듈화 시켜서 다른 실행창에서 아래와 같이 실행시킬 수 있도록 하라.

from PythonClass.Chap_10_module_package1 import std

std.stddev(2.3, 1.7, 1.4, 0.7, 1.9)     #안되고 있음

