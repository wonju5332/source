"""
가변 매개변수

 : 문자열.format() 함수처럼, 매개변수의 수가 유동적인 함수를 만들고 싶을 떄 사용하는 변수이다.
 함수 실행할 때 매개변수를 10개, 20개를 입력해도 제대로 동작을 한다.
 
 문법 : 
 def 함수이름( * 매개변수):
     코드블럭
     
  #파이썬에서 *가 쓰이는 경우는 다음과 같다.
  
  1. 가변 매개변수로 활용할 때
  2. 리스트 변수 내 요소들을 뽑아낼 때    (MIT코드)
"""

#예제

def merge_string(*text_list):       # text_list를 가변 매개변수로 지정한다.
    result  = ''            # result변수를 선언 한 후,
    for s in text_list:    # loop하여 text_list에 선언된 모든 매개변수를 출력한다.
        result += s + ' '   # 매개변수를 loop할때마다 str형태로 더한다.
    return result          # result를 반환한다.

merge_string('아버지가', '방에', '들어가신다')  # str 타입

print('## 문제 150. MIT TTT코드 내에서 보드판을 출력하는 printborad함수를 분석하라. ')


# States as integer : manual coding
EMPTY = 0
PLAYER_X = 1
PLAYER_O = 2
DRAW = 3
BOARD_FORMAT = """----------------------------
| {0} | {1} | {2} |
|--------------------------|
| {3} | {4} | {5} |
|--------------------------|
| {6} | {7} | {8} |
----------------------------"""
NAMES = [' ', 'X', 'O']
def printboard(state):
    """ Print the board from the internal state."""
    cells = []
    for i in range(3):
        for j in range(3):
            cells.append(NAMES[state[i][j]].center(6))
    print(cells)   #### debug  /printboard에 작성된 행렬에 관한 list
    print(*cells)  #### debug  /실제 보드판에포맷에 들어갈 값 하나하나의 요소
    print(BOARD_FORMAT.format(*cells))

printboard([[1,2,2],[1,1,0],[0,0,0]])
print(BOARD_FORMAT.format('a','b','c','d','e','f','g','h','g'))  #함수와 관계없이,포맷에 맞춰 입력된 값.
print(BOARD_FORMAT.format('x','o','x','o','x',' ',' ',' ',' '))
print(BOARD_FORMAT.format('x'.center(6),'o'.center(6),'x'.center(6),'o'.center(6),'x'.center(6),' '.center(6),' '.center(6),' '.center(6),' '.center(6)))
