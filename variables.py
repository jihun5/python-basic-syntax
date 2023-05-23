print("hello")

# 이 # 표시는 프로그래밍에서 주석이라 말한다
# 주석은 파이썬의 인터프리터가 인식하지 못하도록 기호
# 단축키는 Ctrl + / 
a = 1 # a는 변수, a와 1이 같다는 의미가 아님.
b = '1'

# print는 실행 후 결과 값을 가시적으로 보여주기 위해 터미널창에 출력하는 것
print(a)
print(b)

# 변수명명규칙
# 변수명을 지을 때는 숫자가 먼저 나와서는 안된다.
# 변수명 중간에 띄어쓰기, 특수기호 등을 일반적으로 쓰지 않는다.
# 특수부호는 일반적으로 사용하지는 않지만 _ 언더바는 빈번히 사용한다.
# 변수 자료형 출력해보기
print(type(a))
print(type(b))

c = 2.1
print(type(c))

# 자료의 형변환
# 숫자 -> 문자, 실수 -> 정수
a = 10
b = 20
# 결과값이 1020이 나오도록 덧셈을 하여라
print(str(a)+str(b))
c = 2333.33333
# c의 소수부분을 잘라서 출력하라
print(int(c))

# 문자자료형
# 문자는 ""쌍따옴표 또는 ''따옴표로 표현을 한다.
# 'a' 문자에 매듭

# 'a'라는 문자를 변수에 저장하게 되면, 메모리상에 어떤 숫자값으로 저장될까?
# 아스키 코드라는 문자와 매칭되는 테이블을 사용하여 약속된 숫자값으로 저장
# 현대에는 아스키코드의 표현범위의 한계로 인해, utf-8을 표준으로 사용
x = 'A' # a = 97(컴퓨터 메모리상), ord = 내장된 함수값
print(ord(x))
y = 'a'
print(ord(y))
a = 'he1ll2oWO1rld' # 숫자로 입력하기, 각각 아스키 코드 대입하여 계산가능

# multi line으로 문자열을 표현하고 싶으면, 쌍따옴표 3개를 사용하거나 홀따옴표 3개를 사용하면 된다. 
a = '''hello

# world'''
# escape문을 활용한 줄바꿈
# 이스케이프문이란 \n 또는 \t 등의 특수기호를 말한다.
# \n : 줄바꿈, \t : tap키
# \의 또 다른 활용 : 특수문자를 있는 그대로 표현하는 역할
# "쌍따옴표(")는 파이썬에서 문자를 의미한다."라는 문구를 출력해보자.
print("쌍따옴표(\")는 파이썬에서 문자를 의미한다.") 
a = "hello \n world"
print(a)

# 그렇다면 python's easy라는 문구를 출력해보자. 
# a = ''python's easy' 중간에 홑따옴표가 인식이되어서 안되는 경우가 있을 수 있어 쌍따옴표를 사용
print("python's easy")

# 문자열 더하기, 곱하기
# a라는 변수에 python이라는 문자열을 담고, b라는 변수에는 is fun이라는 문자열을 담는다.
# 그리고 c라는 변수에 두 문자열을 더한 겂을 넣어 c를 출력
a = 'python '
b = " is fun"
c = a + b
print(c)
# python python is fun이라는 문자열을 c에 담아 출력 
c = a *2 + b
print(c)

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

# 문자열 포맷팅이란 문자열 중간에 특정 문자(또는 숫자 등)를 삽입하는 방식.
# %s : 문자열, %d : 정수, %f : 실수
# 포맷팅을 왜 쓰는가? 
# 1. 문자열을 직접 삽입하면 1회성으로 coding할 수 밖에 없지만 포맷팅을 사용하면 변수값을 삽입할 수 있다.
# 2. 따옴표를 여러번 안써도 된다.
# language = input("좋아하는 언어를 입력하시오:")
# times = input("그 언어를 몇 번이나 공부하셨나요?:")
# a = "I studied %s very hard %d times" % (language, int(times)) # %s자리에 %"a" a를 추가할 것 , 
# 2역시 같은 원리 같이 사용할 경우 앞과 같은 모습 language 입력 가능 %d자리에 역시 마찬가지로 변수 사용가능
# %d 가 숫자형이기 때문에 times 자리에 int를 사용해야 오류가 나지 않음 
# print(a)
# # 아래와 같이 코딩하면 따옴표로 열고 닫고 너무 많이해서 귀찮다.
# a = "I studied " + language + "very hard" + str(times) + "times"
# print(a)

# my age is %d, and weight is %f kg
# 나이가 몇살이신가요?라고 해서 나이를 받고
# 몸무게가 몇 킬로그램 이신가요?라고 해서 weight 받고 
# 위 문자열을 포맷팅을 통해 사용자의 입력값에 따라 달라지도록 만들고 그 결과값을 출력하라
# age = int(input("나이가 몇살이신가요?:"))
# weight = float(input("몸무게가 몇Kg 이신가요?:"))
# result = "my age is %d my 몸무게는? %f" %(age, weight)
# print(result)
# 변수 a에 2022 변수 b에 호랑이를 선언하고 
# 결과 : 올해는 2022년 %s의 해 입니다. %

# 문자열 관련 주요 함수
# count : 대상 문자열에 지정한 문자가 몇개가 있는지 출력하는 함수
# a = "python"
# print(a.count('o'))
# # find : 대상 문자열에서 지정한 문자가 몇 번 index에 있는 지 찾는 함수
# print(a.find('o'))
# print(a.index('o'))

# whatyouwant = input("아무런 문자나 입력해주세요:")
# search = input("찾고자 하는 문자 1개만 입력해 주세요")
# result = whatyouwant.find(search)
# if result == -1:
#     print("찾고자 하는 값이 없습니다.")
# else:
#     print("요청하신 문자는 %d 번째에 있습니다" % result)

# 대소문자 변경 : upper() / lower()
a = "hello"
a1 = a.upper()
print(a1)
b = "HELLO"
print(b.lower())

# 문자열 양쪽 공백을 없애는 함수 : strip()
a = "   hello word   "
print(a.strip())

# myid = (input("id를 입력해주세요")).strip()
# mypw = input("비밀번호를 입력해주세요")
# print("id는 " +myid + " 이고" + "비밀번호는" +mypw)

# 문자열 대체 : replace()
a = "I studied python"
print(a.replace('python', 'java'))

# 문자열 나누기(split)
# 공백을 기준으로 문자를 자르는 함수 : split()
a = "I studied python"
b = a.split() 
print(b)
# 공백을 넣는 것(" " 빈칸하나 공백만큼 자르기 남은 빈칸은 그대로 출력)과 넣지 않는 것(비어있는 값을 버리기)
a = "I   studied   python"
b = a.split(" ")
c = a.split()
print(b)
print(c)

a = "I:studied:python"
b = a.split(":") #원하는 문자열로 자를 수 있다. 
print(b)

# 아래와 같은 2차 방정식을 파이썬 수식어로 코딩하고 y의 결과를 출력하라
# Y = 2.5 X x제곱 + 3.3 X x +6(x는2)
# 출력화면 : 2차 방정식 결과 = 22.6
x = int(input("x값을 입력해주세요:"))
y = 2.5 * pow(x, 2) + 3.3 * x + 6
print(y) 

print("날씨가")