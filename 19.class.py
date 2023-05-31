# 클래스의 사용
# 1)같은 기능의 함수의 집합
# 2)객체를 만들기 위해 사용
# 3)객체를 정의해 놓은것
# 4)반복하여 사용하는 변수 & 함수를 미리 정해 놓은 틀
# 하나의 class로 여러 객체를 관리하기 위해 사용

# 사칙연산 함수가 있을 때, 같은 기능을 하므로,
# calculator라는 클래스에 모아둘 수 있다.
# 명명규칙 : 일반적으로 클래스는 대문자 알파벳으로 시작
# 변수명, 함수명은 소문자로 시작 -> camalcase ex)myImportanat, myList, 특정 중요단어에서 대문자를 사용 또는 _사용
# 함수의 집합으로서의 클래스 -> 일반적이지 않은 형태
# class Calculator:
#     def plus(a, b):
#         return a+b
#     def minus(a, b):
#         return a-b
#     def multiply(a, b):
#         return a*b
#     def divide(a, b):
#         return a/b
# print(Calculator.plus(10,20))
# 위 클래스의 문제점은 클래스 내에서 누적된 값을 변수로 갖고 있지 않다
# 방법 1 클래스.변수를 쓰면 클래스 변수에 접근가능
class Calculator:
    result = 0
    def plus(a):
        Calculator.result += a 
    def minus(a):
        Calculator.result -= a
    def multiply(a):
        Calculator.result *= a
    def divide(a):
        Calculator.result /= a        
Calculator.plus(10)
print(Calculator.result)
Calculator.minus(5)
print(Calculator.result)

# 방법 2 classmethod 데코레이터 사용
# class내에 선언된 함수는 매서드라고 부른다.
# class Calculator:
#     result = 0
#     @classmethod
#     def plus(cls, a):
#         cls.result += a # 위의 방법 1의 형태와 같음 
#     def minus(cls,a):
#         cls.result -= a
#     def multiply(a):
#         cls.result *= a
#     def divide(a):
#         cls.result /= a        
# Calculator.plus(10)
# print(Calculator.plus(10))
# Calculator.minus(5)
# print(Calculator.minus(5))

# 객체는 class의 복제본이며 인스턴스라 부르기도 한다. 
# 객체의 사용이유
# 클래스의 중복제거 : 변수와 함수의 재활용의 어려움해결
# 객체 형식의 클래스의 기본구조
class Calculator:
    # 객체가 생성될때 init(생성자)은 가장 먼저 실행된다. 사용자가 class로 매개 변수를 만들때 만들자마자 실행하게 하는 함수
    # 생성자는 객체생성될때 객체변수를 초기화.
    def __init__(self): # init(생성자)는 없어도 되지만 자동으로 실행, 초기세팅을 도와주기 위해 값을 지정할 수 있다.
        self.result=0 # 객체를 만들 때 매서드내의 첫번째 매개변수는 객체를 의미한다, self.result = 100, 최초값을 100으로 세팅
    def plus(self, a): # self는 관용적으로 사용하며(이름바꿔도됨), 객체 생성 시 그 객체를 대체하기 위한 자리
        self.result += a # list역시 객체를 생성한다. self 자리에 lista = []가 들어가도 무방하다 
    def minus(self,a):
        self.result -= a
    def multiply(self,a):
        self.result *= a
    def divide(self,a):
        self.result /= a
        #return이 필요없는 이유는 객체가 저장되는 메모리가 비휘발성이다
        #지역변수의 경우 휘발성 메모리에 저장되기 때문에 return값이 필요하다.    
aCompany = Calculator() # 객체는 aCompany self 자리에 aCompany
aCompany.plus(100)
bCompany = Calculator() # 객체는 bCompany self 자리에 bCompany
bCompany.plus(100)
print(aCompany.result)
# print(aCompany.plus(100)) # return self.result 입력 시 객체 aCompany = 100
# print(aCompany.plus(100)) #객체 aCompany = 200
# print(bCompany.plus(100)) #객체 aCompany = 300
lista = Calculator()
lista.plus(10)
print(lista.result)
