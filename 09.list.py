# list는 변수마다 값을 할당하여 사용하기 때문에 관리의 어려움이 있으므로
# 한 변수에 값을 집합시켜 놓은 것.

a = "김돌쇠"
b = "김갑쇠"
c = "김돌순"
print(a)
print(b)
print(c)

# 하나의 변수로 여러개의 데이터를 관리
# list의 경우 [] 대괄호를 사용한다.
lista = ["a","b","c","d","e","f","g"]

# list안의 각각의 값에 접근할 때에는 index를 사용
print(lista[0])
print(lista[1])

# 여러개의 데이터의 범위를 지정해서 가져오고 싶을 때는 slicing 사용
# 슬라이싱의 결가 값은 같은 list로 출력
# 0~5번째까지 출력
print(lista[:5])
# 0~5번째까지 출력한 결과물의 type출력
print(type(lista[:5]))

# 문자배열은 메모리 내부적으로 list와 유사한 자료구조
# 문자열은 값을 추가하거나 수정할수가 없다.
# list는 값으 추가, 삭제, 수정이 가능한 구조를 가지고 있다.
# list는 유연함(숫자, 문자, 숫자+문자, 숫자+리스트 등등) lista = [1,2,3,['a','b','c']]

# 연습문제
# list_ex1 = ['a','b','c',[1,2,3]]
# 변수 number에 [1,2,3]을 담아 출력하라
# number에 담은 값중 1과 3을 더해 4를 출력하라

# list안에 list 값을 조회 및 덧셈하는 방법
list_ex1 = ['a','b','c',[1,2,3]]
number = list_ex1[3]
print(number[0]+number[2]) # = print(list_ex1[3][0] + list_ex1[3][2])

# 문자를 리스트화 할때(길이 구하기)
a = "abcdefghi"
listx = list(a)
print(listx)
count = 0
for b in listx:
    count = count +1
print(count)
print(len(a))

# 리스트 더하기 또는 곱하기
# list를 2개 선언하고 만들어서, 2개를 더해서 하나의 리스트를 만들어보자 그리고 출력
listb = [1,2,3,4,5]
listc = [6,7,8,9,10]
print(listb+listc)
print(listb[:]+listc[:])
print(listb*10)
print(list)

# 리스트 길이 구하기 : len
print(len(listb))

# 리스트 값 수정하기 -> 1개의 값만 바꿀 땐 1개의 값으로 대체
# 여러값을 바꿀땐 다른 리스트로 대체

listd = [1,3,5,6,7,9]
listd[1] = 4
print(listd)
listd[2] = [5,5,5]
print(listd)

# list.count값 찾기
liste = ["1","2","3","4","1","1","3"]
print(liste.count("1"))

# list 요소 삭제하기(del) del 리스트명 index, sling
listf = [1,3,5,7,9,10]
del listf[3]
print(listf)
del listf[2:5]
print(listf)

# 리스트 요소 삭제하기(remove) 리스트.remove(삭제하고싶은 요소의 순번)
listf = [1,3,5,7,9,10]
listf.remove(3)
print(listf) # 중복일 경우 앞의 숫자를 삭제

# 모든 특정한 9값을 삭제해보아라 del, for range
# listg = [1,9,4,9,5,7,8,9]
# for a in range(0, len(listg)):
#     if listg[g] == 9:
#         del listg[g]
# print(listg) #오류가 나는 이유 : 
# 지워지면서 index번호가 계속 줄어들어서 범위가 줄어들어서 오류가 발생
# while 문을 사용하여 하는것이 바람직함.
# 만약에 한다면 count 값을 넣어서 표현이 가능
# 방법1
listg = [1,3,3,1,4,2,5,11,1]
count = 0
for i in range(0, len(listg)):
    if listg[i-count] == 1: #인덱스의 범위 내에서 1을 줄인 listg를 소환
        del listg[i-count] #인덱스의 범위 내에서 1을 줄인 listg를 소환해서 listg에서 1을 삭제
        count = count +1 #1을 지우면서 하나씩 줄어드는 
                        # 인덱스의 수를 맞추어 오류를 발생하지 않게함
print(listg)

# 방법2
for a in range(0, len(listg)):
    if 1 in listg:
        listg.remove(1)
    else:
        break
    # listg에 1이 포함되어있다면 1을 삭제하고 
    # 1번부터 8번까지 다시 1이 있는 지 검토하고 1이 있으면 삭제함
print(listg)

# 방법3
listh = []
for a in range(0, len(listg)):
    if listg[a] !=1:
        # listh = listh + lista[g]]
        # 또는 append
        listh = listh + [listg[a]]
        # listh.append(listg[g]) 
        # 새롭게 만들어진 h리스트에 1을 제외한 항목들을 계속 더해가는 것
print(listh)

# list append : 리스트 맨 뒤로 추가
listi = [1,3,5,7]
# 9,10을 append이용해서 추가해서 출력 
listi.append(9)
listi.append(10) #동시에 2개는 안됨
print(listi)
# list insert : index를 지정하여 추가가능
# listi.index(2, "abc") 추가 후 출력 
listi.insert(2, "abc")
print(listi)
# list extend : interable 객체를 list에 추가할때 사용
# extend는 각 요소를 꺼내어 맨 뒤에 추가

listj = [10,20,30]
listi.append(listj) # append는 리스트 형식 그래도 추가
print(listi)
listi.extend(listj) # 리스트를 요소 형식으로 추가
print(listi)
