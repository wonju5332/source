#1.10 순서 깨지 않고, 시퀀스 중복 없애기

#해시 가능한 타입
def dedupe(items):
    seen = set()
    for i in items:
        if i not in seen:
            yield i
            seen.add(i)
a = [1,5,2,1,9,1,5,10]
print(list(dedupe(a)))


#해시 불가능한 dict 타입

# example2.py
#
# Remove duplicate entries from a sequence while keeping order

def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item   # yield 는 글로벌한 함수이다. 비휘발성임.
            seen.add(val)

if __name__ == '__main__':
    a = [
        {'x': 2, 'y': 3},
        {'x': 1, 'y': 4},
        {'x': 2, 'y': 3},
        {'x': 2, 'y': 3},
        {'x': 10, 'y': 15}
        ]
    print(a)
    print('#############################################')
    print(list(dedupe(a, key=lambda a: (a['x'],a['y']))))





#1.11 슬라이스 이름 붙이기
# 특정 문자열을 자르고 이름 붙이기

"""
문제 :     프로그램 코드에 슬라이스(slice)를 지시하는 하드코딩이 너무많아 이해하기 어려울 때, 이를 정리하려면?
해결 :    고정된 문자열로부터 특정 데이터를 추출하는 코드가 있다고 가정해보자.
        다음과 같이 하면 어떨까?
        SHARES = slice(20,32)
        PRICE = slice(40,48)
        
필요한 함수 : slice()
            s.start / s.stop / s.step
            indices

"""
print('#############################################')
items = [0,1,2,3,4,5,6]
a = slice(2,5,2)
print(items[2:4])  # 2부터
items[a]= [10,11]   # 2:4까지의 값을 10,11 으로 치환?
print(items)
del items[a]        # 10,11으로 치환 한 것을 삭제한다?
print(items)


# slice 인스턴스 활용 / s.start / s.stop / s.step 속성 활용하기
print('#############################################')
# a = slice(10,50,30,50)  #TypeError: slice expected at most 3 arguments, got 4
b = slice(5,10,2)
# print(b.start)
print(b.start)
print(b.stop)
print(b.step)

# 10 <= 50  / 3씩+


s= 'HelloWorld'
print(b.indices(len(s))) #튜플
for i in range(*b.indices(len(s))):
    print(s[i])




#1.12 시퀀스에 가장 많은 아이템 찾기

"""
문제 : 시퀀스에 가장 많이 나타난 아이템을 찾고 싶다.
해결 : collections.Counter 클래스를 활용하면 됨


필요한 것 : collections 모듈 /  Counter 클래스
          most_common() 메소드
"""

words = [
   'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
   'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
   'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
   'my', 'eyes', "you're", 'under'
]


from collections import Counter
word_cnts = Counter(words)
top_three = word_cnts.most_common(3)
print(top_three)

print(word_cnts['not']) # 1
print(word_cnts['eyes']) #8


#위 방법 말고, 카운트를 수동으로 느리기

morewords = ['why','are','you','not','looking','in','my','eyes']
for i in set(words):
    word_cnts[i] +=1
print(word_cnts['eyes'])

word_cnts.update(set(words))

a = Counter(words)
b = Counter(list(set(words)))
print(a)
print(b)
#합집합
c = a + b
print(c)
#차집합
d = a - b
print(d)

print('#############################################')
#1.13 일반키로 딕셔너리 리스트 정렬

"""
문제 : 딕셔너리 리스트가 있고, 하나 혹은 그 이상의 딕셔너리 값으로 이를 정렬하고 싶다.
해결 : operator 모듈 / itemgetter 함수 활용

"""

# 어느 웹사이트 회원 리스트를 데이터 베이스로부터 불러와 다음과 같은 자료구조 만들었다.
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

# 모든 딕셔너리에 포함된 필드 기준, 데이터 정렬 후 출력

# operator.itemgetter() 함수는 rows레코드에서 원하는 값을 추출하는데 사용하는 인덱스를 인자로 받는다.
# 딕셔너리 키 이름 or 숫자 리스트 요소가 될 수도 있고, 객체의 __getitem__() 메소드에 넣을 수 있는 ㅗ든 값이 가능하다.

from operator import itemgetter

rows_by_fname = sorted(rows, key = itemgetter('fname'))
rows_by_uid = sorted(rows, key = itemgetter('uid'))

print(rows_by_fname)# fname을 기준으로 (abc..)
print(rows_by_uid)# uid를 기준으로  (1001 1002..)

print('#############################################')
# itemgetter 함수에는 키를 여러 개 전달할 수도 있다.
rows_by_lfname = sorted(rows, key= itemgetter('lname','fname'))
print(rows_by_lfname)


# itemgetter()의 lambda 표현식 대체
print('#############################################')
rows_by_fname = sorted(rows, key= lambda r: r['fname'])
rows_by_lfname = sorted(rows, key = lambda r: (r['lname'],r['fname']))

print(rows_by_fname)
print(rows_by_lfname)


# min max에도 itemgetter 활용해보기
print('#############################################')
min_rows = min(rows, key = itemgetter('uid'))
max_rows = max(rows, key = itemgetter('uid'))

print(min_rows)
print(max_rows)

