# dic1['신분'] = '학생' 딕셔너리[] = "" or 숫자
# print(dic1)
# dic1.keys() 딕셔너리.keys() = 키값만 뽑아내기
# for k in dic1.keys(): dic1 의 키값만 k에 넣기  
#         print(k)      #print k 는 키값만
#         print(dic1[k]) # 딕셔너리[k] = 키안에 있는 values 값만 추출 딕셔너리[for 문의 변수]
# 삭제 del 변수명 [key]
# 방법 1
# dicta = {} # 딕셔너리 빈칸으로 만들기
# for a in lista: # 딕셔너리 lista를 만들어서 변수 a에 담기 
#     if a not in dicta.keys(): # dicta의 키값이 a에 포함되지 않으면
#         dicta[a] = 1 # A:1    # dicat 키값a:1을 추가할것(키:values) 추가 
#     else:
#         dicta[a] = dicta[a] + 1 # dicta의 키값에 a가 포함되어 있다면 a : 1 +1 = a:2가되는 것 
# print(dicta) - 새롭게 쓰여진 딕셔너리 dicta

# 최대값 구하기
lista = [100, 20, 30, 5, 90]
# 위 리스트의 최대값을 정렬함X(sort), 최대값함수X, for문 쓰기 min, max는 예약 코드이기때문에 이것만 쓰면 안됨
# 방법1
maxA = 0 # max = lista[0] -> 값이 음수일 경우 최대 값은 0으로 고정될 수도 있기때문에 lista 값을 하나 가져와서 비교할 수 있다.
minA = lista[0]
for a in lista: # 100, 20, 30, 5, 90 출력
    if maxA < a: # 100, 20, 30, 5, 90 출력 > if max가 a
        maxA = a
    elif minA > a: # 최소값을 lista[0]번째 부터 찾는다는 가정 
                   # else를 쓰지 않는건 최대값을 구하고 끝나기때문에 else minA가 90이 출력될 가능성이있다.
        minA = a   # 만약 min = 0으로 두고 하면 5>0보다 크니까 출력값은 0이나온다.
print(minA)        # 따라서 최대값, 최솟값을 구할 때는 정해진 list 값의 첫번째를 설정하고
                  # for문에서 lista전체와 비교하여 구하는 것이 바람직하다

# 방법2 max() min()
maxA = max(lista)
minA = min(lista)

# 방법3 sort()
lista.sort()
minA = lista[0] # 최소값
maxA = lista[-1] # 최대값
print(len(lista)) # lista의 오름차순 정리하여 길이를 구하면 맨 마지막 숫자가 가장 높은 수
lista[4] # 5개가 나왔기 때문에 0 1 2 3 4, 4가 가장 높은수 = len(lista)-1
print(lista[4])

# 내림차순 정렬찾기
listb = []
for a in range(len(lista)):
    listb.append(list[len(lista)-a-1])
print(listb)

a = 10
if a >5:
    print("참입니다.")
if a >100:
    print("참입니다.") #위의 if와 상관없이 독립적으로 존재
else:
    print("거짓입니다.") 
# 실행이되는 이유는 바로위에 if가 거짓이기 때문 맨위에 if와는 상관이없음 elif를 쓰는경우 else는 영향을 받음
# else 상단에 있는 if 또는 elif에 종속된다.
# elif도 마찬가지로 elif상단에 if에 종속된다.
