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