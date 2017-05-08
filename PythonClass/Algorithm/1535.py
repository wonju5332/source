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


import time
def test_dict_if():
    d = {}
    start = time.time()
    for i in range(1000000):
        if i in d.keys():
            d[i] +=1
        else:
            d[i] = 1
    print(time.time()- start)

test_dict_if()


