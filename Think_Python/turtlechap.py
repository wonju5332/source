# greeting = 'Hello, World!'
# new_greeting = 'J'+ greeting[1:]
# print(new_greeting)
#
# #Jello, World!
#
#
# # find는 문자를 받아, 등장하는 곳의 index를 뽑아낸다. 발견되지 않으면 -1반환
#
# def find(word, letter,):
#     idx = 0
#     while idx < len(word):  # 0 < 6 - True
#         if word[idx] == letter:  #word[0] == 'd' 라면?
#             return idx
#         print('얼마나',idx)
#         idx += 1
#     return -1
#
#
# print(find('abcdef', 'd'))
#
# #8.4find를 수정해서, word 내의 지수를 세 번째 매개변수로 받아들여, 어디서부터 검색을 시작할지를 지정할 수 있도록 하세요
#
# def find(word, letter, start):   # idx = 3 이라면?
#     idx = 0  #회전 수
#     while start < len(word):  # 3 < 6 - True
#         if word[start] == letter:  #word[3] == f ?
#             return idx
#         start += 1
#         idx += 1
#     return -1
# print(find('abcdef', 'f',3))
#
#
# #다음 프로그램은 문자열에서 a가 나타나는 횟수를 셉니다:
# word = 'banana'
# cnt = 0
# for i in word:
#     if i =='a':
#         cnt += 1
#     print(cnt)
#
#
# def count (word,letter):
#     cnt = 0
#     for i in word:
#         if i == letter:
#             cnt += 1
#     return cnt
#이 코드를 count라는 이름의 함수로 캡슐화하고, 문자열과 문자를 인자로 받아들이도록 일반화하세요.
# print(count('banana','a'))

def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False

    i = 0
    j = len(word2)-1

    while j > 0:
        print('i =',i,'j =',j)
        if word1[i] != word2[j]:
            return False
        i = i + 1
        j = j - 1

    return True

is_reverse('pots','stop') # string index out of range
                            #이런 경우, 오류가 발생한 줄 바로 앞에서 지수의 값을 인쇄해보자.
                            #i=0, j=4
                            #word2[4]가 되다보니, pots의 범위를 넘어 선 것. j에 -1를 해준다.
                            # i = 0 j = 3
                            # i = 1 j = 2
                            # i = 2 j = 1
                            # 을 알게 되었다.
                            # 올바른 답을 얻었으나, 순환이 3번만 된 것이 의심스럽다면, 상태도를 보면 된다.

