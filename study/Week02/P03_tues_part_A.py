"""
                                                ▶ 3.1 반올림 ◀ 
♣  문제 : 부동 소수점 값을 10진수로 반올림하고 싶다.
↘  해결 : 간단한 반올림은 내장 함수인 round(value, ndigits)함수를 사용하고 싶다.
         자세한 소수점 계산    ==> decimal모듈
 """
print('########################################## 3.1 반올림 #####################################')


a = round(1.23,1)
b = round(1.27,1)
c = round(-1.27,1)
d = round(1.25361,3)
print(a,b,c,d)

a = 1627731
print(round(a,-1))
print(round(a,-2))
print(round(a,-3))

print('반올림과 서식화 헷갈려하지 말기')

x = 1.23456
print(format(x, '0.2f'))
print(format(x,'0.3f'))
print('value is {:0.3f}'.format(x))
#value is 1.235

"""
                                                ▶ 3.2 정확한 10진수 계산 ◀ 
♣  문제 : 정확히10진수 계산해야하며, 부동소숫점 사용 시, 작은오류 피하기
↘  해결 : 10진수는 아주 작은계산 하더라도 오류가 발생한다.. 따라서 Decimal모듈사용추천
 """
print('########################################## 3.2 정확한 10진수 계산 #####################################')

print('정확도 문제를 수정하기 위해, 반올림하는건 지양해야 함')
a = 2.1
b= 4.2
c=a+b
print(c)
print(round(c,2))

# 엄청 작은 소숫자 반올림이 문제가 없다면 보통 넘어가지만, 금융권은 절대 그러면 안됨
# decimal모듈 추천

print('부동 소숫점 값에는 10진수를 아주 정확히 표현하지 못한다는 문제있음. ')

a = 4.2
b = 2.1
print(a+b)  # 6.300000000000001
print(a+b == 6.3)  #False


print('위 오류를 피하고 싶다면, decimal사용')

from decimal import Decimal, localcontext
a = Decimal('1.3')
print(type(a))
b = Decimal('1.7')
print(a+b)
print(a+b == Decimal('3.0'))

# decimal객체는 숫자를 문자열로 표현해서, 어색할 수 있으나, 정확히 수행한다.
# 반올림의 자릿수와 같은 계산적 측면을 조절할 수 있는게 장점

print(a/b)
with localcontext() as ctx:
    ctx.prec = 3  #소숫점 3자리
    print(a/b)
    ctx.prec = 50
    print(a/b)


"""
         float   decimal
실행속도         >

"""




"""
                                                ▶ 3.3 출력을 위한 숫자 서식화 ◀ 
♣  문제 : 부동 소수점 값을 10진수로 반올림하고 싶다.
↘  해결 : 간단한 반올림은 내장 함수인 round(value, ndigits)함수를 사용하고 싶다.
         자세한 소수점 계산    ==> decimal모듈
 """
print('########################################## 3.1 반올림 #####################################')