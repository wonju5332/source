# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 11:02:42 2017

@author: sru
"""


for i in range(0,5):       
    print(i)
print('#############')

for i in range(5):
    print(i)
print('#############')

for i in range(1,10,2):    ## 1, 3, 5, 7 , 9
    print(i)              
print('#############')

print('########### 문제 117. 구구단 2단을 출력하라. ###########')

for i in range(1,10):
    a = 2* i
    print('2 X',i,'=',a)
print('#############2단부터 9단까지? ')

for i in range(2,10):
    for j in range(1,10):
        print(i,' X ',j,' = ',i*j)
    print('\n')
    
print('########### 문제 118. 아래의 결과를 출력하시오. ###########')
"""
★
★★
★★★
★★★★
★★★★★
★★★★★★
★★★★★★★
★★★★★★★★
★★★★★★★★★
"""
for i in range(0,10):
    print('★'*i)
print('#######################')
star = ''
for i in range(0,10):
    star = star+'★'
    print(star)
print('########### 문제 119. 아래의 결과를 출력하시오.(반대로 ###########')
"""
★★★★★★★★★★
★★★★★★★★★
★★★★★★★★
★★★★★★★
★★★★★★
★★★★★
★★★★
★★★
★★
★
"""

for i in range(10,0,-1):         ## (10,0, -1 ) 을 넣는다.
    print('★'*i)

print('########### 문제 120. 아래의 결과를 출력하시오.(반대로 ###########')

    

print('########### 문제 121. 중첩 for lopp문 이용하여, ★로 사각형을 만드시오 ###########')

a= 5
b= 4
for i in range(0,b): # 세로
    for j in range(0,a):
        star +=  '★'  # 가로
    print(star)
    star=''    #초기화
######다른방법
for i in range(b):
    result = ''.join('★' for i in range(a))         # .. < result가 none이다. 근데 이곳에
                                                    #     join.() 을 써서 ★ 5개를 모아주는 메서드
    print(result)










print('########### 문제 122. 구구단을 가로로 출력하시오. ###########')

for i in range(1,10):
    garo =''
    for j in range(2,10):
        garo = garo +str(j)+' X '+str(i)+ ' = '+ str(i*j)+'  '.ljust(13)         #ljust 는 lpad같은 그런느낌임.
    print(garo,'\n')

print('########### 문제 123. for loop문을 이용해서 power 함수를 구현하시오! ###########')
## 밑수 2, 지수 3
a= int(input('dd'))
b= int(input('ff'))
power= a

for i in range(0,b-1):
    power *= a
    print(power)


######### For loop문을 활용하는 문자 함수     isdigit / isalpha / isspace########
s = 'some string'

numbers = sum( i.isdigit() for i in s)
words = sum(i.isalpha() for i in s)
spaces = sum(i.isspace() for i in s)

print(numbers)
print(words)
print(spaces)

txt = open("C:/Users/sru/Desktop/이원주/겨울왕국_대본.txt",'r')
lines = txt.readlines()
total = 0
for i in lines:
    numbers = sum( i.isdigit() for i in s)
    total += numbers
print(total)



