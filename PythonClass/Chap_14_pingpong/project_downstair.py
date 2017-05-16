

from tkinter import *
import random
import time


# ball = Ball(canvas, paddle, 'white')
class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
                                    #서  남  동  북
        canvas.configure(background='black') # 캔버스의 색깔을 검정색으로 하겠다.
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)
        self.hit_bottom = False # 바닥에 닿으면 게임 끝나는 코드를
                                # 구현하기 위해서 쓰는 변수
        self.isMiss = False

    def turn_left(self,evt):

        self.x = -5
        self.y = -3

    def turn_right(self,evt):
        self.x = 5
        self.y = -3
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3
        if self.hit_paddle(pos) == True:
            print ('hit')
            self.y = -3

    def gameover(self):
        pos = self.canvas.coords(self.id)
        if pos[1] < 400 < pos[3] and self.isMiss == False and self.y > 0:
            self.isMiss = True
            print('miss')
        elif pos[1] > 400 or pos[3] < 400:
            self.isMiss = False


    def hit_paddle(self,pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
                return True
        return False



class Paddle:
    def __init__(self,canvas,id,pad_x,pad_y):
        self.pad_x = pad_x
        self.pad_y = pad_y
        self.canvas = canvas
        self.id = id
        self.canvas.move(self.id, pad_x,pad_y )
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()



    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0



tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=600, height=500, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
paddle = Paddle(canvas,canvas.create_rectangle(0,0,100,10,fill='white'),200,300)
paddle2 = Paddle(canvas,canvas.create_rectangle(0,0,100,10,fill='white'),100,200)
ball = Ball(canvas, paddle, 'white')


while 1:


    ball.draw()
    paddle.draw()
    ball.gameover()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.02)
