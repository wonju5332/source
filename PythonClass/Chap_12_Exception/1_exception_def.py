print('예제')

# def my_power():
#     try:            #문제가 없을 경우 실행할 코드
#         x = input('분자 숫자를 입력하세요.')
#         y = input('분모 숫자를 입력하세요.')
#         return int(x)/int(y)
#     except:         #문제가 생겼을 경우 실행할 코드
#         print('ERROR - 000 / 0으로 나눌 수 없습니다.')
#
# print(my_power())


# def my_power():
#     try:
#         x = input('')
#         y = input('')
#         return int(x)/int(y)
#     except:
#         print('예외발생')
# print(my_power())
# print('예외에 별칭처리 하기')

#
# def my_power():
#     try:            #문제가 없을 경우 실행할 코드
#         x = input('분자 숫자를 입력하세요.')
#         y = input('분모 숫자를 입력하세요.')
#         return int(x)/int(y)
#     except ZeroDivisionError as err:
#         print('0으로 나눌 수 없습니다..',err)
#     except:         #문제가 생겼을 경우 실행할 코드
#         print('ERROR - 000 / 다른 예외입니다.')
#
# print(my_power())


print('이름을 물어보게 하고, 이름을 입력하면 해당 사원의 월급이 출력되는 함수를 생성하라.')
#
# import pandas as pd
# def find_sal():
#     try:
#         emp = pd.read_csv("d:/data/emp.csv")
#         name = ''
#         while name == '':
#             name = input('이름을 입력하세요').upper()
#         sal = emp[['sal']][emp['ename'] == name].values[0]
#         return sal
#     except:
#         print('해당 사원 없음')
#
# print(find_sal())

# print(find_sal())

print('문제 182. 직업을 물어보게 하고, 직업을 입력 -> 직업 토탈월급 출력 아무것도 입력X -> 계속 물어보고 잘못된 직업 입력 -> 해당 직업 없음 출력')
#
# import pandas as pd
# def find_sal2():
#     try:
#         emp = pd.read_csv("d:/data/emp.csv")
#         your_job = ''
#         while your_job == '':
#             your_job = input('직업을 입력해주세요').upper()
#             sal = emp['sal'][emp['job']==your_job].sum()
#             return sal
#     except:
#         print('해당 직업 없습니다.')
#
# print(find_sal2())
print('문제 183. 이름 물어보고 해당 사원의 월급이 출력되게 하라.  없는 이름 - > 해당사원 없음 출력 있는 이름 - > 월급 추출에 성공했다 출력')
# import pandas as pd
# def find_sal3():
#     try:
#         emp = pd.read_csv("d:/data/emp.csv")
#         name = input('이름 입력하세요')
#         sal = emp['sal'][emp['ename'] == name.upper()].values[0]
#         #return sal  --> return절을 쓰면 else처리에서 인식이 안됨
#         print(sal)
#     except Exception as err:
#         print('해당 사원 없음')
#     finally:       #except가 실행되도, 무조건 실행 O
#         print('월급 추출에 성공했다.')
#
# find_sal3()


print('문제 184. 방금 사용한 else를 이용해, 아래의 나눈 값을 출력하게 되는데, 두 수를 물어보게 하고 나눈 값을 출력할 떄 정상적으로 나눠지면 ')
print('나눈 값을 잘 추출했습니다. 를 출력하고 0으로 나누면 0으로 나눌 수 없습니다 출력')


# def div_int():
#     try:
#         num1 = int(input('첫번째 수는 ~ ?'))
#         num2 = int(input('두번째 수는 ~ ?'))
#         result =num1/num2
#     except ZeroDivisionError as err:
#         print(" 1) 0으로 나눌 수 없습니다.")
#     except:
#         print(" 3) 잘못된 값을 입력했습니다.")
#     else:
#         print(' 2) 정상적으로 출력되었어요.')
#         return result
#
# print(div_int())



print('예제')

# import pandas as pd
# def find_sal2():
#     try:
#         emp = pd.read_csv("d:/data/emp.csv")
#         totsal = emp.groupby('job')['sal'].values[0]
#
#         return totsal
#     except Exception as err:
#         print('해당 직업 없습니다.')
#     finally:
#         print('저는 일단 작업을 마무리 지을겁니다.')



print('Exception 클래스      ####           예제')

# def my_power():
#     try:
#         x=input('분모 숫자를 입력하라')
#         y=input('분자 숫자를 입력하라')
#         return int(x) / int(y)
#     except Exception as err:
#         print("예외발생함")
#     except ZeroDivisionError as err:
#         print('0으로 어떻게나눠. 불가능이지')
# my_power()



# class bird:
#     def fly(self):
#         raise NotADirectoryError
#
# class eagle(bird):
#     def fly(self):
#         print("very fast")
#
#
# eagle = eagle()
# eagle.fly()









print("사용자 정의 예외 처리")
#
# import pandas as pd
# def find_sal():
#     emp = pd.read_csv("d:/data/emp.csv")
#     name = input('사원 이름을 입력하세요').upper()
#     sal = emp['sal'][emp['ename']==name].values[0]
#     if sal >= 3000:
#         raise Exception("월급이 3000 이상이면 볼 수 없어요.")
#     else:
#         return sal
#
# print(find_sal())
#
# print('1부터 9 사이에 숫자를 받게 해서 해당 숫자를 출력하는 함수를 생성하는데,')
# print('1부터 9 사이가 아니면 , 잘못 입력했다. 라는 에러메세지가 나오게 하라')
#
#
#
# def get_number():
#         num = int(input('1부터 9 사이의 숫자를 입력하세요.'))  # null
#         if num < 1 or num > 9:
#             raise Exception("숫자 범위를 초과하여 입력했습니다.")
#         else:
#             return num
#
# print(get_number())

print('190. 1부터 9까지의 숫자 이외의 것을 입력하면, 다시 입력창이 뜨도록 하라.')






print('191. 이번에는 1번부터 9번 사이외에 숫자를 넣으면 다시 물어보게 할 뿐만 아니라 입력을 안해도 다시 물어보게 코드를 수정하시오 ! ')

#
# def get_number():
#     num = 0
#     while num not in range(1,10):
#             try:
#                 num = int(input('1부터 9 사이 숫자 입력하세요.'))
#             except ValueError:
#                 continue
#             return num

