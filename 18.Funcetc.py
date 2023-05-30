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
print(cal_dict['plus'(1,2)])

# lambda로 입력한 매개변수가 짝수면 True, 홀수이면 false
def oddTest(x):
    if x %2 == 0:
        return True
    else:
        return False
oddornot = lambda x : True if x % 2 ==0 else Flase



