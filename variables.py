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

# 문자열 관련 주요 함수 ****
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
# a = "I studied python"
# b = a.split() 
# print(b)
# # 공백을 넣는 것(" " 빈칸하나 공백만큼 자르기 남은 빈칸은 그대로 출력)과 넣지 않는 것(비어있는 값을 버리기)
# a = "I   studied   python"
# b = a.split(" ")
# c = a.split()
# print(b)
# print(c)

# a = "I:studied:python"
# b = a.split(":") #원하는 문자열로 자를 수 있다. 
# print(b)

# # 아래와 같은 2차 방정식을 파이썬 수식어로 코딩하고 y의 결과를 출력하라
# # Y = 2.5 X x제곱 + 3.3 X x +6(x는2)
# # 출력화면 : 2차 방정식 결과 = 22.6
# x = int(input("x값을 입력해주세요:"))
# y = 2.5 * pow(x, 2) + 3.3 * x + 6
# print(y) 

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
