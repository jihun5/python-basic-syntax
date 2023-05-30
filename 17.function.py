a = 100
# 특정한 input 값이 있을때, 
# 해당 값을 복잡한 로직을 통해서 연산을 한다고 가정하자.
# 그런데, 해당 연산은 매우 빈번하게 사용이 된다고 가정하자
result = (((a+10)*20) / 10)**2
print(result)

b = 200
result2 = (((b+10)*20) / 10)**2
print(result2)

# 복잡 로직의 연산을 함수화 시켜서 재사용할 수 있게 해보자.
# input 값이 있어도 되고, 없어도된다.
# return 값이 있어도 되고, 없어도된다.
def Myfunc(myinput):
    calc = (((myinput+10)*20) / 10)**2
    return calc
result2 = Myfunc(200)
print(result2)

# 정의된 함수를 호출할때는 함수명(input)의 형태로 호출하게 된다.
result3 = Myfunc(20)
result4 = Myfunc(50)
result5 = Myfunc(77)

def hello():
    print("안녕하세요")
hello() #변수와 리턴이 모두 없어도 됨.

lista = [4,1,23,5,6]
result = lista.sort() # return 없이 lista원본을 바꿈
print(result) # = none인 이유 원본이 바뀌었기 때문

# 함수 직접 구현해보기
# 함수명은 myPlusFunc
# 함수의 로직은 사용자의 input을 받아 input값의 누적합을 더하는 함수
# 예를들어 100을 입력하면 1+2+3+...+100

def myPlusFunc(myinput):
    num = 0
    for a in range(1, myinput+1):
         num += a
    return num
result = myPlusFunc(10)
print(result)

# input 값을 2개를 받아 2값을 더한 뒤 *2만큼 하여 return하는 함수를 만들어보자
# 그리고 해당 함수를 호출하여 호출된 결과값을 result에 담아 출력해보자
def myFunc(x, y):
    result = (x+y)*2
    return result
result = myFunc(2,3)
print(result) 

# list의 index함수를 for문 또는 while문을 통해 
# 숫자 9가 몇번째 인덱스에 있는 값인지
# print 해보자
lista = [1,4,6,9,9]
print(lista.index(9))

for a in range(len(lista)): # lista 5번반복
    if lista[a] == 9:
        print(a)
        break # 9가 중복인경우 첫번째 9가나왔을때 break 없을 시 3,4 출력

# 위의 for문을 활용하여 myindex라는 이름의 함수를 만들고자 한다.
# input(list, 찾고자하는 값)가 2개가 필요하고 print는 함수 내에서 하지 않도록 한다. return에 값을 담는다.
lista = [1,4,6,9]
def myindex(x, y): # x = lista y = 9 
    result = -1
    for a in range(len(x)): 
       if x[a] == y:
            result = a #= lista[9], index값 넣기
            break
    return result
result = myindex(lista, 9)
print(result)

lista = [1,4,6,9]
def myindex(x, y): # x = lista y = 9 
    result = -1
    for a in range(len(x)): 
        if lista[a] == y:
            print(a)
            break

r1 = myindex(lista, 9)  
print(r1)              # 이렇게 출력시 3하고 none값이 출력 return값이 없으면 none값을 출력
# myindex(lista, 9) 로 그냥 입력 후 출력하면  3값이 나온다.    

#20230530###############################################################
# 키보드로 반지름의 길이를 입력받고
# 원의 넓이를 구하는 함수를 만들어 결과를 출력하라
# 원의 넓이 = 반지름 *반지름 *3.14
# num1 = int(input("반지름의 길이를 입력하시오")) 원의 넓이 : 12.56
# result = circleSize(num1)
# num1 = int(input("반지름의 길이를 입력하시오")) #원의 넓이 : 12.56
# result(원의 넓이) = circleSize(num1)
# def circleSize(x):
#     a = x*x*3.14
#     # return a = x*x*3.14 도가능 
# num1 = int(input("반지름의 길이를 입력하시오"))
# result = circleSize(num1)
# print("원의 넓이:" + str(result))

# "hello python!"
# 1) hello() 이렇게만 호출했을 때 "hello1 python" 위 결과 출력
# 2) print(hello2()) 실행했을때 "hello2 python"
def hello():
    print("hello1 python") # 
    
def hello2():
    a = "hello2 python"
    return a
result = hello2()

# print(hello()) none 값, 리턴이 없기때문
hello()
print(result)

# 입력값의 개수가 정해져 있지 않고 multiple한 함수
def sum(*args):
    num = 0
    for a in args:
        num += a
    return num
totalvalue = sum(1,2,3,4,5)
print(totalvalue)

# 2개 이상의 리턴값이 있는 경우 : 튜플형태로 데이터 return
def cal(a, b):
    result1 = a+b
    result2 = a-b
    result3 = a*b
    return result1,result2,result3

calvalue = cal(1,2)
# 계산한 첫번째 결과 값은 xx, 두번째 결과값은yy, 세번쩨결과값은 zz
print(f"계산한 첫번째 결과값은{calvalue[0]}, 두번째 결과값은{calvalue[1]}, 세번째 결과값은{calvalue[2]}")

# 함수에서 default값 미리 세팅하기
def cal(a, b,c):
    
    if c=="plus":
        result = a + b
    elif c == 'minus':
        result = a - b
    elif c == 'multiply':
        result = a*b
    return result
# result = cal(a,b,c) # 마이너스 한 값 
result = cal(a,b,"minus")
print(result)
result = cal(a,b,"plus")
print(result)
result = cal(a,b, "multiply")
print(result)

# 기본 값세팅
def cal(a,b,c ='plus'):
    if c=="plus":
        result = a + b
    elif c == 'minus':
        result = a - b
    elif c == 'multiply':
        result = a*b
    return result
print(cal(1,2)) # 기본 값으로 plus를 가지고 있기때문에 1+2가 출력됨
print(cal(1,2, "minus"))# 다른 조건이 들어오면 조건이 출력됨 1-2가 출력

# 파이썬에서 default값 세팅하는 대표적인 예시가 print함수
print("hello")
print("world")
