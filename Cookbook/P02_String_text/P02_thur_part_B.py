
"""
▶ 2.9 유니코드 텍스트 노멀화 ◀ 
♣ 문제 : 유니코드 문자열 작업을 하고 있다. 이때 모든 문자열에 동일한 표현식을 갖도록 보장하고 싶다면?
 ↘ 해결 : 유니코드에서 '몇몇' 문자는 '하나 이상의 유효한 시퀀스 코드 포인트' 로 표현할 수 있다.
        
            필요한 것   
                        import unicodedata
                        normalization 메소드    # 첫번째 인자에는 문자열을 어떻게 노멀화할것인지
                                                # ex) NFC = 문자를 정확히 구성하도록 지정
                                                      NFD = 문자를 여러 개 합쳐서 사용하도록 지정
                                                      NFKC = 분리..?
                                                      NFKD = 분리..?
                        
 """
print('########################################## 2.9 유니코드 텍스트 노멀화 #####################################')

s1 = 'Spicy Jalape\u00f1o'  # (U + 00F1)
s2 = 'Spicy Jalapen\u0303o' # (U + 0303)
print(s1)
print(s2)

print(s1 == s2) # False

print(len(s1))
print(len(s2))


# 여러 표현식을 갖는다는 것은 문자열을 비교하는 프로그램의 측면에서 문제가 된다.
# 문제를 해결하기 위해서는 unicodedata 모듈로 텍스트를 노멀라이제이션 해서
# '표준 표현식'으로 바꿔야 한다.

import unicodedata

# NFC 노멀라이제이션
t1 = unicodedata.normalize('NFC', s1)           #NFC = 문자를 정확히 구성하도록 지정
t2 = unicodedata.normalize('NFC', s2)
print(t1) #Spicy Jalapeño
print(t2) #Spicy Jalapeño
print(ascii(t1)) #'Spicy Jalape\xf1o'
print(ascii(t2)) #'Spicy Jalape\xf1o'
print(t1==t2) #return True

# NFD 노멀라이제이션
t3 = unicodedata.normalize('NFD',s1)            #NFD = 문자를 여러 개 합쳐서 사용하도록 지정
t4 = unicodedata.normalize('NFD',s2)
print(t3) #Spicy Jalapeño
print(t4) #Spicy Jalapeño
print(ascii(t3)) #'Spicy Jalapen\u0303o'
print(ascii(t4)) #'Spicy Jalapen\u0303o'
print(t3==t4) # Return True

s = '\ufb01'  #단일 문자
print(s)
s = unicodedata.normalize('NFD',s)
print(s) #ﬁ  <<얘랑 아래 분리한 애는 fi  하나는 붙여서 1바이트, 하나는 분리시켜서 2바이트 ㅋㅋ

#합쳐 놓은 문자가 어떻게 분리되는지 살펴본다.
t3 = unicodedata.normalize('NFKD',s)
t4 = unicodedata.normalize('NFKC',s)
print(t3)
print(t4)


# 일관적이고 안전한 유니코드 텍스트 작업을 위해서 노멀화는 아주 중요하다.
# 특히 '인코딩' 을 조절할 수 없는 상황에서 사용자에게 문자열 입력을 받는 경우엔 특히 조심해야 한다.
# 또한 텍스트 필터링 작업을 할 때도 노멀화는 중요하다.
# 예를 들어, 텍스트에서 발음 구별부호를 모두 제거하고 싶다면 다음과 같이 해야 한다.

s1 = 'Spicy Jalape\u00f1o'  # (U + 00F1)
s2 = 'Spicy Jalapen\u0303o' # (U + 0303)
t1 = unicodedata.normalize('NFD',s1)
d = ''.join(c for c in t1 if not unicodedata.combining(c))
# combining() 함수는 문자가 결합 문자인지 확인한다. 이 함수 안에는, 문자 카테고리찾기/숫자찾기 등 많은 함수가 들어있다.
# join 은 특정 구분자를 포함해 문자열으로 변환한다.
print(d)            # Spicy Jalapeno






"""
▶ 2.10 정규 표현식에 유니코드 사용 ◀ 
♣ 문제 : 텍스트 프로세싱에 정규 표현식을 사용 중이다. 하지만 유니코드 문자 처리가 걱정될때에는?
 ↘ 해결 : re 모듈을 통해 정규표현식을 적용한다. 
            예를 들어, \d는 유니코드 숫자에 이미 매칭한다.
            
    주의사항 : 유니코드의 대소문자 매칭에 주의!             #같은 유니코드에 upper()를 하면 글자가 바뀌어버림
    
    third-party regex 라이브러리 설치 추천 (유니코드 핸들링 유용)
 """
print('########################################## 2.10 정규 표현식에 유니코드 사용 #####################################')

import re
num = re.compile('\d+')

#   아스키(ASCII)숫자
a = num.match('123')
print(a) #<_sre.SRE_Match object; span=(0, 3), match='123'>

#   아라비아 숫자
b = num.match('\u0661\u0662\u0663')  #123...?
print(b) #<_sre.SRE_Match object; span=(0, 3), match='١٢٣'>


# 특정 유니코드 문자를 패턴에 포함하고자 한다면??
# >> 유니코드 문자에 escape 시퀀스를 사용한다.
# 예를 들어, 아라비아 코드 페이지의 모든 문자에 매칭하는 정규표현식은 다음과 같다.

arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')    #모든 문자에 매칭하는 정규 표현식

# 검색 수행 전 '텍스트 노멀화'를 꼭 하는 것이 좋다.
# 주의사항으로, 대소문자 무시매칭에 대소문자 변환을 합친 코드가 좋다.
print('stra\u00dfe')   #straße
pat = re.compile('stra\u00dfe', re.IGNORECASE)
s = 'straße'
d = pat.match(s)
print(d)   # <_sre.SRE_Match object; span=(0, 6), match='straße'> ===>  일치

# 대문자로 변환 후 매치해보기 결과는?
print(s.upper())  #  STRASSE
print(s.lower())
e = pat.match(s.upper())
print(e)   # None ===>   불일치  !! 왜??
# 즉   stra\u00dfe <패턴은 straße < 얘를 일치시키는데,
# upper를 갈겨놓으면  STRASSE << 이렇게 변해서, 불일치!!


######### 유니코드와 정규표현식을 사용해야 한다면,
######### 서드파티(third-party) regex 라이브러리를 설치 후
######### 유니코드 대소문자 변환 등을 기본으로 제공하는 많은 기능 이용 추천






"""
▶ 2.11 문자열에서 문자 잘라내기 ◀ 
♣ 문제 : 텍스트의 처음, 끝, 중간에서 원하지 않는 공백문 등을 잘라내고 싶다.
 ↘ 해결 : strip() 메소드를 사용하면 문자열의 처음과 끝에서 문자를 잘라낼 수 있다. 
           lstrip() 과 rstrip()은 문자열의 왼쪽과 오른쪽의 문자를 잘라낸다.
           기본적으로 이 메소드는 공백문을 잘라내지만 원하는 문자를 지정할 수도 있다.
 """
print('########################################## 2.11 문자열에서 문자 잘라내기 #####################################')

# 공백문 잘라내기!

s = '        hello world \n'
a = s.strip()
b = s.lstrip()
c = s.rstrip()
print(a)
print(b)
print(c)
####### >> '         ' 도 잘라낼 수 있고, \n도 잘라낼 수 있다!

# 문자 잘라내기!

t = '----------hello==========='
a = t.lstrip('-')
b = t.rstrip('=')
c = t.strip('-=')
print(a)
print(b)
print(c)

#########    데이터를 보기 좋기 만들기 위한 용도로 여러 strip() 메소드를 일반적으로 사용함
#########    ex ) 문자열에서 공백문을 없애거나 인용 부호를 삭제하거나 하는 식이다.
#########    하지만 텍스트의 중간에서 잘라내기를 할 수는 없다.


s = '  hello          world     \n'
d = s.strip()      #hello          world
print(d)

#위 코드는 문자열 중간의 공백문이 사라지지 않았다. 이 부분을 처리하려면 replace() 나 정규표현식 치환을 해야 함.

d = s.replace(' ', '')
print(d)
import re
e = re.sub('\s+', ' ', s)
print(e)

# 때로는 파일을 순환하며 데이터를 읽어 들이는 것과 같이 다른 작업과 문자열을
# 잘라내는 작업을 동시에 하고 싶을 수가 있다.
# 이럴 때는 생성자 표현식 사용하는게 좋음

with open("d:/data/emp2.csv") as f:
    lines = (line.strip() for line in f)  # 데이터 변환 담당, 임시 리스트로 만들지 않고 바로 하니까 효율적
    for line in lines:                    # 단지 잘라내기 위한 작업이 적용된 라인을 순환하느 이터레이터 생성할 뿐
        print(line)

# 추가적인 기술은 translate() 메소드가 있다.



"""
▶ 2.12 텍스트 정리 ◀ 
♣ 문제 : 웹페이지에 어떤 사람이 유니코드 텍스트를 입력했다. 이를 정리하고 싶다.
 ↘ 해결 : 텍스트 정리 작업은 크게        1. 텍스트 파싱           2. 데이터 처리 와 관련 있음
           단순한건?      str.upper , str.lower 로 텍스트를 표준케이스로 변환
             또는         str.replace() , re.sub()를 사용한 치환은 특정 문자 시퀀스를 없애거나 바꾸는데 집중할 수 있음
            또는       unicodedata.normalize() 를 사용해서 텍스트 노멀화 시킬 수 있다.
            
            하지만 더 고급적인 게 있음.
            ex) 특정 범위의 문자 or 발음 구별 구호를 없애려고 할 때는 str.translate() 메소드를 사용해야 한다.
            
 """
print('########################################## 2.11 문자열에서 문자 잘라내기 #####################################')



s = 'p\xfdt\u0125\xf6\xf1\x0cis\tawesome\r\n'
print(s)
print(s)

# 문자열에서 공백문을 잘라내보기
# 1. 먼저 작은 변환 테이블을 만들어야 한다.
remap = {
    ord('\t') : ' ',
    ord('\f') : ' ',
    ord('\r') : None      # 삭제됨
}

#############################################

a = s.translate(remap)
print('whitespace remapped:', a)


import unicodedata
import sys
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
                         if unicodedata.combining(chr(c)))

b = unicodedata.normalize('NFD', a)
c = b.translate(cmb_chrs)
print('accents removed:', c)


d = b.encode('ascii','ignore').decode('ascii')
print('accents removed via I/O:', d)
aa
aa