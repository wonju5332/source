# """
#
#
# 		a. 보드판
# 		b. 보드판 리셋
# 		c. Your move? 어디에 수를 둘지 물어보기
# 		d. 중간중간 게임의 승리자가 결정되었는지 확인하는 기능
# 		e. 게임이 다 끝나면 누가 이겼는지 알려주는 메시지 출력기능
# 		f. 게임 순서에 맞춰 X 다음 O가 수행 되게 Play하는 기능
# 		g. 게임이 한번만에 끝나는게 아닌, 계속 진행이 되게 하는 기능
#
# - printboard : 보드를 출력하는 함수
# - emptystate : 비어있는 판을 출력하는 함수(게임이 끝났으면 리셋해야 하므로)
# - gameover : 게임이 끝났는지(누가 이겼는지) 결정하는 함수
# - action : 어디에 수를 둘지를 물어보는 함수 (Your move?)
# - episode_over : 게임 종료 시, 누가 이겼는지 비겼는지 메세지 출력하는 함수
# - play : 게임 종료시, 누가 이겼는지 비겼는지 메세지 출력하는 함수
# -"_main_" : 메인 모듈을 가리키는 전역변수(무한 루프로 계속 게임을 진행하게끔 하는 함수)
#
# """
# print('#########################printboard############################################')
# EMPTY = 0
# PLAYER_X = 1
# PLAYER_O = 2
# DRAW = 3
# BOARD_FORMAT = "----------------------------\n| {0} | {1} | {2} |\n|--------------------------|\n| {3} | {4} | {5} |\n|--------------------------|\n| {6} | {7} | {8} |\n----------------------------"
# NAMES = [' ', 'X', 'O']
# state = [[1,2,0],[0,0,0],[0,0,0]]   #리스트 안의 리스트 len(state) = 3
# def printboard(state):
#     cells = []    # [i=0,j=0 -> 'X']
#                   # [i=0,j=1 -> 'O']
#
#     for i in range(3): #열
#         for j in range(3): #행
#             cells.append(NAMES[state[i][j]].center(6))
#     print(BOARD_FORMAT.format(*cells))  #리스트에서 요소만 빼내는것 *cells
#
# print(printboard(state))
#
#
# print('############################문제 192. 아래의 리스트 안에 리스트 변수에서 리스트1에 해당하는 첫번째 리스트를 출력하시오.##############')
#
# print(state[0])
# """
# [0][0]    [0][1]    [0][2]
# [1][0]    [1][1]    [1][2]
# [2][0]    [2][1]    [2][2]
# """
#
#
# print('#####################################def emptystate######################################')
# print('문제 195. 함수의 매개변수로 함수를 사용할 수 있다고 했다. 그러므로 printboard 에 매개변수로 emptystate() 함수를 사용하면 결과가 어떤게 출력되는지 결과를 출력하라.')
#
# def emptystate():
#     return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
#
# print(printboard(emptystate()))     #emptystae함수를 printboard함수의 변수인 state를 대신해 들어갔음.
#                                     # def printboard(emptystate) ... 같음
#
#
#
#
#
#
# print('###################################gameover#################################')
#
#
# def gameover(state):
#     # 가로/세로로 한 줄 완성한 플레이어가 있다면 그 플레이어 리턴
#     for i in range(3):
#         if state[i][0] != EMPTY and state[i][0] == state[i][1] and state[i][0] == state[i][2]:
#             return state[i][0]
#         if state[0][i] != EMPTY and state[0][i] == state[1][i] and state[0][i] == state[2][i]:
#             return state[0][i]
#     # 좌우 대각선
#     if state[0][0] != EMPTY and state[0][0] == state[1][1] and state[0][0] == state[2][2]:
#         return state[0][0]
#     if state[0][2] != EMPTY and state[0][2] == state[1][1] and state[0][2] == state[2][0]:
#         return state[0][2]
#     # 판이 비었는지
#     for i in range(3):
#         for j in range(3):
#             if state[i][j] == EMPTY:
#                 return EMPTY
#     return DRAW
#
#
# print('위 state 리스트를 하나씩 gameover에 넣어서 실행해 본다. 중단점 찍으며 디버깅 하면서 보기.'



print('#####################################class Human#################')
class Human(object):
    def __init__(self, player):
        self.player = player

print('#####################################def ACTION#################')
print('엔터만 치면 계속 물어보게 수정하시오. ')


# def action():      #self가 있으니 클래스 일것,
#     #printboard(state)         #실행되자마자 보드판을 보여줌
#     action = None
#     while action not in range(1, 10):         #1~10사이가 아니라고 한다면, 계속 물어보게 기능을 작동함.
#         try:
#             action = int(input('Your move? '))
#             switch_map = {            #게임 편하게 하기 위해서 키 밸류 세팅함
#                 1: (0, 0),
#                 2: (0, 1),
#                 3: (0, 2),
#                 4: (1, 0),
#                 5: (1, 1),
#                 6: (1, 2),
#                 7: (2, 0),
#                 8: (2, 1),
#                 9: (2, 2)
#                 }
# 
#         except ValueError:
#             continue
# 
#         return switch_map[action]
# print(action())


