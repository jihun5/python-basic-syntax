# 딕셔너리 자료형은 key와 value로 이루어져있다.
# 영어 사전에서 단어와 뜻으로 이루어져 있던 것에서 유래
# key : 핵심 -> value : 가치(값), 키값 = value
dic1 = {'이름': '홍길동', '나이':25, '성별':'남'}
# set과 dictionary는 거의 유사함

# 딕셔너리의 특징 1
# key는 중복이 불가, value는 다른 key에도 존재할 수 있다.

# 파이썬 에서의 dictionary는 다른언어에서는 ditcionary 는 hashmap, or map으로 부른다
# 다른 language(java, javascript 등)의 map(key, value) 또는 
# hashmap(key, value, 암호화 함수(비밀번호 ->변수+비밀번호, 원래 비밀번호를 모르게))과 유사한 자료형
# json 이라는 자료형태와도 유사하다.(JSON은 JavaScript 객체 리터럴(콘텐츠 그대로 대입), 
# 배열, 스칼라 데이터(단 하나의 값만 저장할 수 있는 데이터)를 표현하는 텍스트 기반의 방식입니다.)
dic1 = {'이름': '홍길동', '나이':25, '성별':'남', '성별':'여'}
# dic1 = {'이름': '홍길동', '나이':25,' 몸무게':25 ,'성별':'남', '성별':'여'} value는 중복이 가능
print(dic1) # 같은 key 값이 출력이 되지 않고 {성별 : '여'} 만이 출력됨
result = {'1':80, "2":90, '3':100, '4':10}
print(result) 

# 딕셔너리의 기본호출 방식은 변수명[key], 변수명.get(key)
print(dic1['나이'])
print(dic1.get('나이'))

# 리스트는 a = [value, ...] 딕셔너리는 a = {key:value, ...} 튜플은 a = (value, ...)
# 리스트와 튜플은 a[index], 딕셔너리는 a[key]

# 딕셔너리의 특징 2 index(순번)
# key와 value로 이루어져 이루어져 있다보니, 순서가 의미가 없다. index로 접근 불가(순차적 data X)
# key를 가지고 value를 검색할때 해시함수를 통해 index를 찾다보니, 매우 빠른 속도를 보장
# ex) 키값을 난수로 표현(순서가 중구난방이 됨)
# -> 비밀번호를 입력시 바로 로그인이 되는 방식(key값), 
# -> 리스트의 경우 n번째까지 찾아보고 나의 비밀번호를 찾아야 로그인이 되는 방법
# -> 리스트 보다 딕셔너리의 처리 속도가 훨씬 빠른 이유

# key:value 추가
dic1 = {'이름': '홍길동', '나이':25, '성별':'남', '성별':'여'}
dic1['신분'] = '학생'
print(dic1)

# 딕셔너리에서 키를 이용한 key:value 삭제
del dic1['성별']
print(dic1)

# 딕셔너리에서 key 목록만을 뽑아낼때
# iterable한 형태로 data가 뽑아져 나오므로 for문 사용가능
keylist = dic1.keys()
print(keylist)

# 위의 keylist에서 각각의 값을 출력해보자.
# 출력값 
# 이름
# 나이
# 신분
for k in keylist:
    print(k)
#  = for k in dic1:
#      print(k)
# for i in range(0, len(keylist)):
#     print(keylist[i]) -> index 값을 가지고 있지 않다는 증거

# value 목록을 뽑아낼때는 .values()
valuelist = dic1.values()
print(valuelist)
for i in valuelist:
    print(i)

for v in dic1.values():
    print(v)

# dic1 = {'이름': '홍길동', '나이':25, '성별':'남', '성별':'여'}
# 키 값을 출력해주는 for 문 안에서 value 값도 같이 출력해보자
for k in keylist:
        print(k)
        print(dic1[k])

#  clear 변수명.clear() key : value 값 모두 한꺼번에 삭제하는 방법
dic1.clear()
print(dic1)

# 위의 for 문을 활용해서 key가 담긴 list를 만들고, value가 담긴 list를 만들어보기
# 1.
# lista = list(dic1.keys())
# print(lista)
# listb = list(dic1.values())
# print(listb)
# 2. append
t1 = []
t2 = []
for k in keylist:
        t1.append(k) # t1 = [] 반복시 계속 리셋이되기때문에 for문 안에 넣으면 안된다
        t2.append(dic1[k])
print(t1)
print(t2)

# 딕셔너리의 확장 : update함수
dic1 = {"a":1, "b":2, "c":3}
dic2 = {"a":2, "d":4, "f":5}
dic1.update(dic2)
print(dic1) # 중복되는 key 값 a:1 삭제후 a:2 남음

lista = ['A', 'A', 'B','O','O','AB','AB']
# 딕셔너리로 변환해서 출력해보자
# 예를 들어 'A':2, 'B':1 .. 등으로 출력 되도록 코딩해보자. not in, in
# hint : a not in dicta.key() if p1 not in payMethod: # not in 포함이 되지 않으면(범위 안에없으면 참)
# dicta = {}
# count = 0
# if "A" in lista:
#     print(lista.count("A")) A가 2개 있다.
# if "B" in lista:
#     print(lista.count("B")) B가 1개 있다.

#  dicta에 'A':1 을 어떻게 세팅하는가?
#  dicta["A"] = 2
# dicta = {}
# for a in lista:
#     if 'A' in lista:
#         dicta['A'] = lista.count("A")
# print(dicta)

# 방법 1
dicta = {}
for a in lista:
    if a not in dicta.keys():
        dicta[a] = 1 # A:1
    else:
        dicta[a] = dicta[a] + 1
print(dicta)

# 방법 2
if a not in dicta.keys():
    dicta[a] = lista.count(a)
print(dicta)