# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 16:20:34 2017

@author: sru
"""
##문제 55. if문을 사용해서, 사원번호가 7788번인 사원의 사원이름과 월급을 출력하라.
#<input 명령어와 if문을 이용한 문제>

import csv
file = open("d:\data\emp_comm.csv",'r')
emp_csv = csv.reader(file)
for list in emp_csv:
    if int(list[5]) == 3000:
        print(list[1],list[5])
        
        
        
        

##문제 56. 월급이 3000 이상인 사원들의 이름과 월급을 출력하라.
##input 과 if 이용
import csv
file = open("d:\data\emp_comm.csv",'r')
emp_csv = csv.reader(file)
for list in emp_csv:
    if int(list[5]) >= 3000:
        print(list[1],list[5])
        

## 문제 57. 1981 년 11월 17이레 입사한 사원들의 이름과 입사일을 출력하시오!
import csv
file = open("d:\data\emp_comm.csv",'r')
emp_csv = csv.reader(file)
for list in emp_csv:
    if list[4] == '1981-11-17':
        print (list[1],list[4])
        
        
        
        
## 문제 58. TTT 관련 문제/ 81년도 입사한 사원들의 이름과 입사일 출력
import csv
file = open("d:\data\emp_comm.csv",'r')
emp_csv = csv.reader(file)
for list in emp_csv:
    if list[4][0:4] == '1981':
        print (list[1],list[4])


### 겨울왕국 긍정 단어 몇개?

    
    
