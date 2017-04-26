# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 11:43:17 2017

@author: sru
"""

##문제 81.
import csv
file = open("C:/Users/sru/Desktop/이원주/2. 자료/3. Python/mit_ttt_study_data.csv")
ttt_csv = csv.reader(file)
for list in ttt_csv:
    print(list)
    
##문제 82.pandas 모듈을 이용, 사원 테이블에서 최대월급을 출력하시오 !!!!!!!!
import pandas as pd
emp= pd.read_csv("d:/data/emp.csv")
print(emp['sal'].max())
print[[emp[]]]
import pandas as pd  ## pandas 실행!!!!!!

emp = pd.read_csv("d:/data/emp.csv")
print( emp['sal'].max())


##문제 83. 직업이 SALESMAN인 사원들의이름과 직업을 출력하세요.
import pandas as pd  
emp = pd.read_csv("d:/data/emp.csv")
result = emp[['ename','sal']][emp['job']=='SALESMAN']
print(result)
                  #열            #행
import pandas as pd  
emp = pd.read_csv("d:/data/emp.csv")

print(result)

##문제 84. 월급 3000 이상인 사원들의 이름과 월급 출력
import pandas as pd  
emp = pd.read_csv("d:/data/emp.csv")
result = emp[['ename','sal']][emp['sal']>=3000].sort_values('sal',ascending=True)
                  #열            #행
print(result)

##문제 월급과 deptno가 20인 것..

import pandas ...


##문제87. 직업, 직업별 토탈월급을 출력하시오 !

import pandas as pd
emp = pd.DataFrame.from_csv("D:/data/emp.csv")
result = emp.groupby('job')['sal'].sum()
print(result)

##문제 88. 부서번호, 부서번호별 평균월급을 출력하시오 ! ## mean

import pandas as pd
emp = pd.DataFrame.from_csv("d:/data/emp.csv")
emp.groupby('deptno')['sal'].mean()

##문제 89. ttt 아래의 sql문을 pandas를 이용해 출력해보기

import csv
import pandas as pd
emp = pd.DataFrame.from_csv("D:\data/mit_ttt2.csv")
result1 = emp[(emp ['PLAYER']==1) &
              (emp['C1']==1) &
                 (emp['C2']==2) &
                    (emp['C3']==1) &
                       (emp['C4']==2) &
                          (emp['C7']==1) &
                             (emp['C9']==2) &
                                (emp['C5']+emp['C6']+emp['C8']==1 )]
result2 = result1.groupby(['C5','C6','C7'])['LEARNING_ORDER'].max()
print(result2)