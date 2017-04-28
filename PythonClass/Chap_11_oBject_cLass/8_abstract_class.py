print('###########################추상클래스 예제#########################33')
"""
추상 클래스는 추상 메소드가 있는 클래스를 말한다.
추상 메소드는 바디(내용)가 없는 메소드이다.
추상 클래스를 상속받는 자식 클래스에서 반드시 지켜줘야할 사항은
추상 클래스 내, 추상메소드와 일반메소드 등 많을 텐데, 그 중 추상메소드는 반드시 가져와서
오버라이드 해야한다.
"""
# 파이썬은 추상클래스를 제공하지 않기때문에, import받는다.

from abc import ABCMeta, abstractmethod


class animal(object):
    __metaclass__ = ABCMeta  # 추상 클래스로 선언

    @abstractmethod  # 추상 메소드 선언
    def bark(self):
        pass  # 비어있는 메소드 - bark , 상속받는 자식들이 반드시
        # 구현해야 되는중요한 메소드


class cat(animal):
    def __init__(self):           #구체화할 도구?
        self.sound = '야옹'
    def bark(self):              #빈메소드
        return self.sound      #오버라이딩

class dog(animal):
    def __init__(self):
        self.sound = '멍멍'
    def bark(self):               #빈메소드
        return self.sound      #오버라이딩

cat_1 = cat()
dog_1 = dog()

print(cat_1.bark())
print(dog_1.bark())



from abc import abstractmethod,ABCMeta

class beverage(object):
    __metaclass__= ABCMeta

    @abstractmethod
    def cost(self):
        pass

class americano(beverage):
    def __init__(self):
        self.price = 3.5
    def cost(self):
        return self.price

class caffelatte(beverage):
    def __init__(self):
        self.price = 4.5
    def cost(self):
        return self.price

americano = americano()
print(americano.cost())
7