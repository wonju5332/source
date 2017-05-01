"""
임의의 문장을 입력받아 각 단어별로 나눈 후에 단어들의 중복되는 개수를 구하는 프로그램을 작성하시오.
 
<처리조건>
(1) 입력된 스트링은 글자의 제한은 없다. 즉 공백이나 ', ' 등도 입력으로 들어 올 수 있다. 
(2) 입력된 문장에서 각 단어사이의 구분은 공백으로 한다. 
(3) 단어에는 공백을 제외한 단어들만이 포함된다.

"""

"""
임의의 문장을 입력받는다.(문장의 길이는 200 이하)
하나의 결과가 나온 후에도 계속 새로운 입력을 받다가, "END"가 입력되면 프로그램을 종료한다.

"""
"""
각 단어들의 발생 빈도를 사전순으로 출력한다.     sorted 
<입력 >
I AM DOG DOG DOG DOG A AM I 
I AM OLYMPIAD JUNGOL JUNGOL OLYMPIAD
END

<출력>
A : 1
AM : 2
DOG : 4
I : 2

-----------초기화

AM : 1
I : 1
JUNGOL : 2
OLYMPIAD : 2
ssdfdfdf
명령어 식으로 end들어가야함..
key 

"""

# list = 'I AM DOG DOG DOG DOG A AM I I AM OLYMPIAD JUNGOL JUNGOL OLYMPIAD '  #나중에는 input식으로
# def print_hist(h):
#     for i in h:
#         print(h[i])
#
# h = 'parrot'
# print_hist(h)
# import operator
# def histogram():
#     while True:
#         d = dict()
#         list = input('문장을 입력하세요.')
#         if list == 'end':            # input값으로 end를 작성한다면?
#             print('Off the ProGram') # 프로그램 종료 실행하라.
#             break
#         else:                        # 그렇지 않다면
#             for i in list.split(' '): # 입력된 문장들의 단어를 쪼개어라.
#                 if i not in d:  # 첫번째 단어가 dict안에 없다면?
#                     d[i] = 1    # 단어 와 1을 key- value로 셋팅하라.
#                 else: d[i] += 1   # 같은 단어가 한번 더 나오면 +1하라.
#             sorted_d = sorted(d.items(), key=operator.itemgetter(0))  # dict의 key를 기준으로 오퍼레이터를 이용해서, sorting한다.
#         print(sorted_d)         #sorting된 결과를 리턴하라.
#
# histogram()













# def str_add():
#     word_list = []
#     while True:  #무한 반복
#         a = input('입력하세요.') # string 입력
#         if a == 'end':
#             break
#         else:
#             for i in a.split(' '):  # I am a boy
#                 if i in word_list:
#                     continue
#                 else:
#                     word_list.append(i)
#         print(word_list)
# str_add()