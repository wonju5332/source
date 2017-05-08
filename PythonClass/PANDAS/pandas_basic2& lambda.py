"""

pandas.DataFrame은 2차원 구조의 데이터를 쉽게 조작할 수 있게 해줌

                pandas 모듈 사용법

                기본문법 : 판다스 데이터 프레임 [열]  [행]

*** 기타 비교 연산자 비교

     오라클                 파이썬               판다스
     between .. and        (>= )&(<= )         [(emp['sal']>=1000) &
                                                (emp['sal']<=3000) ]
     in                       in                    isin
     
     is null               ==''                 emp['comm'].isnull()
     
     like                    [0:1]..            apply함수+ lambda 표현식    
     
*** Lambda 표현식
 " 여러줄의 코드를 딱 한 줄로 만들어주는 인자"
 ex) def hap(x,y):
    return x+y
    print(hap(10,20))
    --------------->     lambda로 표현하면?
                                           -->   (lambda x,y: x+y)(10,20)
                                           
                                           
*** 판다스의 그룹함수 

    max, min, sum, mean, count
            ↓
    emp [['sal']] [emp['job'] =='SALESMAN' ].max()   ----> 직업이 SALESMAN인 사원들의 월급 중에서 최대값 출력
             ↓
    emp.groupby('job')['sal'].max()                  ----> 직업별 최대월급을 출력
"""
##Pandas 기본문법 예제
#연습1
emp_result = emp[ ['ename','sal'] ] [emp['sal']] == 3000 ]
         ##   ↑           ↑                ↑
#     pandas data frame  열               행
# 만일 행을 쓰지 않으면? 열만 나옴. 
# 위처럼 하려면, 먼저 pandas data frame을 만들어야 한다.
import pandas as pd
emp = pd.DataFrame.from_csv("d:/data/emp.csv")
#                            ↑판다스 data frame으로 만들려면 csv파일안에 index 컬럼이 존재해야 한다.
#연습2.

import pandas as pd
emp = pd.DataFrame.from_csv("d:/data/emp.csv")
empresult = emp [['ename','sal']]
print(empresult)

#연습3.
import pandas as pd
emp = pd.DataFrame.from_csv("d:/data/emp.csv")
empresult = emp
print(empresult)

#연습4.  Pandas를 이용한것과, 이용하지 않는 것과의 차이
                  # Pandas
import pandas as pd
emp = pd.DataFrame.from_csv("d:/data/emp.csv")
empresult = emp [['ename','sal','job']][emp['job'] == 'SALESMAN']
print(empresult)

                  # 일반
