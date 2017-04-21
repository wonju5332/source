# -*- coding: utf-8 -*-

"""

Pandas 를 이용한 문법들

1. 판다스 기본문법
2. 판다스 연산자
3. 판다스 이용한 서브쿼리
4. 판다스 이용한 조인


Pandas를 이용하지 않는 조인

1. for loop문을 중첩해서 문제를 해결
2. 딕셔너리 데이터 타입을 이해 ( MIT코드에서 중요하게 쓰임)


파이썬 데이터 구조 3가지  :   1. 리스트      2. 튜플       3. 딕셔너리
                                [ 와 ]         ( 와 )          { 와 }
"""

print ('##################문제 134. 아래와 같이 딕셔너리 형태의 데이터를 만들고 출력하시오#########')

emp_dic = {'mgr':'7788','sal':'1100','deptno':'20','comm':'0',
             'job':'CLERK','hiredate':'1983-01-15','empno':'7876', 'ename':'ADAMS'}
print(type(emp_dic))         # dict 타입


print ('##################문제 135. 6장에서 배운 for loop를 이용해서 emp2.csv 를 읽어와서 emp_dic 라는 딕셔너리 데이터 유형을 만드시오#####')

import csv
file = open("D:/data/emp2.csv")
emp_csv = csv.reader(file)
emp = []  #비어있는 리스트 변수 선언                   csv를 dict에 append하고자 하였으나, dict엔 append기능 X

for i in emp_csv:
    emp.append({'empno' : i[0], 'ename' : i[1], 'job' : i[2], 'mgr' : i[3], 'hiredate' : i[4],
    'sal' : i[5], 'comm' : i[6], 'deptno' : i[7]})

 # Type Dict      즉, 리스트 안에 딕셔너리를 넣었다!

print ('##################문제 136. emp 딕셔너리 변수에서 이름만 출력하시오 #############')

for i in emp:
    print(i['job'])       #좌측처럼 키값을 입력해주면, 키에 할당된 value값이 나온다..PRESIDENT..CLERK..

print ('##################문제 137. emp 딕셔너리 변수에서 월급과 직업만 출력하시오 #############')

for emp_dic in emp:
    print(emp_dic['sal'],emp_dic['job'])

print ('문제 138. dept.csv를 읽어서 딕셔너리 데이터 구조를 저장하고 아래와 같이 수행/ deptno, dname, loc ')

import csv
file = open("D:/data/dept.csv")
dept_csv = csv.reader(file)
dept = []
for i in dept_csv:
    dept.append({'deptno':i[0],'dname':i[1],'loc':i[2]})
print(dept)
for i in dept:
    print(i['deptno'],i['dname'],i['loc'])


print ('문제 139  emp.csv와 dept.csv를 각각 읽어서 emp_dic, dept_dic 딕셔너리 자료형으로 만드는 스크립트를 하나로 합치시오 !')

import csv
emp_file = open('d:/data/emp2.csv')
dept_file = open('d:/data/dept.csv')
emp_csv = csv.reader(emp_file)
dept_csv = csv.reader(dept_file)
emp = []
dept = []
for i in emp_csv:
    emp.append({'empno' : i[0], 'ename' : i[1], 'job' : i[2], 'mgr' : i[3], 'hiredate' : i[4],
    'sal' : i[5], 'comm' : i[6], 'deptno' : i[7]})       # emp

for j in dept_csv:
    dept.append({'deptno':j[0],'dname':j[1],'loc':j[2]}) # dept




print ('문제 140  emp와 dept라는 딕셔너리 자료구조를 만드는 스크립트와 중첩 for lopp문을 이용해서 emp와 dept를 조인시켜서 ename과 loc를 출력하시오.')



for e in emp:  # emp 딕셔너리를 가져온 후
    for d in dept:  #dept테이블에 가서
        if e['deptno'] == d['deptno']:  #emp의 deptno와 dept의 dept와 같은 것을 찾아라.
            print( e['ename'], d['loc'])  #ename과 loc 출력

######## EMP는 row 14건이므로, loop = 14번 돌며, dept = 4건이므로,  14 X 4 씩 loop돈다.  " NESTED LOOP JOIN 방법"

print('문제 141. 부서위치가 DALLAS인 사원들의 이름과 부서위치를 출력하시오.')

for e in emp:
    for d in dept:
        if e['deptno'] == d['deptno']:     #deptno 가 같으면
            if d['loc'] =='DALLAS':         # 그 와중에 D.LOC가 DALLAS이면, 다음을 출력하라.
                print(e['ename'],d['loc'])


print('문제 142. 위 스크립트를 이용해서 조인 함수를 생성하시오.')



def join(tab1,tab1_col,tab2,tab2_col,key):
    for i in tab1:
        for j in tab2:
            if i[key] == j[key]:
                print(i[tab1_col],j[tab2_col])

join(emp,'ename', dept,'loc', 'deptno')

dept
print('문제 143. PANDAS를 이용해서 ename과 loc를 출력하시오.')

import pandas as pd
emp = pd.read_csv("d:/data/emp.csv")
dept = pd.read_csv("d:/data/dept.csv")

result = pd.merge(emp,dept,on='deptno')
print(result[['ename','loc']])

print('문제 143. 부서위치가 DALLAS 인 사원들의 이름과 부서위치를 출력하시오! ')

import pandas as pd
emp = pd.read_csv("d:/data/emp.csv")
dept = pd.read_csv("d:/data/dept.csv")

result = pd.merge(emp,dept,on='deptno')
print(result[['ename','loc']][result['loc']=='DALLAS'])

print('문제 145. 이름과 부서위치를 출력하는데 아래와 같이 Outer Join 을 구현하시오 ! ') ###      OUTER JOIN

import pandas as pd
emp = pd.read_csv("d:/data/emp.csv")
dept = pd.read_csv("d:/data/dept.csv")
result = pd.merge(emp,dept,on='deptno', how = 'right')  # R. 아우터 조인

print(result[['ename','loc']])

