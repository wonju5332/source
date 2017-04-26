"""
recursive function : 재귀함수

자기 스스로를 호출하는 함수.   Recursive call ( 재귀호출) 이라고도 한다.
스택구조와 반복문을 활용하여 이루어진다.

** 스택구조 후입선출. 나중에 들어온 데이터가 먼저 나가는 구조.

**큐 구조 : 선입선출. 먼저 들어온 데이터가 먼저 나가는 구조.  
 ex) ORACLE -> 락(LOCK)  
   SCOTT A    
   
update emp
set sal = 0
where ename = 'king';
                 scott b                             scott c           scott d
                update emp                       update emp
                set sal = 0                       set sal =0  
                where ename = 'king';               ..
                   # 락걸림..
                                   
        
    Enqueue 락 안에 B,C,D 걸려있으며, lock waiter라고 한다. commit을 하게 되면, 그다음 가장 먼저 update 시도한 scott b가 
    
    *스택구조 : 먼저 데이터가 들어간 게 가장 마지막에 나오는 구조
               나중에 들어간 데이터가 가장 먼저 나오는 구조.
               
    반복문 ( lOOP) + 스택 구조 ------> 재귀 알고리즘
    

"""

def some_func(count):                 #10 --> call 하고 기다림 --> 기다림 끝나면 10 출력   선입후출
    if count > 0:
        print(count,'쌓았다') # 쌓는것
        some_func(count-1)
    print(count,'호출했다')

some_func(10)

## 문제 153. 10!를 재귀함수로 구현해서 출력하시오 !

def main():
    num = int(input("자연수를 입력해 주세요.\n"))    #5
    fact = factorial(num)    # fact = factorial(5)  = 120
    print("자연수", num, "의 계승은", fact)   # 자연수 5 의 계승은 120

def factorial(num):       #factorial(5)
    if num == 0:    #5  == 0   False
        return 1   #이 경우는 input값이 0이기 때문에 0!= 1로 반환하라.
    else:       #5 이면 return해라
        return num * factorial(num - 1)

main()

def fact(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

fact(6)



print(16%12)
## 문제 154. 16과 28의 최대공약수를 출력하는데, 재귀함수를 이용해서 구현하시오 !

print(find_gcd(16,28))   #  16과 28  의 GDC는 4

def find_gdc(big,small):    # 20, 16
    result = big % small        # 16 % 20  = 4
    if small % result == 0:
        print(result)
    else:
        find_gdc(big,small)

print(find_gdc(20,16))



## 문제 155. 인자를 3개를 받는 최대공약수를 구하시오.

def find_gdc2(a,b,c):
    if a > b:
        b % a

"""
 재귀 알고리즘을 완성하는 문제           탐욕 알고리즘

 greddy 알고리즘
  
  당장 눈 앞의 이익만 추구하는 것
  먼 미래를 내다 보지 않고 지금 당장의 최선이 무엇인가만 판단
  
  ex) 바둑에서 나올 수 있는 경우의 수 10의 100승 : 
  0이 100개인 숫자
  
  

"""
## 문제 157. 탐욕 알고리즘을 이용하여 금액과 화폐가 주어졌을 때 가장 적은 갯수의 화폐로 지불해봐라..
"""

위 문제를 풀려면 어떤 기능이 있어야 하는가
1. 내 잔액과 화폐단위를 변수로 지정해주는 함수
2.  

"""

def coinGreedy(money, cash_type):
    def coinGreedyRecursive(money, cash_type, res, idx):
        if idx >= len(cash_type):                                                                                          #화폐 다 소진 후 return res
            return res
        dvmd = divmod(money,cash_type[idx])                                                                              #돈과, idx번째의 화폐단위로 나눌수 있음..
        res[cash_type[idx]] = dvmd[0]                                                                                    #해당 화폐 사용 매수   res라는 dict안의 cash_type[]의 idx를 key로 dvmd[0]값을 value로
        return coinGreedyRecursive(dvmd[1],cash_type,res,idx+1)                                                         #dvmd[1]이 잔액, cash_type 동일, res 동일, idx+1 <<재귀

    cash_type.sort(reverse=True)  # 화폐 내림차순 정렬     큰값부터 쓰려고.
    return coinGreedyRecursive(money,cash_type,{},0)


money = int(input('액수입력 : '))  # 타입 : 정수
print(type(money))
cash_type = [int(x) for x in input('화폐단위를 입력하세요 : ').split(' ')]
res = coinGreedy(money,cash_type)
for key in res:))
    print('{0}원 : {1}개'.format(key,res[key]