import csv
file = open("d:/data/emp.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    if (emp_list[2]=='SALESMAN'):
        print(emp_list[1],emp_list[5],emp_list[2])

############################################################################
##문제 91. 직업이 SALESMAN, ANALYST인 사원들의 이름과 월급과 직업을 출력하시오.
##문제 92. 직업이 SALESMAN, ANALYST이 아닌 사원들의 이름과 월급과 직업을 출력하라.

                # pandas이용  / 문제 91

import pandas as pd 
emp = pd.DataFrame.from_csv("d:/data/emp.csv")      #행.isin (    ['cond1','cond2'  ]  )
empresult = emp[['ename','sal','job']][emp['job'].isin (['SALESMAN','ANALYST'])]
print(empresult)
                # pandas이용  / 문제 92  (힌트 : pandas에서 not을 ~ 로 나타낸다.)
import pandas as pd 
emp = pd.DataFrame.from_csv("d:/data/emp.csv")      #행.isin (    ['cond1','cond2'  ]  )
empresult = emp[['ename','sal','job']][~emp['job'].isin (['SALESMAN','ANALYST'])]
print(empresult)

                # 일반 파이썬 / 문제 91
import csv
file = open("d:/data/emp.csv")
emp_csv = csv.reader(file)
for list in emp_csv:
    if list[2] in ['SALESMAN','ANALYST']:
        print(list[1],list[5],list[2])
                # 일반 파이썬 / 문제 92
import csv
file = open("d:/data/emp.csv")
emp_csv = csv.reader(file)
for list in emp_csv:
    if list[2] not in ['SALESMAN','ANALYST']:
        print(list[1],list[5],list[2])
############################################################################
##문제 93. 커미션이 null인 사원들의 이름과 커미션을 출력하시오!
##문제 94. 커미션이 null이 아닌       ''
                # pandas이용  / 문제 93
import pandas as pd
emp = pd.DataFrame.from_csv("d:/data/emp.csv")
empresult = emp[['ename','comm']][emp['comm'].isnull()]
print(empresult)
                # pandas이용  / 문제 94
import pandas as pd
emp = pd.DataFrame.from_csv("d:/data/emp.csv")
empresult = emp[['ename','comm']][~emp['comm'].isnull()] # ~ 또는 .notnull()
print(empresult)

                # 일반 파이썬  / 문제 93
import csv
file = open("d:/data/emp.csv")
emp_csv = csv.reader(file)
print('ename','comm')
for list in emp_csv:
    if list[6] =='':
        print(list[1],list[6])
                # 일반 파이썬  / 문제 94
import csv
file = open("d:/data/emp.csv")
emp_csv = csv.reader(file)
print('ename','comm')
for list in emp_csv:
    if list[6] != '':
        print(list[1],list[6])

############################################################################
##문제 95. 월급이 1000 에서 3000 사이인 사원들의 이름과 월급을 출력하시오!

                # pandas이용  / 문제 95
import pandas as pd
emp = pd.read_csv("d:/data/emp.csv")
empresult = emp[['ename','sal']][(emp['sal']> 1000) & (emp['sal'] < 3000)]
print(empresult)
                # 일반 파이썬  / 문제 95
import csv
file = open("d:/data/emp2.csv")
emp_csv = csv.reader(file)
print('ename','sal')
for list in emp_csv:
    if (int(list[5]) >= 1000) &(int(list[5]) <= 3000):
        print(list[1],list[5])

## 문제 96. 이름의 첫 글자가 S로 시작하는 사원들의 이름을 출력하시오 !

                   # pandas이용  / 문제 96         
                   ##  lambda 활용! 
import pandas as pd
emp = pd.read_csv("d:/data/emp.csv")                  
empresult = emp[['ename','sal']][emp['ename'].apply(lambda x:x[0]=='S')]
print (empresult)

                   # 위 식을 lambda표현식을 사용하지 않고 함수를 생성해서 수행하라.
def p97(z):
    if z[0] == 'S' :
        return True
    return False
import pandas as pd
emp = pd.read_csv("d:/data/emp.csv")                  
empresult = emp[['ename','sal']][emp['ename'].apply(p97)]
print (empresult)
############################################################################

##문제 98. 이름의 끝글자가 T로 끝나는 사원들의 이름을 출력하시오 ! (lambda사용.)
import pandas as pd
emp = pd.read_csv("d:/data/emp.csv")         
empresult = emp[['ename']][emp['ename'].apply(lambda x:x[-1]=='T')]
print(empresult)

#################################    PANDASGroup 함수  #######################
##문제 99. 직업, 직업별 최대월급을 출력하는데, 직업이 SALESMAN은 제외하고 출력하라!
import pandas as pd
emp =pd.DataFrame.from_csv("d:/data/emp.csv")
empresult = emp[['sal','job']][emp['job'] !='SALESMAN'].groupby('job')['sal'].max()
empresult2 = empresult.sort(['job','sal'],ascending[True,True])
print(empresult2)



##문제 100. 부서번호, 직업, 부서번호별 직업별 토탈월급을 출력하시오 !
## select deptno,job, sum(sal)
## from emp
## group by deptno, job;

###                    pandas이용으로 풀기
import pandas as pd
emp = pd.read_csv("d:/data/emp.csv")
empresult = emp.groupby(['deptno','job'])['sal'].sum()
print(empresult)



###############################  PANDAS X 서브쿼리 ##########################
##문제 101. JONES 보다 더 많은 월급을 받는 사원들의 이름과 월급을 출력하라!

"""
ORACLE이었다면??
select ename, sal
    from emp
    where sal > ( select sal from emp where ename = 'JONES');
"""
##Pandas라면??
import pandas as pd
emp = pd.read_csv("d:/data/emp.csv")
jonessal = emp[['sal']][emp['ename']=='JONES']
empresult = emp[['ename','sal']][emp['sal'] >= jonessal]
  # 이 상태에서 jonessal은 하나의 value가 아닌, DataFrame상태이기 때문에 연산에 쓰일 수 없다.
#따라서 다음과 같이 .values[0]을 넣어준다.
import pandas as pd
emp = pd.read_csv("d:/data/emp.csv")
jonessal = emp[['sal']][emp['ename']=='JONES'].values[0]
print(type(jonessal))
empresult = emp[['ename','sal']][emp['sal'] >= jonessal[0]]
print(empresult)

## 문제 102. SCOTT의 직속상사 이름을 출력하시오 !
import pandas as pd
emp = pd.read_csv("d:/data/emp.csv")
scottmgr = emp['mgr'][emp['ename'] == 'SCOTT'].values[0]
mgrename = emp[['ename']][emp['empno'] == scottmgr]
print(mgrename)

##문제 103. 관리자인 사원들의 이름을 출력하라.

"""
select ename
    from emp
    where empno in (select mgr
                    from emp);
    
"""
import pandas as pd
emp = pd.read_csv("d:/data/emp.csv")
result = emp[['ename']][emp['empno'].isin (emp['mgr'])]
print (result)

## 문제 104. 칼럼 c5,c6,c8 이 남아있을 때 어떤 수가 가장 좋은 수인가?

"""
select * from ttt_data
where learning_order in (
                            select max(learning_order) from ttt_data
                            where player = 1
                            and c1 = 1 and c2 = 2 and c3 = 1 and c4= 2 and c5+c6+c8=1
                            group by c5,c6,c8) and player = 1;
"""

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
subq = result1.groupby(['C5','C6','C7'])['LEARNING_ORDER'].max()
## subq를 .values로 얻어도 되고, 아래와 같이 해도 됨.

a= []
for i in subq:
    a.append(i)
print(a)

##############################################################
result3 = emp[emp['LEARNING_ORDER'].isin (a)]
print(result3)




print('#########이름 입력하고 함수 실행하면 사원의 직업이 소문자로 출력되게 하라. ########')
def find_job(name):
    import pandas as pd
    emp = pd.DataFrame.from_csv("d:/data/emp.csv")
    job = emp[['job']][emp['ename'] == name].values[0][0]     # 옆에처럼 변수 선언하고 values뽑으면 array타입으로 나오며, return절에 한번에 써버리면 str형태로 나옴..신기
    return job
def lowercase(func):
    def wrapper1(name):
        result = func(name)
        return result.lower()
    return wrapper1

new_find_job = lowercase(find_job)
print(new_find_job('SCOTT'))
print(type(find_job('SCOTT')))
