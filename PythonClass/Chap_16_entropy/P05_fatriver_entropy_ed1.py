"""
아래에서 구한 분할 후 엔트로피를 이용해서, 결정트리를 만드는데 필요한 함수를 구현하시오.


"""
"""
지방간 엔트로피 지수 구하기

dataset = ['age','gender','drink','smoke','Fatliver']
headset = ['age','gender','drink','smoke']

"""


"""

엔트로피 계산이 정정되었음.

분할 전 엔트로피 = 종속변수에 해당하는 변인의 엔트로피값
분할 후 엔트로피 = 독립변수X1 X 종속변수Y 간의 엔트로피값


사실상 분할 후 엔트로피만 구해서 결정트리를 구성해도 무방하다는 뜻

문제 363. 쿠폰 반응여부에 대한 데이터를 가지고 분할 후 엔트로피를 구하시오!

            준비물
1. inputs 데이터 필요 [ {}, true ]   -- raw형태로 준비하지말고, 함수로 구성하게 만들기
2. entropy, data_entropy, partition_entropy, class_prob.. , partition by.. 메쏘드



"""



# import math  # 엔트로피 계산에 로그함수를 쓰기 위해 math 모듈을 불러온다.

# import collections  # 분석 컬럼별 확률을 계산하기 위해 만드는 class_probabilities를 함수로 만들기 위해 사용하는 모듈을 불러온다.
# 자세히 설명하면 collection.Counter 함수를 사용하기 위함인데
# collection.Counter() 함수는 Hashing(책 p.110 참조) 할 수 있는 오브젝트들을
# count 하기 위해 서브 클래스들을 딕셔너리화 할 때 사용한다.

from functools import partial  # c5.0(엔트로피를 사용하는 알고리즘) 알고리즘 기반의 의사결정트리를
# 제작하는 트리제작함수인 build_tree_id3에서 사용하는데
# functools.partial() 함수는 기준 함수로 부터 정해진 기존 인자가 주어지는 여러개의 특정한 함수를 만들고자 할 때 사용한다.
# http://betle.tistory.com/entry/PYTHON-decorator를 참조

# from collections import defaultdict  # 팩토리 함수는 특정 형의 데이터 항목을 새로 만들기 위해 사용되는데


# defaultdict(list) 함수는 missing value(결측값)을 처리 하기 위한
# 팩토리 함수를 불러오는 서브 클래스를 딕셔너리화 할 떄 사용한다.


#########################   데이터셋   #################################
# 데이터셋 = [ ( {데이터가 되는 컬럼의 키와 값으로 구성된 딕셔너리}, 분석타겟컬럼의 값  ) , ..... ]
# 분석 타겟 컬럼 : 라벨(label)
# 분석에 사용하는 데이터가 되는 컬럼 : 어트리뷰트(attribute) - 속성
# 분석에 사용하는 데이터의 값 : inputs


import csv
import math               # 엔트로피 계산에 로그함수를 쓰기 위해 math 모듈을 불러온다.
import collections
from collections import defaultdict


inputs = list()  # 최종적으로 사용할 데이터셋의 형태가 리스트여야 하기 때문에 빈 리스트를 생성합니다.
temps = []
file = open("d:/data/fatliver3.csv", "r")  # csv 파일로 데이터셋을 불러옴
coupon_csv = csv.reader(file)
for i in coupon_csv:
    temps.append(i)  # 데이터 값
# print(temps)  #[['남', '30대', 'NO', 'YES', 'NO', 'NO'],[ ..] ,[.. ] , .. [ ..] ]
column_set = ['age','gender','drink','smoke','Fatliver']  # 데이터의 라벨(컬럼명)

for data in temps:  # 위처럼 리스트로 된 데이터값과 리스트로된 라벨(컬럼명)을 분석에 맞는 데이터형태로 바꾸는 과정.
    temp_dict = {}  # 데이터셋 = [ ( {데이터가 되는 컬럼의 키와 값으로 구성된 딕셔너리}, 분석타겟컬럼의 값  ) , ..... ] 의 형태로 되어있어야 분석할 수 있다.
    affect_params = len(column_set) - 1  # 데이터셋의 최종값을 타겟변수로 두었기 때문에 타겟변수는 데이터값 딕셔너리에 넣지 않습니다. 분석타겟변수의 위치를 잡아주는 값
    for i in range(affect_params):  # 타겟변수를 제외한 나머지 변수들로 딕셔너리에 데이터를 입력
        if i != affect_params:  # 생성한 딕셔너리와 넣지 않은 타겟변수를 분석을 위한 큰 튜플안에 입력
            temp_dict[column_set[i]] = data[i]  #  {gender : ['남', '30대', 'NO', 'YES', 'NO', 'NO'] }
    inputs.append(tuple((temp_dict, True if data[affect_params] == 'yes' else False)))  #





head_set = ['age','gender','drink','smoke']

def class_probabilities(labels):       # 엔트로피 계산에 사용하는 컬럼의 확률을 계산하는 함수
    total_count = len(labels)
    return [count / total_count for count in collections.Counter(labels).values()]


def entropy(class_probabilities):
    return sum(-p * math.log(p, 2) for p in class_probabilities )


def partition_by(inputs, attribute):
    groups = defaultdict(list)
    for input in inputs:
        key=input[0][attribute]
        groups[key].append(input)
    return groups

for key in head_set:
    print(partition_by(inputs,key).values())


def data_entropy(labeled_data):
    labels = [label for _, label in labeled_data]  #_는 그냥 i don't care >> 즉, labels는 키-밸류 중 밸류 값(True,False)들만 저장해놓은 리스트가 된다.
    probabilities = class_probabilities(labels)
    #print (entropy(probabilities))
    return entropy(probabilities)


def partition_entropy(subsets):         # 파티션된 노드들의 엔트로피
    total_count = sum(len(subset) for subset in subsets)        # subset은 라벨이 있는 데이터의 리스트의 리스트이다. 이것에 대한 엔트로피를 계산한다.
    #for subset in subsets:
        #print (len(subset))
        #print (data_entropy(subset))
    return sum(data_entropy(subset) * len(subset) / total_count for subset in subsets)


for key in head_set:
    #print( partition_by(inputs,key).values())
    print (key,partition_entropy( partition_by(inputs,key).values()))






