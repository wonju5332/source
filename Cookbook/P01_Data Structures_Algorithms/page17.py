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

"""
문제 :     프로그램 코드에 슬라이스(slice)를 지시하는 하드코딩이 너무많아 이해하기 어려울 때, 이를 정리하려면?
해결 : 
"""