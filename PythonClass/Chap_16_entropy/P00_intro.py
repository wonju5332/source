"""
엔트로피 지수를 구해야 하는 이유는?
    정보 획득량을 구하기 위해서
    
    정복획득량 = 분할전 엔트로피(불확실성) - 분할 후 엔트로피 (불확실성)
    
분할 후 엔트로피가 적은 것이 가장 먼저 물어봐야 할 질문인 것이다.


"""


print('문제 345. 카드YN컬럼의 데이터의 분할 전 엔트로피를 구하시오.')
print('문제 346. 확률을 입력했을 때, 엔트로피를 출력하는 파이썬 함수를 생성하시오!')

from fractions import Fraction
import fractions
import math
a = Fraction(4,5)
a= (4,5)
print()


def entropy(pre,pst):
    a = Fraction(*pre)  #4/5
    b = Fraction(*pst)  #1/5
    sec_pre = a*math.log2(a)
    sec_pst = -(b*math.log2(a))

# entropy((4,5),(1,5))

print(sum(i for i in range(0,11)))


val = [0.8, 0.2]


def entro(val):
    print(sum(-i*math.log2(i) for i in val))
    print(type([i for i in val]),'워우')
    print((i for i in val),'와아')
entro(val)



print('아래의 리스트 변수에 있는 y와 n이 y가 4개있고, n이 1개 있다는게 자동으로 구분되어지게 하려면?')


from collections import Counter
card_yn = ['Y','Y','N','Y','Y']
card_ynk = ['Y','Y','N','Y','Y','K']
def class_prob(labels):
    return Counter(labels).values()
print(class_prob(card_yn))
print(class_prob(card_ynk))  #[idx] 안먹힘. dict.values는 idx안준다고 함.


def class_prob_2(labels):
    return Counter(labels)

print(type(class_prob_2(card_ynk).__getitem__('Y')))  #int형임. Y의 count값


print('위 코드를 이용해서 확률이 나올 수 있도록 출력되게 하라.')

def prob_cal(labels):
    tot_cnt = len(labels)
    return [i/tot_cnt for i in Counter(labels).values()]

print(prob_cal(card_yn))  #0.8 0.2



print('##########################################################')
print('위에서 만든 함수 2개(entropy, class_prob)를 가지고 card_yn의 엔트로피를 구하시오')
print('##########################################################')


def entro(val):
    return print(sum(-i*math.log2(i) for i in val))




def prob_cal(labels):
    tot_cnt = len(labels)
    return [i/tot_cnt for i in Counter(labels).values()]

entro(prob_cal(card_yn))



print('문제 352. 아래의 데이터 셋에서 a만 출력하려면?')

inputs = [('a','b'),('c','d')]
print(inputs[0][0])

print('아래의 데이터 셋에서 scott을 출력하려면?')

inputs=[{'ename' : 'scott'}, True]

print(inputs[0]['ename'])

print('문제 353. 아래의 결과에서 scott과 smith를 출력하려면?')

inputs = [{'ename' : 'scott'}, True,
          {'ename' : 'smith'}, False
          ]

print(inputs[0]['ename'],inputs[2]['ename'])
print([inputs[i]['ename'] for i in range(len(inputs)) if i%2 == 0])

print('문제 354. 아래의 데이터 셋에서 card_yn의 y와 n만 출력하려면?')

inputs = [({'ename' : 'scott','card_yn':'Y'}, True),
          ({'ename' : 'smith','card_yn':'N'}, False)
          ]



for input in inputs:
    print(input[0]['card_yn'])




print('문제 355. 아래의 inputs 데이터 셋에서 card_yn 의 y와 n을 groups라는 비어있는 리스트 변수에 넣으시오.')
groups = list()
inputs = [
         ( {'cust_name':'SCOTT', 'card_yn':'Y', 'review_yn':'Y', 'before_buy_yn':'Y'}, True),
         ( {'cust_name':'SMITH', 'card_yn':'Y', 'review_yn':'Y', 'before_buy_yn':'Y'}, True),
         ( {'cust_name':'ALLEN', 'card_yn':'N', 'review_yn':'N', 'before_buy_yn':'Y'}, False),
         ( {'cust_name':'JONES', 'card_yn':'Y', 'review_yn':'N', 'before_buy_yn':'N'}, True),
         ( {'cust_name':'WARD',  'card_yn':'Y', 'review_yn':'Y', 'before_buy_yn':'Y'}, True) ]


