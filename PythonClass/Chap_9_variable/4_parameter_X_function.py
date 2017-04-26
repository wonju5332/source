
def stop_fun(num):
    for i in range(1, num +1 ):  # 1부터 입력한 값 +1까지  loop한다. (0부터 시작이라서)
        print('숫자 {0} 을 출력합니다'.format(i) )       # format에 답을 작성한다.
        if i == 5:     #i가 5가 됬을 때.
            return      # True loop을 끝내버려라. (return 뒤에 아무것도 적지 않으면 함수 종료이다.)

stop_fun(10)

##예제

def enumstates(state, idx, agent):
    if idx > 8:
        player = last_to_act(state)
        if player == agent.player:
            agent.add(state)
    else:
        winner = gameover(state)
        if winner != EMPTY:
            return        #winner에 값이 아무것도 없으면, 출력하라.
        i = int(idx / 3)
        j = idx % 3
        for val in range(3):
            state[i][j] = val
            enumstates(state, idx + 1, agent)






##문제 151. 아래와 같이 숫자를 입력하고, 함수를 실행하면 숫자가 세로로 출력도게 하시오 !


def something(*num):
    result = 0
    for s in num:
        print(s)

something(1,2,3,4,5,6,7,0)

