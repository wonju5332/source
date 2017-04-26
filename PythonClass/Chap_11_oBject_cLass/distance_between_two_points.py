class point(object):
    """Represnets a point in 2-d space."""
import math

print(point)  # class 'point'
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

