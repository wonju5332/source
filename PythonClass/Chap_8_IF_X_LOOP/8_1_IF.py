# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 09:59:41 2017

@author: sru


IF문 문법

if 조건1:             **조건이 Ture이면 실행이 되고, False이면 실행되지 않음**
    실행문            
elif 조건2:
    실행문
elif 조건3:
    실행문
else:                   << 생략 가능
    실행문
    
    
 **조건이 False로 평가되는 경우??
    1. False
    2. None
    3. 숫자 0   (True = 1)
    4. 비어있는 순서열: '',(),[] ..
    5. 비어있는 딕셔너리 : {}
    
    
"""

## 문제 111. 숫자를 물어보게 하고, 입력했을 때 짝수인지 홀수인지 출력하는 if문을 이용한 코드작성하라.
result = ''
a = int(input('숫자를 입력하세요'))
if a%2 == 0:
    result = '짝수입니다.'
else:
    result = '홀수입니다'
print(result)

## 문제 112. 위의 if문의 예제로 mod함수를 생성하라.

def mod(a):
    if a%2 == 0:
        return '짝수입니다'
    else:
        return '홀수입니다.'
print(mod(7))

## 문제 113. 이름을 물어본 후, 입력하면 해당 사원이 고소득자?저소득자? 출력되게하라.
# sal >= 3000 고소득 / 2000 적당합니다 / 2000 이하 저소득
import pandas as pd
emp = pd.read_csv("d:/data/emp.csv")
a = input('이름이 무엇입니까?').upper()
result = emp['sal'][emp['ename']==a].values[0]

if result >= 3000:
    print('고소득자입니다')
elif result >= 2000:
    print('적당합니다')
else:
    print('저소득자임')
        ### csv로도 해보기.  (아직 못했음.)
import csv
file = open("D:/data/emp.csv")
emp_csv = csv.reader(file)
for list in emp_csv:
    if list[2] == 'KING':
        sal = list[5]

print(sal)

##문제 115. 가우스 공식 1부터 10까지의 숫자의 합을 출력하시오!
## 첫번째 수 입력하라~ 1   두번째 수 입력하라~ 10     1 부터 10 까지의 합은 55 입니다.

a = int(input('첫번째 수 입력하라'))
b = int(input('두번째 수 입력하라'))
d = int(input('공차 입력하라'))
n_num = ((b-a)/d)+1
l_num = a+((n_num-1)*d)
result = (n_num*(a+l_num))/2
print(result)

## 위 문제를 다시 수행하는데, 아래와 같이 큰 숫자를 먼저 입력하면 첫번째 입력한 숫자가
## 두번째 입력한 숫자보다 큽니다. 라는 메세지가 출력되게 하세요.

a = int(input('첫번째 수 입력하라'))
b = int(input('두번째 수 입력하라'))
d = int(input('공차 입력하라'))
temp = ''

if a > b:
    keep = int(input('먼저 입력한 숫자가 너무 크다. 알아서 진행할까요? Y = 1 / N = 0'))
    if keep == 1:
        temp = b
        b = a
        a = temp
        n_num = ((b-a)/d)+1
        l_num = a+((n_num-1)*d)
        result = (n_num*(a+l_num))/2
        print(result)
    else:
        print('계산이 종료되었습니다.')
else:
    n_num = ((b-a)/d)+1
    l_num = a+((n_num-1)*d)
    result = (n_num*(a+l_num))/2
    print(result)
        














