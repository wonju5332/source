class point(object):
    """Represnets a point in 2-d space."""
import math

blank = point()  #인스턴스화 되었다.
print(blank)     # 클래스와 메모리에 저장된 장소를 출력한다.

blank.x = 3.0
blank.y = 4.0
print(blank.y)    #blank가 가리키는 객체로 가서 y의 값을 취하라.(y에 대입)
print(blank.x)

print('(%d, %d)' % (blank.x, blank.y))
distance = math.sqrt(blank.x**2 + blank.y**2)  #int형식인듯? 계산되네
print(distance)  # 5

    def print_point(p):
    print ('(%g, %g)' % (p.x, p.y))

    print_point(blank)




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

