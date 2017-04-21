## 함수 생성 하는 방법


"""
def 함수이름 (매개변수):
    실행문
    return 결과

"""

print( '예제')

def my_abs(arg):
    if (arg < 0 ):
        result = arg * -1
    else:
        result = arg
    return result

print(my_abs(5))


print( '문제 146. 아래와 같이 이름을 입력해서 함수를 실행하면 해당 사원의 부서위치 출력되게 하라.')

# print (find_loc('SMITH'))        ---> DALLAS

def find_loc(var):

    import pandas as pd
    emp = pd.read_csv("d:/data/emp.csv")
    dept = pd.read_csv("d:/data/dept.csv")
    result = pd.merge(emp,dept,on='deptno')
    loc = result[['loc']][result['ename'] == var]
    return loc
print(find_loc('SMITH'))

print( '문제 147. 미분계수를 구하는 함수를 생성하는데, f(x) = 2x ^2 +1에 관하여 x=2 일때 기울기 구하시오! ')


def mibun_fun(val):
    import math
    delta = pow(10,-4)
    f_y = (2*pow((val+delta),2)+1)-((2*pow(val,2))+1)
    result = f_y/delta
    return result

print(mibun_fun(-2))


print ('문제 148. ')

def numerical_diff(func1,x):
    delta = 1e-4       # 0.0001 or 10의 -4승
    return (  (func1(x + delta) - func1(x - delta))/ (2 * delta) )     #수치미분   델타X가 아닌, -델타와 +델타 간의 직선을 델타의 기울기로 본다! 만약에 f(x)에 로그값 0이 들어가면 무한대가 되버리기 때문에!

def func1 (x):
    return 2*pow(x,2)+1                 #함수 설정
print( numerical_diff (func1, -2) )    # 미분(함수,a값)

print( ' 문제 148. 함수 f(x) = x ^2 -x +5 함수의 x 가 -2일때 미분계수를 구하시오.')

def function_2 (x):
    return pow(x,2)-x+5
print( numerical_diff (function_2, -2) )







def mibun(f,x):
    delta = pow(10,-4)    #delta값
    return ()