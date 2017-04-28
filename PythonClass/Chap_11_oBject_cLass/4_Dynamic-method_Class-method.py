# 1. 인스턴스 메소드 : 로봇의 팔이 잘 작동하는지 로봇을 만들어놓고 작동해보며 확인하는 메소드
# 2. 다이나믹 클래스 메소드

#예제

class Calculator:    #객체 = 속성+기능 이라고 했는데, 이건 기능만 4가지가 있는 클래스임. 속성어디있음?
    @staticmethod
    def plus(a, b):
        return a + b

    @staticmethod
    def divide(a, b):
        return a / b


def multiply(a, b):
    return a * b


def minus(a, b):
    return a - b


if __name__ == '__main__':
    print("{0} + {1} = {2}".format(7, 4, Calculator.plus(7, 4)))     #  <<<<<<<< 정적 메소드를 호출하는 중.
    print("{0} - {1} = {2}".format(7, 4, minus(7, 4)))
    print("{0} / {1} = {2}".format(7, 4, Calculator.divide(7, 4)))
    print("{0} * {1} = {2}".format(7, 4, multiply(7, 4)))

