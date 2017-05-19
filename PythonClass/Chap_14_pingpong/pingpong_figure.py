print('문제 229 . 캔버스의 공의 첫 시작위치가 천정위가 되게 하시오!')
# 관련코드 self.canvas.move(self.id, 245, 100)
# 캔버스는 left극점 = (0,0) middle = (245,0)  right극점 = (490,0)  center (245,100)
import random
class Ball:

    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        canvas.configure(background='black')
        self.canvas.move(self.id, 245, 100)
                          #공      x축,  y축
        starts = [-3, -2, -1, 1, 2, 3]    #공의 방향
        random.shuffle(starts)

        self.x = starts[0]
        self.y = -3  # 공을 기준 (245,100)으로 값이 커질수록 속도 증가
        self.canvas_height = self.canvas.winfo_height()  #캔버스의 총 height
        self.canvas_width = self.canvas.winfo_width()    #캔버스의 총  width
        self.hit_bottom = False  # 바닥에 닿을 시,  게임오버되도록 return False처리

#정답은 self.canvas.move(self.id, 245, 0)  << y축을 0으로 올려버리면 된다.



print('문제 230. 게임이 시작할때 왼쪽, 오른쪽 중 랜덤으로 가게하지 말고, 무조건 오른쪽으로 가게 하려면?')
# 관련코드는  starts = [-3, -2, -1, 1, 2, 3]
#           random.shuffle(starts)
# starts = [1, 2, 3]    오른쪽
# starts = [-3, -2, -1]  왼쪽



print('문제 231. 캔버스의 전체 높이와 전체 넓이가 어떻게 되는지 확인하시오.')
# 관련코드
# self.canvas_height = self.canvas.winfo_height()
# self.canvas_width = self.canvas.winfo_width()
# print(self.canvas_height)   # 500
# print(self.canvas_width)    # 600





print('####################### def draw #########################')





def draw(self):
    self.canvas.move(self.id, self.x, self.y)
            #           공,     공의 x,   공의 y
            #                  (-좌 +우) (-아래 +위)
    pos = self.canvas.coords(self.id)
    if pos[1] <= 0:
        self.y = 3
    if pos[3] >= self.canvas_height:
        self.hit_bottom = True
    if pos[0] <= 0:
        self.x = 3
    if pos[2] >= self.canvas_width:
        self.x = -3
    if self.hit_paddle(pos) == True:
        self.y = -3


    def turn_left(self,evt):
        self.x = -9

    def turn_right(self,evt):
        self.x = 9



print('문제 232. 공이 키보드의 방향키로 움직여지게 하려면?')
# 관련코드:
# def draw -> self.canvas.move(self.id, self.x, self.y)
# class paddle
#     def __init__


# 답코드



# class Ball:
#
#     def __init__(self, canvas, paddle, color):
#         self.canvas = canvas
#         self.paddle = paddle
#         self.id = canvas.create_oval(10, 10, 25, 25, fill=color)  #공의 좌표
#                                     #서   남  동   북
#         canvas.configure(background='black')
#         self.canvas.move(self.id, 245, 100)
#         starts = [-3, -2, -1, 1, 2, 3]  #시작의 방향
#         random.shuffle(starts)
#
#         self.x = starts[0]
#         self.y = -3
#         self.canvas_height = self.canvas.winfo_height()
#         self.canvas_width = self.canvas.winfo_width()
#         print(self.canvas_height)
#         print(self.canvas_width)
#         self.hit_bottom = False
#         self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
#         self.canvas.bind_all('<KeyPress-Right>',self.turn_right)
#         self.canvas.bind_all('<KeyPress-Up>',self.turn_up)
#         self.canvas.bind_all('<KeyPress-Down>',self.turn_down)
#     def turn_left(self, evt):
#         self.x = -9
#
#     def turn_right(self, evt):
#         self.x = 9
#
#     def turn_up(self, evt):
#         self.y = -9
#
#     def turn_down(self, evt):
#         self.y = 9
#
#     def draw(self):
#         self.canvas.move(self.id, self.x, self.y)


print('공이 캔버스 화면 밖으로 나가지 않도록 하게 하려면?')
#원리이해
# 1. 공이 위로 올라가서 천정에 부딪히면 ?      >> 스스로 아래로 튀기게 하는 코드
# 2. 공이 아래로 내려가서 바닥에 부딪히면?     >> 스스로 위로 튀기게 하는 코드
# 3. 공이 동쪽(오른쪽)으로 가서 벽에 부딪히면 ?       >> 스스로 서쪽으로 오는 코드
# 4. 공이 서쪽(왼쪽)으로 가서 벽에 부딪히면?        >> 스스로 동쪽으로 오는 코드



# ------------------------------------------------  (100,0)
#                     ●




def draw(self):
    self.canvas.move(self.id, self.x, self.y)
    pos = self.canvas.coords(self.id)  # [86.0, 485.0, 101.0, 500.0]
    #                                        서    남      동    북
    if pos[1] <= 0:  # 남쪽이 0이면
        self.y = 3  # y를 3으로
    if pos[3] >= self.canvas_height:  # 북이 500보다 크다면 그냥 게임오버
        self.hit_bottom = True      #게임오버
        # self.y = -3               #만일, 게임오버 말고 다시 위로 튀기게 하고자 한다면 -3
    if pos[0] <= 0:
        self.x = 3
    if pos[2] >= self.canvas_width:
        self.x = -3
    if self.hit_paddle(pos) == True:
        self.y = -3


print('볼이 패들에 닿으면 딱 멈춰지게 하시오')


print('스페이스 바 누르면 게임이 다시 시작되게 하시오, 즉 공이 위로 올라가게 하라.')


def hit_paddle(self, pos):
    paddle_pos = self.canvas.coords(self.paddle.id)  # 패들의 위치
    print(paddle_pos)
    if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:

        if pos[3] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
            return True
    return False
print('문제 238. 공이 멈춰진 이후패들을 따라 움직여지게 하시오.')
