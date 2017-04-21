# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 15:24:15 2017

@author: sru


*************WHILE LOOP************
문법 : 
    while 조건 :
        실행문
        


"""

# 예제.

limit = int(input('반복할 횟수입력해주세용..'))

count = 0  # count는 0이다.
while count < limit:   #카운트가 입력한 값보다 작을때까지만 돌아라!
    count += 1
    print('{0}회 반복.'.format(count))
    
#문제 126. 숫자를 물어보게하고 숫자를 입력하면 해당 숫자만큼 아래와 같은 그림이 그려지게 하세용..
# 숫자를 입력하세요 ~ 6 (while loop문)

a = int(input('숫자를 입력하세요 '))
cnt = 0
while cnt < a:
    cnt += 1
    space = a-cnt
    print(' '*space,end='')
    print('★'*cnt+' '*space)
    

##문제 127. 팩토리얼을 while loop문으로 구현하시오 !
a = 5
cnt = 0
result = 5
while cnt < a:
    cnt += 1
    result = result -1
    print(a*result)



##문제 128. log함수를 파이썬으로 구현하시오. 밑수 2 진수 16 로그값은4이다.

a = int(input('밑수입력'))
b = int(input('진수입력'))
result = b
cnt= 0

while result > 1:
    cnt += 1
    result = result / a   
print('답은 =',cnt)

##문제 129. 두 수를 입력받아서, 최대공약수를 구하시오 !

a= int(input('첫번째 숫자를 입력하세요'))
b= int(input('두번째 숫자를 입력하세요'))


c= input('최대공약수 알고싶은 숫자 써주세요').split(' ')
a=int(c[0])
b=int(c[1])
if a > b:
    temp2 = b
    b = a
    a = temp2                # minvalue찾기

if a%b ==0:
    print(b)
else:        
    temp = a%b #6
    while temp != 0:         
        result = temp
        temp = b % temp
    print(result)
    

gdc= []  # gdc라는 리스트를 열어준다.
wow = int(input('숫자를 가로로 쭉 얼마든 써보렴.'))  #값을 입력받을 곳이다.
gdc.append(wow)  #값을 gdc에 append해준다.
length = len(gdc) # gdc리스트에 들어있는 값의 갯수를 출력한다.
cnt = 0
