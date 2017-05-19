from tkinter import *   #파이썬 GUI 프로그래밍 패키지
import random
import time


"""
############# Ball 클래스 ################
"""
class Ball:

    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)  #공의 크기와 색깔
                                   #서   남  동   북
        canvas.configure(background='black')
        self.canvas.move(self.id, 245,0)  #첫 공의 스타트 위치
        self.y = -3
        starts = [-3, -2, -1, 1, 2, 3]  #시작의 방향 좌3,좌2,좌1,우1,우2,우3
        random.shuffle(starts)  #시작의 방향 6가지 선택 중 랜덤 1가지 초이스
        self.x = starts[0]    #랜덤으로 1개를 골랐으니, start[(random값)]이므로 start[0]
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
        self.ismiss = False
        self.values = {}

    def add(self, key):
        self.values[key] = 0
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = ball.canvas.coords(ball.id)

        if pos[1] <= 0:   #남쪽이 0이면
            self.y = 3    #y를 3으로
        if pos[3] >= self.canvas_height:  #북이 500보다 크다면 그냥 게임오버
            #self.hit_bottom = True
            self.y = -3                   #땅에 닿으면 튀어오르게 하기
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3
    def hit_paddle(self,pos):
        paddle_pos = self.canvas.coords(self.paddle.id)  #패들의 위치
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:

            if pos[3] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
                self.y=-3
                return True

        return False
    def keystate(self,movement):
        pos = self.canvas.coords(self.id)  # [86.0, 485.0, 101.0, 500.0]
        #                                      서    남      동     북
        paddle_pos = self.canvas.coords(self.paddle.id)
        return paddle_pos[0], (pos[0], pos[1]), (self.x, self.y),(movement)

    def lookup(self,key):
        if key not in self.values:
            self.add(key)
        return self.values[key]

    def randomChoice(self):
        rand = random.choice([0,1]) # 0 or 1중 하나를 random으로 고름
        key = self.keystate(rand)
        if key not in self.values:  #values 딕셔너리에 해당key가 없다면?
            self.add(key)           #추가해버리기
        return rand  # 0또는 1출력


def gameover(ball):
    paddle_pos = ball.canvas.coords(ball.paddle.id)
    pos = ball.canvas.coords(ball.id)
    hit_paddle = ball.hit_paddle(pos)

    # print(paddle_pos[0],(pos[0],pos[1]), (ball.x,ball.y))  #패들의 x좌표

    if paddle_pos[3] < pos[3] and ball.ismiss == False :
        ball.ismiss = True
        return 'miss'
    elif hit_paddle == True:
        return 'hit'
    elif pos[3] < paddle_pos[3]:
        ball.ismiss = False
        return 'pass'

def winnerval(val):  # miss
    if val == 'miss':
        return -1
    elif val == 'hit':
        return 1
    else:
        return 0

"""
############# Paddle 클래스 ################
"""

# hit_paddle = True 면 멈추게?
class Paddle:

    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10,fill=color) #패들의 크기와, 색깔
        self.canvas.move(self.id, 250, 400)  # 패들을 움직이게 하는 함수
        self.x = 0    # 패들이 게임시작할때, 움직이지 말라고 속도를 고정시킴
        self.y = 0
        self.canvas_width = self.canvas.winfo_width()   # 패들이 화면밖으로 나가지 않게 하기 위해
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)

    def draw(self):

        pad_pos = self.canvas.coords(self.id)
        if pad_pos[0] <= 0 and self.x < 0:
            # self.x = 0  #현재 버그는 계속 turn_left기능을 주면 벽을 통과하고 있음. 더 강력한 툴로써, return을 시켜버리면 함수가 종료됨
            return
        elif pad_pos[2] >= self.canvas_width and self.x >0:
            # self.x = 0
            return
        self.canvas.move(self.id, self.x, self.y)  #canvas.move는 원래 pos위에 있었으나, 이 아래다 데리고 오면서,

    def turn_left(self,evt):
        self.x = -9
        # self.y = 0
    def turn_right(self,evt):
        self.x = 9



tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=600, height=500, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
paddle = Paddle(canvas,'white')
ball = Ball(canvas, paddle, 'white')
# winner = gameover()
#print(winner(winner))   즉, def winner( gameover의 리턴값)
while 1:
    if ball.hit_bottom == False:
        ball.draw()
        y= 300
        starts = [-2,2]
        random.shuffle(starts)
        x = starts[0]
        winner = gameover(ball)
        key = ball.keystate(x)  # 0 또는 1
        ball.add(key)    # values[key] 에 대입
        print(ball.randomChoice())
        print(ball.values)
        print(ball.keystate(x), end=' ')
        print(winnerval(winner))
    #ball.draw()
    tk.update_idletasks()  # tkinter에게 계속 화면 그리고 있으라고 명령
    tk.update()  # 초기화
    time.sleep(0.02)