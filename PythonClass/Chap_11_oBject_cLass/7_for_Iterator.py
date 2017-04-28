

# 우리가 당연하게 사용했던 위와 같은 for문은 사실 range()로
# 생성된 list가 iterable 하기 때문에 member들을 불러서
# 사용이 가능했던 것
# for 문의 range

# 예제
x=[1,2,3]

type(x)

y=iter(x)
print(type(y))
print(next(y))
print(next(y))
print(next(y))


