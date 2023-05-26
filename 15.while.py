# while문의 기본구조
# while 조건식 : # 조건식이 참인 경우 => 무한 반복이 기본전제
#     실행문
# a = 10
# while  a>5:
#     print("참입니다.")

# 조건을 체크 후 true 이면 실행문을 1회 실행시키고
# 다시 조건을 체크하고, true이면 다시 실행
# 조건이 false가 되는 순간 while 문 종료
a = 0
while a<5:
    print(str(a)+"번 반복")          # a +=1이 print 위로 가면
    a += 1                          # 반복횟수는 동일하지만 값이 달라질 수 있다.

# # 1~1000까지만 프린트 되도록 출력.
# # 1~1000까지 모두 더한 값을 출력 + 평균값 
sum = 0
a = 0
while a < 1000:
      a += 1  #sum 을 안에다가 넣으면 반복될때마다 sum = n n값으로 초기화
      sum += a
print(sum)  
print(sum/1000)

# # while문에서 반복을 진행하다가 break를 만나면, 반복문 종료.
# # if 문을 써서 n조건하에 break
sum = 0
a = 0
while True:
     a += 1  
     sum += a
     if a == 1000:
         break    
print(sum)  

# continue : 이 구문을 만나면, 다시 반복문 조건으로 이동
# 아래와 같이 코딩하면 hello가 무한 출력이 된다.
# a = 0
# while a<1000:
#     print("hello")
#     continue           #다시 조건문으로, a += 1 무시하기때문에 무한 반복
#     a += 1

# 홀수만 더해서 출력하기
sum = 0
a = 0
while a<1000:
    a += 1
    if a%2 != 0:
        sum += a
print(sum)

# continue 쓰기
sum = 0
a = 0
while a<1000:
    a += 1
    if a%2 == 0:
        continue  # 짝수인 경우 더하지 않고 넘어간다 즉, 위와 같은 식
    sum += a
print(sum)


# while True:
#     num1 = int(input("숫자를 입력해주시오:"))
#     if num1 > 180:
#         continue        #하단에 불필요한 로직을 수행하지 않고 다시 조건으로 이동할 수 있게 해준다
#     if num1 < 90:
#         print("예각")
#     elif num1 == 90:     #if로 쓰는 순간 독립된 형태이기때문에 위에서 true라면 둔각과 예각이 모두 출략되는 현상이 일어남
#         print("직각")
#     elif num1 < 180:
#         print("둔각")
#     else:                # elif num1 == 180: 로 써된다. 
#         print("평행")

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