for input in inputs:
    groups.append(input[0]['card_yn'])
print('card_yn',groups)





print('##########################################################')
print('위 코드를 가지고, 아래의 결과가 출력되게 하시오.')
print('##########################################################')
# ['Y', 'Y', 'N', 'Y', 'Y']
# ['Y', 'Y', 'N', 'N', 'Y']
# ['Y', 'Y', 'Y', 'N', 'Y']


def column_data(inputs, key):
        groups = []
        for input in inputs:
            groups.append(input[0][key])
        print(groups)

for i in ['card_yn','review_yn','before_buy_yn']:
    column_data(inputs,i)


print('##########################################################')
print('아래와 같이 분할 전 엔트로피가 출력되게 위 코드를 수정하시오.')
print('##########################################################')





inputs = [
         ( {'cust_name':'SCOTT', 'card_yn':'Y', 'review_yn':'Y', 'before_buy_yn':'Y'}, True),
         ( {'cust_name':'SMITH', 'card_yn':'Y', 'review_yn':'Y', 'before_buy_yn':'Y'}, True),
         ( {'cust_name':'ALLEN', 'card_yn':'N', 'review_yn':'N', 'before_buy_yn':'Y'}, False),
         ( {'cust_name':'JONES', 'card_yn':'Y', 'review_yn':'N', 'before_buy_yn':'N'}, True),
         ( {'cust_name':'WARD',  'card_yn':'Y', 'review_yn':'Y', 'before_buy_yn':'Y'}, True) ]


def entro(val):
    return sum(-i*math.log2(i) for i in val)

entro(val)
def prob_cal(labels):
    tot_cnt = len(labels)
    return [i/tot_cnt for i in Counter(labels).values()]

print(prob_cal(card_yn))  #0.8 0.2

def column_data(inputs, key):
    groups = []
    for input in inputs:
        groups.append(input[0][key])
    return groups

print('분할 전 엔트로피')
for i in ['card_yn','review_yn','before_buy_yn']:
    yn = column_data(inputs,i)
    print(yn)
    p = prob_cal(yn)
    print(p)
    print(entro(p))


print('구매여부 컬럼으로 분할한 분할 후 엔트로피를 구하는 방법')

# True : 구매함 / False : 구매안함


# 분할 전 엔트로피 : sum( prob_i * log2(prob_i) for i in [A,B, ..Z] )
# 분할 후 엔트로피 :

# defaultdict() 란 말그대로 dictionary에 기본 값을 정의하고, value에 값이 없더라도 에러를 출력하지 않고 기본값을 출력하는 문법
import math
import collections
from collections import defaultdict
group1 = {}
group1['one']= 'a'  #정의 one:a

def noname():
    return 'a'

group2 = defaultdict(noname)
group2['one']
print(group2['one'])



group3 = defaultdict(lambda:'a')
print(group3['one'])


group4 = defaultdict(list)
group4['one']     #list: 'one'
print(group4['one'])


def column_data(inputs, column):
    groups = defaultdict(list)
    for input in inputs:
        key = input[0][column]
        # print('key',key)
        groups[key].append(input[1])
        # print(groups)
    return groups

for i in ['card_yn','review_yn','before_buy_yn']:
    yn = column_data(inputs,i)
    print(yn.items())


"""

[      ('Y', [True, True, True, True]), ('N', [False])       ]
[      ('Y', [True, True, True]), ('N', [False, True])       ]
[      ('Y', [True, True, False, True]), ('N', [True])       ]


"""


print('위의 column_data 함수와 아래의 part..함수를 이용해서 분할 후 엔트로피를 아래와 같이 출력되게 하쇼')


