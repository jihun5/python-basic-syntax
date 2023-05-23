# 파이썬에서 인덱스란, 기본적으로 특정위치를 가리키는 용도로 사용
# 변수명[인덱스 번호] - 인덱스 번호에 위치한 값을 반환 
# # 인덱스의 사용방법은 원하는 대상[숫자값]
# A = "python is fun" print(a[0]) >> p
# 프로그래밍에서는 대부분의 순서는 0부터 시작(0,1,2,3...의 순서, 공백포함)
# 문자 h를 출력하라
a = "python's fun"
print(a[3])
# 문자열의 마지막 문자를 출력해보자.
a = "python's fun python's fun python's fun"
print(a[-1])
# 문자열의 길이를 구하는 함수는 len
print(len(a))
print(a[len(a)-1])

# 문자열의 슬라이싱
# 슬라이싱이란 문자열을 잘라내는 것을 의미
# 대상변수[x:y] : x이상 y 미만의 index를 가진 문자열을 잘라낸다.
a = "python is fun"
# python만 잘라내기
b = a[0:6]
print(b)
# x, y 자리에 값이 없으면 처음부터 끝까지를 의미
# 6번째 문자부터 끝까지 잘라내서 변수 b에 담아 출력 
b = a[6:]
print(b)
# a[x:y:z] 여기에서 z는 z-1 개씩 건너뛰고
# 2번째 이상 7번째 미만 문자열 중에 1개씩 건너뛰고 b에 담아 출력
b = a[2:7:2]
print(b)
# 처음부터끝까지 3개씩 뛰고
print(a[::3])
# 연습문제 A = '20220505children's_day' 슬라이싱을 이용하여 date 라는 변수에 날짜
# day라는 날에 children's_day를 각각 출력하시오
A = '20220505children\'s_day'
date = A[:8]
day = A[8:]
print(date)
print(day)

# 연습문제 3개의 단어를 입력받아 첫글자 추출후 약자를 추출
#  조건 1> 각 단여의 변수 word1 ...3
#  조건 2> 입력과 출력 구분선: 문자열 연산
#  조건 3> 각변수의 첫 단어만 추출하여 변수 저장(index)

# 출력화면 에씨
# 첫번째 단어 : korea
# 두번째 단어 : Baseball
# 세번째 단어 : orag
# ======================
# 약자 : KBO

word1 = input("첫번째 단어 :")
word2 = input("두번째 단어 :")
word3 = input("세번째 단어 :")
print("="*20)
result = print("약자:", word1[0]+word2[0]+word3[0])
print("="*20) 