print('#####################################def episode_over#################')
print('비겼어요 가 출력되게 수정하시오. ')

#   원래 코드
# def episode_over(self, winner):
#     if winner == DRAW:
#         print('Game over! It was a draw.')
#     else:
#         print('Game over! Winner: Player {0}'.format(winner))

#print(episode_over(1))
#Game over! Winner: 1



print('#####################################def play함수#################')
print('실제로 게임을 진행하는 함수이다. 게임 종료 시 누가 이겼는지 비겼는지')
print('비겼어요 가 출력되게 수정하시오. ')

# def play(agent1, agent2):
#     state = emptystate()   #게임 판을 새로 리셋
#     for i in range(9):     # i -> 0, 1, 2 ... 8 까지 수행
#         if i % 2 == 0:     # i % 2 , 즉 i가 짝수이면 다음을 수행해라.
#             move = agent1.action(state)
#         else:              #           i가 홀수이면 다음을 수행해라.
#             move = agent2.action(state)   #
#         state[move[0]][move[1]] = (i % 2) + 1
#         winner = gameover(state)
#         if winner != EMPTY:
#             return winner
#     return winner
#

# Play 함수 코드 설명

# i=0 일때 -> 짝수 -> move = agent1.action(state) 수행 -> Your move? 물어본다.
# 그래서 1을 입력하면 move 에 1 : (0,0)이 담기게 된다. -> 그러면 state[0][0]으로 첫번째 리스트의 첫번째 요소를 가리키는 인덱스가 된다.
# 여기에 (0%2)+1인 1이 담기게 된다. state에 담기는 내용은 아래와 같다.
# [[1,0,0],[0,0,0],[0,0,0]]
#그리고 나서 gameover함수에 state리스트에 넣고, 게임이 종료되었는지 안되었는지 확인한다.


# i=1일때 -> 홀수 -> move = agent2.action(state) 수행  -> Your move? 물어본다.
# 그래서 5를 입력하면 move에 5 : (1,1)이 담기게 된다. -> 그러면 state[1][1]이 되고 두번째리스트의 두번째 요소를 가리키는 인덱스가 된다.
# 여기에 (1%2)+1이 담기게 된다.
# [[1,0,0],[0,2,0],[0,0,0]]
# 그리고 나서 바로 gameover함수에 state리스트를 넣어보고 게임이 종료되었나 안되었나 확인한다.



print('메인 함수에 대한 설명 : 게임을 진행시키며, 무한 반복 시키는 기능')

# if __name__ == "__main__":      #메인모듈이 아니라면, 실행하지 마라.
#     p1 = Human(1)               #Human 클래스를 p1로 인스턴스화 함
#     p2 = Human(2)               #Human 클래스를 p2로 인스턴스화 함
#     while True:                 #무한 반복하라.
#         winner = play(p1, p2)   #
#         p1.episode_over(winner)
#         p2.episode_over(winner)
#
#

print('문제 198. 아래 코드를 이용해서 main 함수를 생성하는데 무한 루프가 아닌 게임횟수를 아래와 같이 지정해서 수행되게 하시오 !')

#main(2)

# def main(cnt):
#     num = 0
#     #if __name__ == "__main__":
#     p1 = Human(1)
#     p2 = Human(2)
#     while num < cnt:
#         num += 1
#         winner = play(p1, p2)
#         p1.episode_over(winner)
#         p2.episode_over(winner)
#
# main(2)


print('문제 199. 사람과 컴퓨터(랜덤으로) 와 게임을 할 수 있게 하시오.')
# TTT_manVscomputer.py
print('문제 200. com Vs com 하게 해보시오.')
# Human 인스턴스를 Compuer로 바꿔주면 됨.


print('문제 201.컴퓨터(랜덤) 와 컴퓨터(랜덤) 와의 대결의 게임 진행 데이터를 D드라이브 밑에 test200.csv로 생성되게 하시오! ')



print('문제 202. 게임 과정의 데이터 말고, 게임 종료된 결과 데이터만 수집되게끔 아래의 코드를 어느 함수에 추가하라.')
def play(agent1, agent2):
    state = emptystate()
    for i in range(9):
        if i % 2 == 0:
            move = agent1.action(state)
        else:
            move = agent2.action(state)
        state[move[0]][move[1]] = (i % 2) + 1
        winner = gameover(state)
        if winner != EMPTY:
            import csv
            Fn = ("D:/data/test500.csv")
            w = csv.writer(open(Fn, 'a'), delimiter=',')  #a = append  delimiter = ',' >>쉼표로 구분자 한다.
            w.writerow([state[0][0],
                        state[0][1],
                        state[0][2],
                        state[1][0],
                        state[1][1],
                        state[1][2],
                        state[2][0],
                        state[2][1],
                        state[2][2],
                        winner
                        ])
            return winner
    return winner