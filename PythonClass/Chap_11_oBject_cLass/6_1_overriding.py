"""
Overriding
 :짓밟다. 무효로 하다. ~에 우선하다.
   :부모 클래스로부터 상속받은 메소드를 다시 정의하다

"""

class grandfather:
    def __init__(self):
        print("튼튼한 두 다리")
class father2(grandfather):
    def __init__(self):
        super().__init__()
        print("지혜")
father1 = father2() #지혜만 출력되게 된다. 즉, 오버라이드 되었기 때문이다. 할아버지의 튼튼한 두 다리도 물려받고 싶다면? super()를 적자


