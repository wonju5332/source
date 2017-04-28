print('#####예제 1 #####')

class yourclass:
    pass
class myclass:
    def __init__(self):
        self.msg = "hello"        #퍼블릭 변수임.

    def some_method(self):
        print(self.msg)
obj = myclass()  #생성자
obj.some_method()  # 메소드를 실행했기 때문에, 출력이 된것 이며
print(obj.msg)     # 따로 msg라는 퍼블릭변수를 실행해버린 것임.


print('#####예제 2 #####')

class yourclass:
    pass
class myclass:
    def __init__(self):
        self.msg = "hello"
        self.__private = "private"

    def some_method(self):
        print(self.msg)
        print(self.__private)
obj = myclass()
obj.some_method()      # hello  / private 출력
print(obj.msg,)        # hello   (퍼블릭 ) 출력
print(obj.__private)   # error   : AttributeError: 'myclass' object has no attribute '__private'