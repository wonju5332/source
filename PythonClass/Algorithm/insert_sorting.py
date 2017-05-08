
a = [10,5,8,9,20]

def insert_order(a):
    for i in range(len(a)-1):    # range(4)   -->  i = 0     , i = 1        , i = 2
        for j in range(i+1):      # range(1)   --> j = 0, 1  , j = 0, 1, 2  , j = 0, 1, 2, 3
            if a[j]>=a[i+1]:
                temp = a[i+1]
                for k in range(i+1,j,-1) :
                   a[k] = a[k-1]
                a[j] = temp
    return a


"""
버블정렬을 python 으로 구현한 코드
필요한 메소드는 2가지이다.

1 . 두수의 크기를 비교하는 메소드 ( for loop문)
2 . 두 수를 swich 하는 메소드   ( for loop문)

"""

# i = 0  j = 0   --> a[0] >= a[1]   10  >= 5--> temp = a[1]