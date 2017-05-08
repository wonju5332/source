import math

def stddev(*args):  # 부모 함수가 args라는 가변 매개변수를 선언했다.
    def mean():  # 1번함수
        return sum(args) / len(args)  # 전체 값을 sum한 후 관측치의 총 갯수로 나눠라. (부모 함수의 가변매개변수를 자식 함수들이 활용하는 모습)

    def var(m):  # 2번함수     var 안에 mean()을 넣었으니.  함수 var에서는 m으로 보는것.
        total = 0  # total default = 0으로 선언해놓아라.
        for x in args:  #
            total += (m - x) ** 2  # (M-X)^2의 SUM값이기 때문에, 각 관측치들을 for문을 활용, 더해준다.
        return total / (len(args) - 1)

    v = var(mean())  # 2번자식 안에 1번자식을 넣고 값을 출력 후, 부모가 sqrt적용하여 내보내는 모습.
    return math.sqrt(v)

