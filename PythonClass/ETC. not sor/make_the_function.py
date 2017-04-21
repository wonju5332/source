# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 10:07:44 2017

@author: sru
"""

import csv

file = open("d:\data\emp_comm.csv",'r')  # 'r' 읽기.
emp_csv = csv.reader(file)   ## emp_csv는 변수명임.
##instr함수##
#####################문제 35. ################

def instr(word, target):
    for i in range(len(word)):
        if word[i] == target:
            return i+1
    return -1  ##False는 -1을 리턴한다. tpye을 intger로 통일위해.

word = 'smith'
result = instr(word,'h')
print(result)
if result == -1:
    print('없다')
else:
    print('있다')
 ## 내장함수인 Find함수도 있음

#####################문제 37.38.39 ################
##이름과 월급과 보너스를 출력하는데 보너스는 월급의 15퍼센트로 출력하기
##위 결과 재출력, 컬럼명도 출력되게 하라.
##위 결과 재출력, 소숫점 이하 나오지 않고, 반올림 되게 하라.
##보너스 출력 시, 소숫점 이하 trunc써서 잘라내기
import csv
import math
file = open("d:\data\emp_comm.csv",'r')
emp_csv = csv.reader(file)
print('이름','월급','보너스')
for list in emp_csv:
    print('round',list[1],list[5],round(int(list[5])*0.15))
    print('trunc',list[1],list[5],math.trunc((int(list[5])*0.15)))

###################문제 41. input 명령어 이용한 연산자함수 사용##############
a = input ('첫번째 숫자를 입력하세요')
b = input ('두번째 숫자를 입력하세요')

result= int(a)+int(b)
print (result)
########################문제42. 숫자 입력받아, 짝수인지 홀수인지 출력되게 하라.
##연산자 : %  P86참고


a = int(input('첫번째 숫자를 입력하세요'))
b = int(input('2번째  숫자를 입력하세요'))
c = [a,b]
d = int(input('숫자입력하세요'))
print(c)
for i in c:
    if i[i-1]%2 == 0:
        print('짝수')
else:
    print('홀수')

if d%2 == 0:
    print ('짝수')
else:
    print ('홀수')
    

## 문제 42. Power 함수 이용하여 아래의 프로그램 구현하라.
## 숫자를 입력하라 ------- 2
## 지수를 입력하라 ------- 3
##          8 입니다.
import math
num = int(input('숫자 입력하세요'))
exp = int(input('지수 입력하세요'))
result = math.pow(num,exp)
print(result)

##########날짜 함수 ##################################
##문제 43. 오늘 날짜를 출력하시오. add_month vs relativedelta

import datetime
today = datetime.date.today()
print(today)

##문제 44. 오늘부터 3달뒤의 날짜를 출력하시오 !

from datetime import date
from dateutil.relativedelta import relativedelta

result =date.today() + relativedelta(months=+3) ##지금 날짜로부터 3개월 후 날짜!!
print (date.today()) 
print (result)

## 또는

import datetime
a = datetime.datetime(2016, 12, 25)
b = datetime.datetime(2017, 3, 14)
from dateutil.relativedelta import relativedelta
c = relativedelta(b, a)
c.months

## 이름, 입사일, 입사한 날짜에서 3달 후의 날짜를 출력하시오 !
from datetime import date
from dateutil.relativedelta import relativedelta
import csv
file = open("d:\data\emp_comm.csv",'r')
emp_csv = csv.reader(file)

for list in emp_csv:
    a = datetime.datetime.strptime(list[4], '%Y-%m-%d')
    print(list[1],list[4],a+relativedelta(days=-17)) ##은총이형이 알려주신 방법, 

   
##문제 46. 올해 2월달의 마지막 날짜를 출력하시오 !
## <Last_day> vs <monthrange>
## 문제47. 오늘부터 요번달 말일까지 총 몇일 남았는지 ?  today().day 일, month 월, year 연
from calendar import monthrange
print(monthrange(2017,4)[1]-date.today().month,'일')  ## day - day (int형)

## 오늘이 무슨 요일인지 출력하시오
import datetime
print (date.today()) #오늘 날짜 확인
print (date.today().weekday())#오늘 요일 확인
days=['monday','tuseday','wednesday','thursday','friday','saturday','sunday']
print(days[0])  ##  <<<이걸 활용한다! 
print(days[date.today().weekday()])

## 문제 49. 이름, 입사한 요일을 출력하시오 !
import datetime
import csv
days = ['monday','tuseday','wednesday','thursday','friday','saturday','sunday']
file = open("d:\data\emp_comm.csv",'r')
emp_csv = csv.reader(file)

for list in emp_csv:
    a = datetime.datetime.strptime(list[4], '%Y-%m-%d')  ##날짜형 변환해준다.
    print(list[1],list[4],days[a.weekday()])

## 문제 50. 오늘날짜에서 하루를 더한 날짜가 어떻게 되는가?
import datetime
print(date.today()+ datetime.timedelta(days=1))

##문제 51.  아래와 같이 실행될 수 있는 사용자 정의 함수를 생성하시오!
## next_day(date.today(), 1 )


def next_day(date,day)
a= datetime.datetime.strptime(date, '%Y-%m-%d')
return (d + datetime, timedelta(days=day))

print(next_day('2017-04-13',2))

##아래와 같이 수행하면, 지정된 날짜에서 돌아오는 요일의 날짜가 출력되게 하시오. XX
##자료형 중 dictionary 자료형 이용해서 수행.

import datetime as dt
def next_day(toDay, wod):
    wods = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
    diff = wods.index(wod)-toDay.weekday()
    return toDay+dt.timedelta(days=diff) if diff > 0 else toDay+dt.timedelta(days=7+diff)

print(next_day(dt.datetime.today().date(), '월요일'))

## 문제 54. 이름, 입사한 날짜부터 오늘까지 총 몇일 근무했는지 출력하시오 !
## datetime.datetime.strptime(list[4], '%Y-%m-%d').date()
import datetime
from calendar import monthrange
import csv
days = ['monday','tuseday','wednesday','thursday','friday','saturday','sunday']
file = open("d:\data\emp_comm.csv",'r')
emp_csv = csv.reader(file)
for list in emp_csv: