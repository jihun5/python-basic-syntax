# 로또 번호 생성기
# 랜덤의 값을 추출하는 파이썬 라이브러리 -> random
import random
print(random.randint(1,45))
# 리스트의 크기가 6개인 리스트를 만들어서, 오늘의 로또 번호를 만들어보자.(while문 써서))
# 저 문을 6번 반복하면 된다.
import random
A = random.randint(1,45)
lista = []
# a = 0
# while True:
#     if listvalues < 6:
#         continue

# 내가 한거 무엇이 잘못되었나 보기
# a = 0
# lista = []
# while alistvalues < 6:  # 여기가 잘못됐으.. a = 6
#     listvalues = int(input("값을 입력하시오:"), random.randint(1,45)) #int, input을 할 필요가 없었으
#     lista.append(listvalues) 
#     a += 1
# print(lista)


a=0
lista = []
while a < 6:
    randNum = random.randint(1,45)
    lista.append(randNum)
    a+=1
print(lista)
    
# while True:
#     listSize = int(input("리스트의 크기를 입력해주세요"))
#     if listSize>10:
#         print("다시 입력해주세요")
#         continue
#     a = 0
#     lista = []
#     while a < listSize:
#         listvalues = int(input("리스트의 값을 입력해주세요"))
#         lista.append(listvalues)
#         a += 1
#     print(lista)


# # for문의 기본 구조
# # for 변수 in 반복가능한자료형
# #     실행문
# lista = [1,2,3,4,5,6,7,8,9,10]
# for a in lista:
#     print(a) # 10번의 반복을 하게 됨

# # listb = ["a","b","c","d"]
# # for b in range(0, len(listb)):
# #     print(listb[b]) 파이썬 외에 언어 기본문법


# # range 문법
# for a in range(1, 101): # a, a-1의 범위 1부터 100까지는 1, 101
#      print(a, end=' ')

# 여기서 부터 오늘 한 거!

# range의 의미 : iteable 객체
v1 = range(1,10)
print(v1)

v1 = list(range(1,10))
print(v1)

# range(x,y) : x이상 y미만의 숫자를 담은 객체
# range(y) : 0이상 y미만의 숫자를 담은 객체

v1 = list(range(10,20))

#  for a in 리스트를 써서 v1의 값을 모두 출력
for a in v1:
    print(a)

# for a in range를 써서 v1[index]
for a in range(len(v1)): # range(0,10), range(0, len(v1))
    print(v1[a])
print(v1)

# 내가 한건디 위에꺼랑 비교했을 때 까비!
# for a in range(len(v1)):
#     print(a)      이렇게 다르네잉  print(v1[a])
# listx = [v1]
# print(listx)

# for a in 리스트 구문으로는 원본리스트 데이터를 변경할 수 없다
lista = [10,20,30,40,50,60,70,80,90,100]
for a in lista:
    a = 100     # 10을 100, 20을 100...으로 바꿀수 있는가? no
                # 그래서 lista = [] 이런식으로 써서 재구성을 해야 하는 경우가 있다. 
                # ex) lista[5] = 100 으로 우리는 변경했다
                # list의 각각의 요소는 주소값을 가지고 만들어지는데 후에 직접적으로 고치지 않는 한 
                # 주소 값을 모르기때문에 성립이 되지 않는다. 
                # lista[5] = 100이 되는 이유는 직접 lista의 5번째 주소로 직접 들어가 100으로 고치기 때문이다.
indexTemp = 0
for a in lista:
    lista[indexTemp] = 100    # lista[직접변수]를 넣어 고치는 방법을 택해야 한다. 
    indexTemp += 1            # += 1하는 이유는 lista의 범위가 있어야 멈출 수 있기때문이다. 

# 직접 리스트의 index로 접근해야지 원본을 바꿀 수 있다.
for a in range(len(lista)):
    lista[a] = 100
print(lista)

# 리스트를 만드는 방법중에 리스트 컴프리헨션이라는 방법이 있다.
# 리스트에 0~9까지 담는 방법
# 방법1
lista = [0,1,2,3,4,5,6,7,8,9]
# 방법2
lista = list(range(10))
# 방법3
lista = []
for a in range(10):
    lista.append(a)

# 방법3 심화 :홀수인 값에 2를 곱한 값만을 list로 만들어라
lista = []
for a in range(10):
    if a%2 != 0:
        lista.append(a*2) # 홀수인 값을 구했고
print(lista) #올 맞춤 갸꿀  

# 방법4 : 리스트컴프리핸션
# 장점 : 간결하다
lista = [a for a in range(10)] 
# 0~9까지 a꺼내놓는데 맨 앞 a에 다시 쌓는 개념
print(lista)
# 방법4의 곱하기2 
lista = [a*2 for a in range(10)] 
# 하나씩 꺼내다음에 *2 연산 후 lista에 담는 것
print(lista)
# 방법 4의 심화
lista = [a*2 for a in range(10) if a %2 !=0] 
# 하나씩 꺼내다음에 *2 연산 후 lista에 담는 것
print(lista)