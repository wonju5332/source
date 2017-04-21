# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 10:33:55 2017
	append( )	리스트 끝에 새 요소를 추가
	extend( )	기존 리스트에 타 리스트를 이어 붙임
	insert( )	리스트의 특정 위치에 새로운 요소를 입력
	remove( )	리스트 내부의 특정 요소를 삭제
	pop( )	리스트의 마지막 위치의 요소를 제거 (스택 자료 구조)
	index( )	리스트의 특정위치의 요소를 출력할때 사용
	count( )	리스트 요소의 건수를 출력
	sort( )	리스트의 요소를 정렬
	reverse( )	리스트의 요소의 순서를 반대로 뒤집는 명령

@author: sru
"""

## 문제 71. a라는 변수에 list선언 후 input 명령어를 이용하여 a라는 list에 추가할 value물어보고 추가하는 기능 구현


# 내가 한것(틀린거)
a = input('EMP_LIST에 추가할 요소 입력하세요')
emp_list = [a]  

### append 활용한 모범답안.
emp_list=[]
a = input('EMP_LIST에 추가할 요소 입력하세요')
emp_list.append(a)
print(emp_list)

## 문제 72. emp_list 에 추가된 value 를 삭제하는 코드를 구현하시오!.

# emp_list 에 삭제할 요소를 입력하세요 ~ 53

k= input(' emp_list 에 삭제할 요소를 입력하세요 ~')
emp_list.remove(k)
print(emp_list)

##문제 73. emp_list에 요소를 추가하고 삭제하고 갯수를 확인하는 코드를 구현하시오.
#emp_list에 요소를 추가하려면 1번, 삭제하려면 2번, 갯수확인은 3번을 누르세요.
#1번 >>추가할 요소를 입력하세요 ~ d
#2번 >> 삭제할 요소를 입력하세요 ~ f
#3번 >> EMP_LIST에 요소의 개수는 총 N 개입니다.

    
emp_list=[]  ##초기화 될 수 있으니, 한번만 실행하기 , 원하면 for 문 돌리면됨.
a=0
c=0

select = int(input('emp_list에 요소를 추가하려면 1번, 삭제하려면 2번, 갯수확인은 3번을 누르세요.'))
if select == 1:
    a = input('추가할 요소를 입력하세요 ~ ')
    emp_list.append(a)
    print(emp_list)
elif select == 2:
    c = input('삭제할 요소를 입력하세요 ~')
    emp_list.remove(c)
    print(emp_list)
else:
    print(len(emp_list))

##문제 74. 리스트 메소드 중에 sort를 이용해서 월급을 출력할 때 높은것 부터 출력될 수 있도록 하라.
###1.sal_list 라는 empty_list에 emp_list 의 5번째 요소를 for loop로 담아낸다.
#####2.이름과 월급을 출력하는데, 월급이 높은것부터 출력되게 하시오. 

sal_list =[]
import csv
file = open("d:\\data\\emp2.csv", 'r', encoding='euc-kr')
emp_csv = csv.reader(file)
for list in emp_csv:
    sal_list.append(list[5])


sort_list = []

import csv
file = open("d:\\data\\emp2.csv", 'r', encoding='euc-kr')
emp_csv = csv.reader(file)
for list in emp_csv:
    sort_list.append(int(list[5])) ##str >> int로 변환
    sort_list.sort(reverse = True)  ## sort.reverse 정렬
for i in sort_list:   ##list형태의 sort_list를 for문을 통해 값 1개씩 출력.
    print(i)

    """
     sum   ok
     len   ok
     avg   X   -> sum(A) / len(a) 대체
     """    
##월급 max값 구하기  
###sal_list에 sal값 몰아 넣기
####print에서 max함수 넣기
import csv
file = open("D:\\data\\emp2.csv", "r")
emp = csv.reader(file)
sal_list = []
for i in emp:
    sal_list.append(int(i[5]))
print(max(sal_list)) ###max값 이렇게 구하면 됨.

##문제 79. emp list 에서 직업이 SALESMAN인 사원들 중에서의 최대월급을 출력하라.
import csv
file = open("D:\\data\\emp2.csv","r")
emp = csv.reader(file)
sal_list=[]
for i in emp:
    if i[2] == 'SALESMAN':
        sal_list.append(int(i[5]))

print(max(sal_list))
        
 








