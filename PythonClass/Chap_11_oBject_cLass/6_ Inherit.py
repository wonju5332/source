"""
상속이 필요한 이유?
1. 코드를 간결하게 만들기 위해
2. 객체지향 언어를 제대로 활용하기 위한 방법


"""


class father:
    def __init__(self):
        print("father said : hello ~")
        self.msg = "father said : Good Morning"

class child(father):
    def __init__(self):
        #father.__init__(self)
        super().__init__()
        print("child said : hello ~~ I am a child")

child = child()  ##hello ~ I am a child
print(child.msg)



print('###################다중상속 ############')

class father1:
    def func(self):
        print("father1의 지식")
class father2:
    def func(self):
        print("father2의 지혜")
class child(father1,father2):
    def childfunc(self):
        father1.func(self)
        father2.func(self)

object_child = child()  #생성자 선언
object_child.func()  #한쪽 유산 출력



print('###################다중상속 X 할아버지상속 ############')

class grandfather:
    def __init__(self):
        print('할아버지의 튼튼한 두 팔')
class father1(grandfather):
    def __init__(self):
        grandfather.__init__(self)
        print("1번아빠의 지식")
class father2(grandfather):
    def __init__(self):
        grandfather.__init__(self)
        print("2번아빠의 지혜")
class grandchild(father1,father2):
    def __init__(self):
        father1.__init__(self)
        father2.__init__(self)
        print("손자는 키가 크는 중이다.")

grandchild = grandchild()  #생성자 선언



print('###################문제 166 ############')

class grandfather:
    def __init__(self):
        print('할아버지의 튼튼한 두 팔')
class father1(grandfather):
    def __init__(self):
        super(father1,self).__init__()
        print("1번아빠의 지식")
class father2(grandfather):
    def __init__(self):
        super(father2,self).__init__()
        print("2번아빠의 지혜")
class grandchild(father1,father2):
    def __init__(self):
        super().__init__()
        print("손자는 키가 크는 중이다.")

grandchild = grandchild()  #생성자 선언
