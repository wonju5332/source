print('문제 172. gun 이라는 인스턴스를 생성하기 위해서 gun 클래스를 생성하라.')
"""
gun = gun()     #총 설계도로 총을 실체화 시키는 ..
gun.charge(10)  #총알 10발 장전
gun.shoot(3)    #3발 쏜다.
#탕!
#탕!
#탕!
#7발 남았습니다.
gun.print()     #현재 총알이 얼마나 남았는지 확인
#7발 남았습니다.

#변수 : 총알담는변수(magazine)는 초기화되어야 함. 1 / 기능 : 1. 장전  2. 발사  3. print 기능
"""
class gun():
    def __init__(self):        #자기 자신을 불러오면서, 초기화 실행
        self.bullet = 0
        #장전 (여기서 num은 장전 총알 갯수)   메소드에서 num은 지역변수이다.
    def charge(self,num):
        self.bullet = num
        print('총알 {0}발 장전'.format(num))
        #발사 (여기서 num은 발사 횟수)
    def trigger(self,num):
        for i in range(num):
            if self.bullet > 0:
                print('탕!')
                self.bullet -= 1
            #총알이 없다면, 경고문과 함께 종료
            elif self.bullet == 0:
                print('empty !! Please Reroad!')
                break
        return self.bullet
    def print(self):
        if self.bullet == 0:
            print("empty !! Please Reroad !")
            self.charge(int(input('몇발 장전하시겠습니까?')))  # 친구 함수 호출하여 장전한다.
        else:
            print('{} 발 남았습니다.'.format(self.bullet))



gun = gun()
gun.charge(10)
gun.trigger(10)
gun.print()



print('######예제2  클래스를 사용하는 이유?#########################################')
print('######딕셔너리와 클래스의 차이점 비교########################################')
print('###################딕셔너리를 사용하는 경우')

# 아래는 기존의 딕셔너리를 사용했을 때..
student = {'name':'이원주', 'year':2, 'class':3, 'stu_id':35}
print ('{}, {}학년 {}반 {}번'.format(student['name'],student['year'],student['class'],student['stu_id']))
# 위 경우 너무 복잡하다 매번..
#아래와 같이 활용하면 좋다.
print('###################딕셔너리를 클래스로 활용하여 사용하는 경우###########################')

class student(object):
    def __init__(self,name,year,class_num,stu_id):
        self.name = name
        self.year = year
        self.class_num = class_num
        self.stu_id = stu_id

    def intro_myself(self):
        return '{} , {}학년  {}반  {}번 입니다.'.format(self.name, self.year, self.class_num, self.stu_id)




student = student('김인호',2,3,35)  #실체화
print(student.intro_myself())     #print > 함수호출


print('######문제 173. 위 student 클래스를 다시 실행하는데 self빼고 실행해보시오. ##########')

class student(object):
    def __init__(self,name,year,class_num,stu_id):
        self.name = name
        self.year = year
        self.class_num = class_num
        self.stu_id = stu_id

    def intro_myself(self):   #<여기 self를 지웟음. 지우면 인자값이 없어서 오류남. self쓰면 자동으로 인자를 넣어버림.
        return '{} , {}학년  {}반  {}번 입니다.'.format(self.name, self.year, self.class_num, self.stu_id)

student = student('이원주',3,2,38)
print(student.intro_myself())
      #intro_myself() takes 0 positional arguments but 1 was given


# self를 인자로써 호출하면 동작하는 이유는?
# 인스턴스의 메소드를 호출하면, 인스턴스 자기 자신인 self가 첫번째 인자로 자동으로 전달되기 때문!

print('문제 173 자기 자신이 인스턴스의 메소드에 인자로 전달되는 것이 어떤것인지 확인하기 위해 인스턴스를 통하지 않고 바로 클래스의 intro_myself를 직접 호출하여 확인하시오.')
class student(object):
    def __init__(self,name,year,class_num,stu_id):
        self.name = name
        self.year = year
        self.class_num = class_num
        self.stu_id = stu_id

    def intro_myself(self):   #<여기 self를 지웟음. 지우면 인자값이 없어서 오류남. self쓰면 자동으로 인자를 넣어버림.
        return '{} , {}학년  {}반  {}번 입니다.'.format(self.name, self.year, self.class_num, self.stu_id)

student_1 = student('이원주' ,2,3,35)
print(student.intro_myself(student_1))


