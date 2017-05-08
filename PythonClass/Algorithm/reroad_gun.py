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
            self.charge(int(input('몇발 장전하시겠습니까?')))  # 친구 함수 호출하여 장전한다.
        else:
            print('{} 발 남았습니다.'.format(self.bullet))