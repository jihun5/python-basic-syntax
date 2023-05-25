# set은 집합이라고 부르기도 한다.
# set의 특성은 딕셔너리와 마찬가지로, index가 없고, 중복이 없다.
# 추가, 수정, 삭제 가능
s1 = {'이름', '나이','성별'}
l1 = '이름', '나이','성별'
s1 = set(['이름', '나이','성별']) #형변환       list를 set으로
# 집합의 개수 구하는 함수는 len 
# print(len(s1)) = 3

# list의 중복을 제거하기 위해서
# list를 가지고 set으로 형변환 시키는 방식도 많이 사용
s1 = set(['이름','이름', '나이','성별'])
print(s1)
s2 = set('test') # = set(list('test'))
print(s2)

# index로 접근은 불가
# print(s1[0]) # 오류
lista = ['A','A','A','B','B','AB','O']
# 이 반 학생들의 혈액형 종류는 총 몇개인가?
# A, B, AB -> 3개
setA = set(lista)
print(len(setA))

# setA의 값을 하나씩 출력하려면 ? setA[0], setA[1] X
for a in setA:
    print(a) # for 문으로 출력가능
# set안에 리스트가 주어지는 경우가 많다.

# 합집합
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8])
s3 = s1.union(s2) # s3 = s1 | s2 # | : 또는 or을 의미(백스페이스 옆에 키 + shift)
print(s3)

# 프로그래밍에서 &(shift+7)은 일반적으로 and(엠퍼샌드)를 의미
s3 = s1 & s2 # = s3 = s1.intersection(s2)
print(s3)

#차집합 
# s2-s1, = s2.difference(s1)

# 집합에서 값 추가 : add
s1 = {1,2,3,4,5,6}
# 7을 추가
s1.add(7)
print(s1)

# 값 여러개 추가시 update함수(딕셔너리와 동일)
# s1
# s2
# s1에 s2를 update
# s1출력

s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,8,9}
s1.update(s2) # s3 = 하지 않는 이유는 s1자체가 바뀌기 떄문에 s3는 none이라고 나옴
print(s1)

# set값 삭제시 remove, discard 함수 활용
# discard : remove와의 차이점은 삭제할 값이 존재하지 않아도 에러가 발생하지 않는다는 점.
s1 = {1,2,3,4,5,6}
s1.remove(6)
s1.discard(5)
print(s1)

# boolean(불형)타입
# ex) a in lista, a not in lista, a in dicta.key(), a in seta
# in, not in : in(또는 not in(없어야 참)) 뒤에 iterable한 자료형이 나오고

# 비어있는 값들은 거짓, 값이 들어있으면 참
# while 조건 : #조건이 참인 한 무한 반복
#     실행문
# for 변수 in 리스트: #리스트의 개수 만큼 반복
#     실행문
lista = [1,2,3]
while lista:
    print('참입니다.') #무한반복
    lista.pop() # 반복할때마다 하나씩 삭제
# 3, 2, 1 삭제후 값이 비어질때까지 삭제하기 떄문에 while문 이 멈춤
# 0은 거짓, 1은 참

