# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 15:29:37 2017

딕셔너리 자료형은 key와 value를 조합해서 사용하는 자료형이다.



@author: sru
"""

##예제

dic = {}
dic['파이썬'] = 'www.python.org'
	    #   ↑               ↑ 
		#key             value
dic['애플'] = 'www.apple.com'
dic.keys()
dic.values()
dic['애플']
dic
dic.pop('애플') # 애플 인 요소 삭제
dic.clear()  #전체 다 삭제
dic


## 문제 105. 딕셔너리 자료형을 이용해서 주어가 0, 명사가 2, 동사가 1로 해서 한글과 영문을 저장하시오!!!!!
dic = {}
dic['나는'] = ('I',0)
dic['소년'] = ('boy',2)
dic['이다'] = ('am',1)
dic['피자'] = ('pizza',2)
dic['먹는다'] = ('eat',1)
"""
주어 : 0 
명사 : 2
동사 : 1

{'나는': ('I', 0),
 '먹는다': ('eat', 1),
 '소년': ('boy', 2),
 '이다': ('am', 1),
 '피자': ('pizza', 2)}
한글 어순 : 나는 소년입니다. (주어+보어+동사)
영어 어순 : I am boy.       (주어+동사+보어)
"""

##문제 106. 한글을 물어보게 하고, 한글을 입력하면 영어로 번역하는 프로그램을 파이썬으로 구현하라.(어순만 변경)
result = ''
input_kor = input('입력하세요.(나는 소년 이다 / 나는 피자를 먹는다) :')
input_list = input_kor.split(' ')
for i in range(len(input_list)) :
    for j in input_list :
        if dic[j][1]==i :
            result = result + dic[j][0] + ' '
print(result)


############### SMT 감성어 사전 #################

##문제 107. 카페에서 SMT용 감성어 사전을 내려받아 CSV파일을 파이선에서 불러와요.

import csv
file = open("d:/data/smt_dic.csv",'r')
dic_csv = csv.reader(file)
for list in dic_csv:
    print(list[1],list[3],list[4])

##문제 109. smt 감성어 사전의 1번째 요소를 key로 설정하고,
##                           3번째 요소를 dic변수의 0번째 요소로 하고,
##                           4번째 요소를 dic변수의 4번째 요소로 지정해서
##                           smt_dic 라는 딕셔너리 자료형 변수를 생성하시오!
import csv
file = open("d:/data/smt_dic.csv",'r')
dic_csv = csv.reader(file)
smt_dic = {}
for list in dic_csv:
    smt_dic[list[1]] = (list[3],list[4])
smt_dic

##문제 110. 무성이가 만든 감성어 사전과 진우가 만든 번역기를 이용해서 한글 영문 번역기를 완성시키시오.
import csv
file = open("d:/data/smt_dic.csv",'r')
dic_csv = csv.reader(file)
smt_dic = {}
for list in dic_csv:
    smt_dic[list[1]] = (list[3],list[4])
    smt_dic[list[2]] = (list[3],list[4])
smt_dic
result = ''
input_kor = input('입력하세요.(나는 소년 이다 / 나는 피자를 먹는다) :')
input_list = input_kor.split(' ')
for i in range(len(input_list)) :
    for j in input_list :
        if int(smt_dic[j][1])==i :
            result = result + smt_dic[j][0] + ' '
            break
print(result)
