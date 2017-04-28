

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
            self.charge(10)  # 친구 함수 호출하여 장전한다. 자동10발 장전로딩ㅋㅋ
        else:
            print('{} 발 남았습니다.'.format(self.bullet))



gun_1 = gun()
gun_1.charge(10)
gun_1.trigger(10)
gun_1.print()

gun_2 = gun()
gun_2.charge(10)
gun_2.trigger(10)
gun_2.print()

print(gun_1)
print(gun_2)
##서로 다른 메모리를 사용하고 있다.
print(gun_1.__class__)
print(gun_2.__class__)

print('#### 문제 174. gun class 의 메소드들을 static method 틀로 변경해서 다시 총을 쏘시오.####')

class gun():
    bullet = 0
    @staticmethod
    def charge(num):
        gun.bullet = num
        print('총알 {0}발 장전'.format(num))
    @staticmethod
    def trigger(num):
        for i in range(num):
            if gun.bullet > 0:
                print('탕!')
                gun.bullet -= 1
            elif gun.bullet == 0:
                print('empty !! Please Reroad!')
                break
        return gun.bullet
    @staticmethod
    def print():
         if gun.bullet == 0:
            print("empty !! Please Reroad !")
         else:
            print('{} 발 남았습니다.'.format(gun.bullet))

gun_0 = gun()
gun_0.charge(10)
gun_0.trigger(3)
gun_0.print()



gun_1 = gun()
gun_1.charge()
gun_1.trigger(3)
gun_1.print()



gun_2 = gun()
gun_2.charge()          #충전하지 않고, 쏴보기
gun_2.trigger(1)
gun_2.print()

print(gun_0,gun_1,gun_2)


print('문제 175. static method로 선언한 클래스를 이용해서 인스턴스화한 두개의 총 쏘는 메소드가 서로 같은 메모리를 쓰는지 다른 메모리를 쓰는지 확인하라.')


print(gun_0.trigger)
print(gun_1.trigger)

print(gun_2.trigger)
print()
