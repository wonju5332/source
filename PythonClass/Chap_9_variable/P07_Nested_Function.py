"""
파이썬에서는 함수 안에 함수를 정의하는 것이 가능하다.
중첩함수는 자신이 소속된 함수의 매개변수에 접근할 수 있다는 특징이 있다.

예제
표준편차를 구하려면? 
1. 평균값 구하는 함수
2. 분산값 구하는 함수
위 두개의 함수를 중첩하여 사용한 후, 루트를 적용하면 표준편차값을 구할 수 있을 것.


"""

import math
def stddev(*args):     #부모 함수가 args라는 가변 매개변수를 선언했다.
    def mean():        #1번함수
        return sum(args)/len(args)      #전체 값을 sum한 후 관측치의 총 갯수로 나눠라. (부모 함수의 가변매개변수를 자식 함수들이 활용하는 모습)
    def var(m):        # 2번함수     var 안에 mean()을 넣었으니.  함수 var에서는 m으로 보는것.
        total = 0       # total default = 0으로 선언해놓아라.
        for x in args: #
            total += (m-x) **2   #    (M-X)^2의 SUM값이기 때문에, 각 관측치들을 for문을 활용, 더해준다.
        return total / (len (args) -1)

    v = var(mean())       #2번자식 안에 1번자식을 넣고 값을 출력 후, 부모가 sqrt적용하여 내보내는 모습.
    return math.sqrt(v)
if __name__ "=="__main__"

stddev(2.3,1.7,1.4,0.7,1.9)

# 문제 156. 가변 매개변수를 이용, 여러개의 숫자를 입력받아 최대공약수를 출력을 해낸 준호의 코드를 가져다가 중첩함수로 구성하시오.

def list(*n):
    def gcdtwo(a, b):

        if min(a, b) == 0:
            return max(a, b)
        return gcdtwo(b, a % b)

    def gcd(a):
        b = gcdtwo(max(a), min(a))

        a.remove(min(a))
        a.remove(max(a))

        a.append(b)
        if max(a) == min(a):
            print('최대공약수는 : ', a[0])
        else:
            gcd(a)

    a = []
    for i in n:
        a.append(i)
    gcd(a)

list(300,500,554,1234)