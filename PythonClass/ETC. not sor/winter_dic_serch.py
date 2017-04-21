# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 18:13:34 2017

@author: sru
"""
import csv       ##txt파일은 변수하나에 담아서 출력했으나, csv파일은 다 써주었다.
positive = open("D:\\data\\positive_negative\\edit\\positive-words.csv",'r')
posi_csv = csv.reader(positive)
winter = open("D:\\data\\positive_negative\\winter.txt",'r',encoding='euc-kr')
w_list = []
po_dic = []
sum = 0

for line in winter:
    words = line.split()  
    for i in words:
       w_list.append(i)
print(w_list)        ## 단어별 쪼갠 것을 하나의 리스트에 담았다.

for po in posi_csv:
    po_dic = po      ## 긍정사전을 한 리스트에 담았다.
    
for i in w_list:     ## 대본과 사전을 in으로 검색하여, 매칭 한개당 1씩 더해주었다.
    if i in po_dic:
        sum = sum+1
print(sum)

