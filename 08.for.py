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

# # range 문법
# for a in range(1, 101): # a, a-1의 범위 1부터 100까지는 1, 101
#     print(a, end=' ')

# # listb = ["a","b","c","d"]
# # for b in range(0, len(listb)):
# #     print(listb[b]) 파이썬 외에 언어 기본문법
