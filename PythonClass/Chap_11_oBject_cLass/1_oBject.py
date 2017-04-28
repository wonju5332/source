class car:
    def __init__(self):  # 초기화 해주는 함수
        self.color = 0xFF000  # 자동차의 색깔
        self.wheel_size = 16  # 바퀴의 크기
        self.displacement = 2000  # 엔진 배기량

    def forward(self):  # 전진하는 기능
        pass

    def backward(self):  # 후진하는 기능
        pass

    def turn_left(self):  # 좌회전
        pass

    def turn_right(self):  # 우회전
        pass


if __name__ == '__main__':  # 메인모듈일때 아래 스크립트 실행해라!
    my_car = car()  # car() 클래스에 의해서 my_car 라는 객체가 생성됨. 인스턴스화 됨.
                    # Car()클래스로 my_car라는 oBject생성
    print('0x{:02X}'.format(my_car.color))  #
    print(my_car.wheel_size)
    print(my_car.displacement)  # Car의 속성(변수)들 출력

    my_car.forward()  # my_car의 메소드(기능) 을 호출
    my_car.backward()
    my_car.turn_left()
    my_car.turn_right()


class ClassVar:
    text_list = []   # 클래스의 정의 시점에서 바로 메모리에 할당됨
    def add(self,text):
        self.text_list.append(text)       #글자 추가하는 함수
    def print_list(self):
        print(self.text_list)             #글자 출력하는 함수

if __name__ == '__main__':
    a = ClassVar()   #위에서 만든 붕어빵을 이용해서 a라는 붕어빵을 만든다.
    a.add('a')       #a라는 붕어빵(인스턴스(객체))에 a(앙금)를 add 기능(함수)을 작동시킨다.
    a.print_list     #a라는 붕어빵(인스턴스(객체))에 print_list기능(함수)를 작동시킨다.

    b = ClassVar()   #위에서 만든 붕어빵 틀을 이용해서 b라는 붕어빵을 만든다.
    b.add('b')       #b라는 붕어빵(인스턴스(객체))에 b(슈크림)를  add한다.
    b.print_list()   #출력 결과로 기대되는것?


class ClassVar:
    def __init__(self):
        self.text_list = []
    #text_list = []   # 클래스의 정의 시점에서 바로 메모리에 할당됨
    def add(self,text):
        self.text_list.append(text)       #글자 추가하는 함수
    def print_list(self):
        print(self.text_list)             #글자 출력하는 함수

if __name__ == '__main__':
    a = ClassVar()   #위에서 만든 붕어빵을 이용해서 a라는 붕어빵을 만든다.
    a.add('a')       #a라는 붕어빵(인스턴스(객체))에 a(앙금)를 add 기능(함수)을 작동시킨다.
    a.print_list()   #a라는 붕어빵(인스턴스(객체))에 print_list기능(함수)를 작동시킨다.

    b = ClassVar()   #위에서 만든 붕어빵 틀을 이용해서 b라는 붕어빵을 만든다.
    b.add('b')       #b라는 붕어빵(인스턴스(객체))에 b(슈크림)를  add한다.
    b.print_list()   #출력 결과로 기대되는것?


