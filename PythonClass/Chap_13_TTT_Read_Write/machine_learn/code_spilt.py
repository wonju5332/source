#1.3 random함수

import random
EMPTY = 0   #상수는 변수명을 대문자로 쓴다.
state = [[1,2,0],[0,0,0],[0,0,0]]

PLAYER_X = 1
PLAYER_O = 2
DRAW = 3
BOARD_FORMAT = "----------------------------\n| {0} | {1} | {2} |\n|--------------------------|\n| {3} | {4} | {5} |\n|--------------------------|\n| {6} | {7} | {8} |\n----------------------------"
NAMES = [' ', 'X', 'O']

# def random_func(state):
#     available = []
#     for i in range(3):
#         for j in range(3):
#             if state[i][j] == EMPTY:    # 1 or 2면 not append  i=0 , j=2 일때 [0,2] == empty 이므로 [(0,2)]삽입
#                 available.append((i, j))
#     print('available  : ',available)    # empty공간을 available에 채워놓았음.
#     return random.choice(available)     # 그 중 랜덤으로 한 값을 return
#
# print(random_func(state))


# 1.4 greedy 함수
state = [[1,2,1],[0,0,0],[0,0,0]]


def greedy(self, state):
    maxval = -50000  #최대 가중치
    maxmove = None   #최선의 수
    if self.verbose:
        cells = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == EMPTY:
                state[i][j] = self.player
                val = self.lookup(state)  # values 에 없으면 새로 0.5 를
                # values 에 넣어주고 그 값을
                state[i][j] = EMPTY  # 다시 여기로 가져온다.
                # 있으면 바로 values 에서 가져온다.
                if val > maxval:
                    maxval = val
                    maxmove = (i, j)
                if self.verbose:
                    cells.append('{0:.3f}'.format(val).center(6))
            elif self.verbose:
                cells.append(NAMES[state[i][j]].center(6))
    if self.verbose:
        print(BOARD_FORMAT.format(*cells))
    print(maxmove)
    return maxmove



#1.5 lookup 함수
state = [[1,2,1],[0,0,0],[0,0,0]]
def lookup(self, state):   #[[1,2,1],[0,0,0],[0,0,0]]
        key = self.statetuple(state) # 리스트를 튜플로 바꿔주는 역활
        if not key in self.values:
            self.add(key)  # values 에 없으면 add 함수로 추가
        return self.values[key]  # 있으면 그거 리턴, 없으면 만들고 리턴


 #1.6 add 함수
