# 람다함수 : 1)함수를 간편하게 표현하기 위한 방식
#           2) 함수를 변수에 담기 위한 방식
# lambda 매개변수: 실행문
def add(a,b):
    return a+b
print(add(1,2))

add_lambda = lambda a, b : a+b
print(add_lambda(1,2))

# 매개변수 a를 입력했을 때, a의 제곱이 출력되는 lambda함수 생성
m_lambda = lambda a : a**2
print(m_lambda(3))

add = lambda a, b : a+b
minus = lambda a, b : a-b
multiply = lambda a, b : a*b
# list에 람다 함수를 담아서 사용가능
cal_list = [lambda a, b : a+b, lambda a, b : a-b, lambda a, b : a*b]
print(cal_list[0](1,2))
cal_dict ={"plus": lambda a, b : a+b, "minus":lambda a, b : a-b, 
            "multiply": lambda a, b : a*b}
print(cal_dict['plus'](1,2))

# lambda로 입력한 매개변수가 짝수면 True, 홀수이면 false
def oddTest(x):
    if x %2 == 0:
        return True
    else:
        return False
oddornot = lambda x : True if x % 2 ==0 else Flase

# map함수 : 특정함수와 반복가능한 자료형을 입력받아 
# 특정 함수가 수행한 결과 값을 return
# 사용예시 : map(함수, 리스트(또는 튜플 등등))

def two_times(x):
    return x*2
map(two_times, [1,2,3,4])
print(map(two_times, [1,2,3,4])) # 객체여서 주소 값이 나온다
lst = list(map(two_times, [1,2,3,4]))
print(lst)

# map 함수와 lambda함수를 사용하여 
# 입력한 list의 제곱값을 담은 list를 출력하도록하자
m_lambda = lambda a : a**2
lis1 = list(map(lambda a : a**2, [1,2,3,4]))
print(lis1)

# map의 역할은 대상이되는 리스트를 가지고, 
# 함수를 적용하여 새로운리스트를 만들어내는 것
# filter의 역할은 대상이 되는 리스트에서 
# 함수를 적용하여 침/거짓 조건으로 값을 걸러내는 것
# filter 함수 안에 매개변수가 참이면 선택하고, 거짓이면 걸러내는 것

def trueOrNot(x):
    if x > 0:
        return True
    else:
        return False
lst = list(filter(trueOrNot, [-1,0,3,-2,5]))
print(lst)

# 위 로직을 lambda를 써서 바꿔보자(삼항연산자)
# a = 10
# print('A는 10보다 큽니다') if a > 10  else  print('A는 10보다 작습니다')

lst = list(filter(lambda a : True if a > 0 else False, [-1,0,3,-2,5])) 
# filter 대신에 map을 사용하면 true, false, true, false 형식으로 나옴
print(lst)

# 함수형 프로그래밍(map, lambda, filter)을 
# 사용하여 주어진 리스트에서 홀수만 추출하도록 하여라.
lista = [4,7,1,2,5,6,8]
lst = list(filter(lambda a : True if a%2 != 0 else False, lista))
print(lst)

# sum : 주어진 자료들의 총합
print(sum([1,2,3]))
sum_value = sum(filter(lambda a : True if a%2 != 0 else False, lista))
print(sum_value)

# 문자를 아스키코드 변환 : ord()
print(ord("a"))
# 숫자 107이 의미하는 아스키코드상의 문자는 뭘까? : chr()
print(chr(107))
# 예를 들어 문자열이 주어질때 숫자를 제외하고 문자값만 새로운 문자열로 만들어 보아라
str1 = "123asdf512kjlk"
print(ord("z")) #소문자 a~z : 97~122
print(ord('Z')) #대문자 A~Z : 65~90
new_str = ""
for a in str1:
    if (122> ord(a) >= 97) or (65>= ord(a) >= 90):
            new_str += a
print(new_str)

# 절대값 구하기 : abs()
print(abs(-3))
# 주어진 리스트에 절대값으로 변환한 리스트를 출력해보자
# map을 사용해서
lista = [1,-5,12,-5]
def abss(x):
    return abs(x)
lst = list(map(abss, lista))
print(lst)
print(list(map(abs,lista)))

# 재귀함수
# factorial 예제
# 변수 n을 넣었을 때 n!가 나오도록 함수를 만들어보자.

def factorial(n):
    total = 1
    for a in range(1, n+1):
        total *= a
    return total
result = factorial(4)
print(result)

# 재귀함수를 통한 factorial 예제 굉장히 어려운 함수
# 재귀함수란 함수내에서 함수자기자신을 호출하는 함수.
# def test(n):
#     return n+test(n) # 10+test(10)을 계속반복
# result = test(10)
# print(result)

# def test(n):
#     return n+test(n-1) # 10+test(9)
#                        # 10+test(8)
#                        # 10+test(7) -까지 무한반복
# result = test(10)

# 재귀함수에서는 반드시 재귀함수를 종료시키는 조건이 들어가야 한다.
# def test(n):
#     if n == 1:
#         return 1
#     return n+test(n-1) 
# result = test(10)
# print(result)
# # 10 + 9 + 8....1 = 55 조건 n==1 이 있기때문에 1에서 더이상 리턴하지 않는다.

# 펙토리얼 재귀함수 구하기
# def test(n):
#     if n == 1:
#         return 1
#     return n*test(n-1) 
# result = test(5)
# print(result)

# # 재귀함수를 반드시 써야만 하는 상황
# # 반복의 횟수를 알수 없을 때

# lista = [10,20,30,40,50]
# 다섯개의 숫자중에 2개씩 숫자를 추출하는
# 경우의 수를 구하고자 한다
# 2개씩 숫자를 추출하여 list에 담아 마지막 모든 리스트를 출력하도록 하라 =>10개
# [[10,20],[20,10],[10,40]....] append
# lista = [10,20,30,40,50]
# result = []
# def test1(n):
#     for a in range(len(lista)):
#         result.append(lista)
#     if n == 10:
#         return result
# result = test1(10)
# print(result)

# lista = [10,20,30,40,50]
# new_list = []
# count = 0
# for a in range(len(lista)):
#     for b in range(a+1, len(lista)):
#         count += 1 
#         new_list.append([lista[a], lista[b]])
# print(count)

lista = [10,20,30,40,50]
new_list = []
# def mysort():
for a in range(len(lista)):
    for b in range(a+1, len(lista)): 
        new_list.append([lista[a], lista[b]])
print(new_list)
