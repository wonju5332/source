"""
기본값 매개변수와 키워드 매개변수0000000000000000000000000000000000000000000000000000

기본값 매개변수란 입력하지 않으면 기본으로 할당되는 매개변수를 일컫는다.

ex) log(4, 2)      , log (10)   << 밑수를 입력하지 않으면 자연스럽게 기본으로 자연수(e)가 할당된다.


"""


def print_string(txt, cnt=10):
    for i in range(cnt):
        print(txt)

print_string("안녕하세요")  # 매개변수 미할당으로 default 적용된 경우
print_string("안녕하세요",3)  # cnt = 3으로 할당된 경우


print('# 아래와 같이 이름만 넣으면, 소속팀과 직위가 출력되는 함수를 생성하라.')

print_inform(name = '장경원')




def print_inform(name,position='팀장',team ='머신러닝팀'):
    print('이름 = {0}'.format(name))
    print('직위 = {0}'.format(position))
    print('부서 = {0}'.format(team))

print_inform('장경원')



print('# MIT TTT 코딩에서 Function 기능에 default parameter적용한 부분코드..')
"""
class Agent(object):
    def __init__(self, player, verbose = False, lossval = 0, learning = True):
        self.values = {}
        self.player = player
        self.verbose = verbose
        self.lossval = lossval
        self.learning = learning
        self.epsilon = 0.1
        self.alpha = 0.99
        self.prevstate = None
        self.prevscore = 0
        self.count = 0
        enumstates(emptystate(), 0, self)
"""
import math
print(math.gcd(math.gcd(16,18),30))