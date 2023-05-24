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
