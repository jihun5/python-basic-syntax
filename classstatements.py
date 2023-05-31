# 클래스의 상속
# 부모 클래스에서의 기능을 자식클래스에서 물려받는것
# class 자식클래스명(부모클래스명) 이런 형식으로 선언
class Calculator:
    def __init__(self):
        self.result = 0
    def plus(self, a):
        self.result += a 
    def minus(self, a):
        self.result -= a
    def multiply(self, a):
        self.result *= a

# Calculator상속 후 divide 매서드 추가, 
# 부모 클래스를 건드리면 관련된 자식함수들 모두 변경 
class CalculatorChild(Calculator):
    def divide(self, a):
        self.result /= a
    # 부모한테 있는 기능을 재선언하게 되면, 부모의 기능보다
    # 자식의 기능이 우선하게 되고, 이를 overriding이라고 한다.
    def multiply(self, a):
        self.result *= (a+1)

# if __name__ == "__main__": 이거를 사용하면 다른 모듈에서 출력이 안되게끔 하는 코드 if를 하고 들여쓰기 
cc1 = CalculatorChild()
cc1.plus(100)
cc1.divide(10)  
# 파이썬에서 overlodding은 안하는 것 같다(다른 매개변수를 가진 매서드를 추가하면 다른 언어에서는 매개변수의 개수에 따라 다른 값을 출력한다.)
cc1.multiply(10) #부모 클래스에서는 *10, 자식클래스에서는 a+1이기때문에 *11
print(cc1.result)
print(cc1)
# lista = [10,20,30] 을 프린트 한경우 왜 주소가 안나오고 값이 나오는가?
# print함수가 속해 있는 클래스는 object클래스 함수를 상속받고 있는데
# list, dict같은 파이썬에서 자주 사용되는 객체값을 value형식으로 출력해주는 함수가 있다.
