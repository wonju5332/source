# -*- coding: utf-8 -*-

#################      CONTINUE
# 반복문이 실행되는 동안, 특정 코드블럭은 실행하지 않고 다른 코드블럭만 실행되게 할때 사용하는 문법

print("######################예제")
for i in range(10):
    if i % 2 == 1:  # 2로 나눈 나머지 값이 1이 된다는 것은 i가 무얼 의미하는 것인가?
        continue  # 홀수
    print(i)  # 결과는 짝수만 나오게 됨.

# 문제 131. 숫자를 1부터 10까지 출력하는데 중간에 5는 나오지 않게 하시오!


for i in range(1, 11):      #1~ 10까지라 9까지만 나옴.. 그래서 11함
    if i == 5:
        continue
    print(i)


i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)

############### BREAK          "루프를 중단시키는 역할"

print('##############예제 ###########')

i=0
while (True):
    i = i+1
    if i == 1000:
        print('i가 {0}이 됨. 반복문을 중단함'.format(i))
        break
    print(i)

print('#########문제 132. 함수를 생성하는데 아래와 같이 숫자를 넣어서 실행하면 해당 숫자만큼 숫자가 세로로 출력되게 하라.')


def break_fun(num):
    cnt = 0
    while 1:  # True   or  1:   둘다 트루 표현
        cnt += 1
        print(cnt)
        if cnt == num:
            break


break_fun(10)                 # 여기서 print (함수) 해버리면, return 값이 NONE이기 때문에 그것도 호출됨.

print('#########문제 133. 위 함수 수정해서 결과가 아래와 같이 가로로 출력되게 하라.')

def break_fun(num):
    result = []
    cnt = 0
    while 1:  # True   or  1:   둘다 트루 표현
        cnt += 1
        result.append(cnt)
        if cnt == num: # cnt가 10 입력한 num값이 됬을 때 무한루프를 빠져나온다.
            break         #  Break를 걸며, result 값을 return 한다!
    return result

print(break_fun(10))



