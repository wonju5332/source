# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 16:37:12 2017

오라클                    파이썬
in                          in
is null                    ==''
between .. and            (>=  )  & ( <=  )
                                 and도 가능
like                     [0:1]  [-1]
                          정규식 함수  ^,$(시작,끝)



@author: sru
"""

## 문제 59. 아래의 리스트 변수에서 positive 라는 단어는 몇개가 나오는가?
## in 활용

word = ['winter','cold','positive','negative'] ##윈터
sum = 0
for i in word:
    if i == 'positive': ## 사전
        sum = sum+1
print(sum)


## 문제 60. 아래의 리스트 변수에서 po와 ng라는 단어가 몇개가 포함되어있는지 알아봐요
##  IN으로 단어 여러개 비교
word = ['winter','cold','positive','negative']
sum = 0
for i in word:
    if i in ['positive','negative']:
        sum = sum+1
print(sum)

##문제 61. 겨울왕국 대본에 긍정단어 몇개나 ?
##문제62. 직업이 SALESMAN이고 월급1200이상인 사원들의 이름과 직업과 월급을 출력하시오. 
import csv
file = open("D:\data\emp_comm.csv",'r')
emp_csv = csv.reader(file)
for list in emp_csv:
    if (list[2] =='SALESMAN') & (int(list[5]) >= 1200):
        print(list[1],list[2],list[5])
##문제63. 월급이 1000에서 3000사이인 사원들의 이름과 월급을 출력하시오.
import csv
file = open("D:\data\emp_comm.csv",'r')
emp_csv = csv.reader(file)
for list in emp_csv:
    if  int(list[5]) > 1000 & int(list[5]) < 3000:
        print(list[1],list[5])

##문제64. 직업이 ANALST, CLERK 인 사원들의 이름과 월급과 직업을 출력하시오. 
import csv
file = open("D:\data\emp_comm.csv",'r')
emp_csv = csv.reader(file)
for list in emp_csv:
    if  list[2] in ('ANALST','CLERK'):
        print(list[1],list[5])
##문제65. 직업이 ANALST, CLERK 이 아닌 사원들의 이름과 월급과 직업을 출력하시오. 
import csv
file = open("D:\data\emp_comm.csv",'r')
emp_csv = csv.reader(file)
for list in emp_csv:
    if  list[2] not in ('ANALST','CLERK'):
        print(list[1],list[5])

##문제 67. 커미션이 null값을 제외하고 출력하세요.
import csv
file = open("D:\data\emp_comm.csv",'r')
emp_csv = csv.reader(file)
for list in emp_csv:
    if list[6] != '':
        print(list[1],list[6])
##문제 68. 이름의 첫번째 철자가 S로 시작하는 사원들의 이름과 월급을 출력하세요.

import csv
file = open("D:\data\emp_comm.csv",'r')
emp_csv = csv.reader(file)
for list in emp_csv:
    if list[1][0:1] == 'S':
        print(list[1],list[6])
##문제 69. 이름의 두번째 철자가 M인 사원들의 이름과 월급을 출력하라.
import csv
file = open("D:\data\emp_comm.csv",'r')
emp_csv = csv.reader(file)
for list in emp_csv:
    if list[1][1:2] == 'M':
        print(list[1],list[6])

## 문제 70. 이름의 마지막 철자가 H인 사원들의 이름과 월급을 출력하라.
import csv
file = open("D:\data\emp_comm.csv",'r')
emp_csv = csv.reader(file)
for list in emp_csv:
    if list[1][-1] == 'H':        ##뒤에서부터는 -1부터임.
        print(list[1],list[6])