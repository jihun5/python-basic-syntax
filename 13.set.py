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
a = set(lista)
print(a)
print(len(a))
