# while문 패턴(가장기본적인)
# a= 0
# while a<n:
#     실행문
#     a+=1

# a = 0
# while True:
#     if a ==10:
#         break
#     a +=1    

# 1반에 수학 점수가 60점이 넘으면 합격
# 60점 미만이면 불합격
# lista 학생의 번호순서대로 있을 때, 아래와 같이 출력하도록 코딩하여라 
lista = [90,25,67,45,80]
# 출력화면예시
# 1번학생은 합격입니다. n번 학생
# 2학생은 불합격입니다.
num = 1 # 1번째 학생부터이기 때문
for a in lista:
    if a > 60:
        print(f"{num} 번째 학생은 합격입니다")
    else:
        print(f"{num} 번째 학생은 불합격입니다.")
    num += 1
# 방법2
for a in range(len(lista)):
    if lista[a] > 60:
        print(f"{a+1} 번째 학생은 합격입니다")
    else:
        print(f"{a+1} 번째 학생은 불합격입니다.")
    # num += 1



# for문과 break : for문에서 break문을 반드시써야 하는 상황 
# 혈액형이 a형인 고객 선착순 1명만 찾는 상황.
lista = ["b","b","ab","a","b","a"]
# 출력결과 : n번째 고객이 이벤트에 당첨되었다. 4번째 고객이 당첨이 되었다.
# 내가한거 
# num = 0
# for a in lista: # a b ab a b a = lista[0] ~ lista[5]까지 인디 lista[4]
#     if a == "a":
#         print(f"{num}번째 고객이 이벤트에 당첨이 되었다.")
#         break

for a in range(len(lista)): # 순서를 나타낸거
    if lista[a] == "a": # a가 숫자이기때문에 index가 가능하지만 내가 한경우 a는 "a", "b" 등 index에 문자가 들어가서 출력이 안됐다.
        print(f"{a+1}번째 고객이 이벤트에 당첨")
        break

# for문을 이용한 구구단
# 5단 결과 출력 : 5 X 1 = 5 
#                5 X 2 = 10
b = 5
for a in range(1, 10):
    print(f"{b} x {a} = {b*a}")

# # 구구단 몇단을 계산해 드릴까요?  ###########이따 돌려놓기
# b = int(input("몇 단을 계산해드릴까요?:"))
# while True:
#     for a in range(1, 10):
#         print(f"{b} x {a} = {b*a}")
#     break

# 2중 for문
# 구구단을 5~9단까지 한꺼번에 출력
# 출력화면
# 5x1 = 5
# ...
# 9X9 = 81
# b = 5 # 5에서 9까지의 값 b를 먼저 정의
for b in range(5, 10):
    for a in range(1, 10):
        print(f"{b} x {a} = {b*a}")
b = 5
while b < 10:
    for a in range(1, 10):
        print(f"{b} x {a} = {b*a}")
    b += 1

lista = [10,20,30,40]
# lista[0]와 lista[1]번째의 자리를 바꾸려면?
#  lista = [20,10,30,40]
# listb = []
# listb = [lista[1], lista[0], lista[2], lista[3]]
# print(listb)

lista[0] = lista[1]
lista[1] = lista[0] # 바뀐 상태로 다시 바꾸니까 다시 20, 20, 30, 40이 된다.

temp = lista[0] # 10
lista[0] = lista[1] # 10을 20으로 교체
lista[1] = temp # 20은 10으로 교체

# 파이썬에서 지원하고 있는 문법
lista[0], lista[1] = lista[1], lista[0]

# for문을 이용한 정렬 알고리즘
lista = [93,45,21,30,20,94,66,71,45]
# 위 리스트를 어떻게 오름 차순 할 것인가?
# 컴퓨터의 경우 값을 직접적으로 비교할 수 없고 주소로 할당받기때문에
# 0번값과 1...2..3...4를 비교하고 작은수 n를 출력하는 것
# 작은수가 0번째에 고정된 후 순서의 알고리즘
# 다시 1번째부터 2...3...4번째 자리를 비교 n(고정),1..2..3..4... 1이 2..3...4와 다시 비교
# lista.sort()
# print(lista) # print(lista.sort()) 는틀림 왜 lista값이 이미 오름차순되어서 변경되었기 때문에 또 sort할필요가 없다.
# for문의 1번의 사용은 lista값 전체를 1번씩 꺼내온다.
# lista 0번째 자리를 구하기 위해 -8번비교, 7번비교(0과1고정), 6번비교(0,1,2고정)

# 선택정렬 : 0번째 index부터 가장 작은 값을 채워나가는 방식
lista = [93,45,21,30,20,94,66,71,45]
# min = lista[0]
# listb = []
# temp = lista[0]
# for a in lista: # 어려움 직접적인 숫자, 원본을 바꿀수가 없다
#     if a > min:
#         min = lista[0]
#         for b in lista:
#             if b > min:
#                 min = lista[0]
#                 print(min)
# 첫번째 for문은 채워나가야할 index를 의미
for a in range(len(lista)-1): # 인덱스 값에 접근하기 위해 len를 사용 0~8까지 a는 0~8까지 각자 자리를 의미, 
                              # -1을 하는 이유는 7번째가 완성이 되는순간 8번째랑 비교할 필요가 없어서
        for b in range(a+1, len(lista)): # 비교의 대상이 되는 index를 의미, len(listb)는 똑같이 계속 8변을 반복 
                                        # 범위를 a번째에서 lista로 설정해야 하나씩 줄여 나갈 수 있다. 
                                        # a+1을 하는 이유는 자기 자신과 비교할 경우를 제외하기 위해
            if lista[a] > lista[b]: 
                # 자리 체인지
                # lista[a], list[b] = lista[b], lista[a]
                temp = lista[a]
                lista[a] = lista[b]
                lista[b] = temp
print(lista)

# 위에꺼 깔금하게 코드만 나오게 하기
# for a in range(len(lista)-1):  
#            for b in range(a+1, len(lista)): 
#             if lista[a] > lista[b]: 
#                 temp = lista[a]
#                 lista[a] = lista[b]
#                 lista[b] = temp
# print(lista)

# 버블정렬

# 2차원 행렬
lista = [[1,2,3], [2,3,4]]
print(len(lista)) # 전체가 2개 
print(len(lista[0])) # 각각의 요소가 3개

# 
ansnwer = []
arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]
# answer = [[4,6],[7,9]]
# arr1[0][0] + arr2[0][0], arr1[0][1]+arr[0][1], arr1[1][0] + arr2[1][0], arr1[1][1] + arr2[1][1]
for a in range(len(arr1)): # 전체 리스트의 길이 0~1, 2개의 요소
    temp = [] 
    for b in range(len(arr1[0])): # 그 리스트 안에 길이 1,2, 2개의 요소
        temp.append(arr1[a][b]+arr2[a][b]) # temp = 4,6 0번째의 0번째 더하기(4), 0번쨰의 1번째 더하기(6)
                                           # arr1의 1번에 1번째요소 + arr2의 1번쨰 1번째요소 더하기 = [7]
                                           # arr1의 1번쩨 2번째요소 + arr2의 1번째 2번쨰 요소 더하기 = [9]
    ansnwer.append(temp)
print(ansnwer)