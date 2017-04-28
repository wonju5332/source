
"""
함수의 특징

"""

print('#########함수의 특징1. 변수에 할당 할 수 있다.########')

def greet(name):
    return "Hello {} ".format(name)

greet_someone = greet   #함수를 변수에 할당.

print(greet_someone("scott"))


print('#########함수의 특징2. 다른 함수내에서 정의 될 수 있다. #########')

def greeting(name):
    def greet_msg():
        return 'Hello'
    return "{} {}".format(greet_msg(),name)

print(greeting("scott"))

print('#########함수의 특징3. 함수의 인자(매개변수)값으로 전달될 수 있다. ########')

def greet(name):
    return "Hello {} ".format(name)

def change_name_greet(func):
    name="king"
    return func(name)
print(change_name_greet(greet))

print('#########함수의 특징4. 함수의 반환값이 될 수 있다. ########')

def greet(name):
    return "Hello {} ".format(name)

def uppercase(func):   #func에 greet라는 함수가 들어옴.
    def wrapper(name):
        result = func(name)        #greet("scott")
        return result.upper()
    return wrapper

new_greet = uppercase(greet)
print(new_greet("scott"))


print('#########이름 입력하고 함수 실행하면 사원의 직업이 소문자로 출력되게 하라. ########')
def find_job(name):
    import pandas as pd
    emp = pd.read_csv("d:/data/emp.csv")
    job = emp[['job']][emp['ename'] == name].values[0][0]
    return job

def lowercase(func):          #lowercase( find_job(name) )
    def wrapper1(name):
        result = func(name)   # job
        return result.lower()  #job.lower()
    return wrapper1

new_find_job = lowercase(find_job)
print(new_find_job('SCOTT'))
print(type(find_job('SCOTT')))


print('##########데코레이터 사용 전 함수 간단하게 사용해보기.. ###################################')

class greet(object):
    current_user = None           #current_user 라는 변수인 속성을 선언
    def set_name(self,name):      #name에 admin 이라는 문자가 들어오면
        if name =='admin':        #current_user 에 admin 이라는 문자를 담고
            self.current_user = name
        else:                     #admin 이 아니라면 권한이 없다는 에러를 발생시켜라.
            raise Exception("There is no 권한")

    def get_greeting(self,name):
        if name =='admin':        #admin 이 맞다면
            return "Hello {} ".format(self.current_user)  # Hello 한다.

## 위 클래스를 실행하려면? 다음과 같이 한다.

gReet = greet()
gReet.set_name('admin')
print(gReet.get_greeting('admin'))
gReet.set_name('scott')
print(gReet.get_greeting('scott'))


print('###문제 168 위 코드에서 중복적으로 사용되는 코드부분 중 하나의 코드를 떼어내서 함수로 생성하시오. ( admin이 맞는지)#####')

def is_admin(user_name):
    if user_name != 'admin':
        raise Exception("권한이 없어요")
class greet(object):
    current_user = None
    def set_name(self,name):
        is_admin(name)
        self.current_user = name

    def get_greeting(self,name):
        is_admin(name)
        return "Hello {}".format(self.current_user)

gReet = greet()
gReet.set_name('admin')
print(gReet.get_greeting('admin'))

gReet.set_name('scott')
print(gReet.get_greeting('scott'))



print('###문제 169 King만 월급을 볼 수 있게하고, King 이 아닌 다른 사원들은 권한이 없다며 볼 수 없게 에러나게 하라.#####')
import pandas as pd
def is_admin(emp_name):
    if emp_name != 'KING':
        raise Exception("권한이 없어요")
class find_sal(object):
    user = None

    def set_name(self,name):
        is_admin(name)    #위에서 함수로 조건을 만들어놔서 class안에서 꿀빨고있음.
        self.user = name  # scott입력
    def get_sal(self,name):
        is_admin(name)    #어떻게 보면 조건에 ok면 아래 실행문 수행
        emp = pd.read_csv("d:/data/emp.csv")
        sal = emp[['sal']][emp['ename']==name].values[0][0]
        return sal

find_sal = find_sal() #생성자
find_sal.set_name('KING')
print(find_sal.get_sal('KING'))

find_sal.set_name('SCOTT')
print(find_sal.get_sal('SCOTT'))




print('###문제 170 위 is_admin을 통해 코드가 좋아졌지만 데코레이터로 더 좋아지게 할 수 있다. 해봐라.#####')


def is_admin(func):
    def wrapper(*arg,**kwargs):     # *arg 리스트 가변 매개변수
                                    # **kwargs 딕셔너리 가변 매개변수
        if kwargs.get('name') != 'admin':
            raise Exception("권한이 없다고 몇번 말씀드립니까")
        return func(*arg,**kwargs)
    return wrapper
class greet(object):
    current_user = None
    @is_admin      #admin 이 아니라면 아래 객체 실행하지도 마라.
    def set_name(self,name):
        self.current_user = name
    @is_admin      #admin 이 아니라면 아래 객체 실행하지도 마라.   데코레이터는 함수의 머리위에 장식처럼 꽂아 사용하기 때문에~!!
    def get_greeting(self,name):
        return "Hello {}".format(self.current_user)
gReet = greet()
gReet.set_name(name='admin')
print(gReet.get_greeting(name='admin'))   #키워드 매개변수  name = '   '  써야함.

#결국 그저 데코레이터는 함수를 대신 실행해줄 뿐, 즉 대리 호출임.


print('###문제 171.  169번 코드를 데코레이터로 개선시켜라#####')

import pandas as pd
def is_admin(func):
    def wrapper(*arg, **kwargs):
        if kwargs.get('name') == 'KING':
            raise Exception("권한이 없어요")
        return func(*arg,**kwargs)
    return wrapper
class find_sal(object):
    user = None
    @is_admin
    def set_name(self,name):
        self.user = name  # scott입력
    @is_admin
    def get_sal(self,name):
        emp = pd.read_csv("d:/data/emp.csv")
        sal = emp[['sal']][emp['ename']==name].values[0][0]
        return sal

find_sal = find_sal() #생성자
find_sal.set_name(name='KING')
print(find_sal.get_sal(name='KING'))

find_sal.set_name(name='SMITH')
print(find_sal.get_sal(name='SMITH'))

