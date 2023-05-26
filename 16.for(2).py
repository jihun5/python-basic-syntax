# while은 무한 for문은 범위 

# 나만의 리스트 만들기
# 리스트의 크기를 입력받아 그 크기 만큼 임의 숫자를 리스트에 추가하고
# 리스트의 크기와 값 전체를 출력하라
# 모든값은 키보드로 입력받고, list의 크기는 함수를 통해 구하라
# 단, 리스트의 크기는 10 이하로 입력하라

# 출력화면 (while)
# 리스트의 크기를 정하세요!30
# 리스트의 크기를 10이하로 다시 할당하세요! 9
# 리스트에 값을 할당해보세요! 1
# 리스트에 값을 할당해보세요! 2
# ..................
# 크기9의 리스트['1''2''3''4''5''6''7''8''9']

# sum = 0
# a = 0
# while a < 1000:
#       a += 1  #sum 을 안에다가 넣으면 반복될때마다 sum = n n값으로 초기화
#       sum += a


# 내가 한거 무엇이 잘 못되었나 비교 하기
# lista = [] # 빈리스트정의
# a = int(input("리스트의 크기를 정하세요!")) 
# while a > 30:
#     print("리스트의 크기를 10이하로 다시 설정해주세요") #
#     break
#     #다시 반복문이 실행되지 않게 만들기
#     if a > 0:
#         a += 1
#         lista += lista.append(a)
# print(lista)

# 1.사용자한테 리스트크기를 입력(3)
# 2. 리스트 크기 만큼 값을 입력받는 것.(3번반복)
while True:
    listSize = int(input("리스트의 크기를 입력해주세요"))
    if listSize>10:
        print("다시 입력해주세요")
        continue
    a = 0
    lista = []
    while a < listSize:
        listvalues = int(input("리스트의 값을 입력해주세요"))
        lista.append(listvalues)
        a += 1
    print(lista)
