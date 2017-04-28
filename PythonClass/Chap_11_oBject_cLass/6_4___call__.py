print('##############예제1 #################')
class sample(object):
    def __init__(self):
        print('전 생성하면 바로 실행됨')
sample = sample()


print('##############예제2 #################')

class sample2(object):
    def __call__(self):
        print('인스턴스에 괄호를 붙이면 제가 실행되지요.')
sample2_instance = sample2()  #실행안됨
sample2_instance()            #실행됨

"""
클래스의 인스턴스를 함수처럼 호출하기 위해서 클래스의 __call__이라는 매직 메소드를 정의했다.
이 원리를 이용해서 클래스를 데코레이터 구현할 수 있다.
어제 우리가 데코레이터로 구현한건 클래스가 아닌 함수였다.

"""


class onlyadmin(object):  # 함수에 들어가는 매개변수의 문자열을 받아서
    def __init__(self, func):  # 대문자로 변환해줌
        self.func = func

    def __call__(self, *args, **kwargs):
        name = kwargs.get('name').upper()
        self.func(name)


@onlyadmin  # 클래스명을 써준다.
def greet(name):
    print("Hello {}".format(name))


greet(name='Scott')


print('문제 176. 위 onlyadmin 데코레이터를 활용해서 find_job이라는 함수를 강력하게 하시오.')
#find_job(name='scott')
#당신의 직업은 analyst입니다. (소문자)

