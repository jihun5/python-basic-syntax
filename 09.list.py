# list는 변수마다 값을 할당하여 사용하기 때문에 관리의 어려움이 있으므로
# 한 변수에 값을 집합시켜 놓은 것.

a = "김돌쇠"
b = "김갑쇠"
c = "김돌순"
print(a)
print(b)
print(c)

# 하나의 변수로 여러개의 데이터를 관리
# list의 경우 [] 대괄호를 사용한다.
lista = ["a","b","c","d","e","f","g"]

# list안의 각각의 값에 접근할 때에는 index를 사용
print(lista[0])
print(lista[1])

# 여러개의 데이터의 범위를 지정해서 가져오고 싶을 때는 slicing 사용
# 슬라이싱의 결가 값은 같은 list로 출력
# 0~5번째까지 출력
print(lista[:5])
# 0~5번째까지 출력한 결과물의 type출력
print(type(lista[:5]))

# 문자배열은 메모리 내부적으로 list와 유사한 자료구조
# 문자열은 값을 추가하거나 수정할수가 없다.
# list는 값으 추가, 삭제, 수정이 가능한 구조를 가지고 있다.
# list는 유연함(숫자, 문자, 숫자+문자, 숫자+리스트 등등) lista = [1,2,3,['a','b','c']]

# 연습문제
# list_ex1 = ['a','b','c',[1,2,3]]
# 변수 number에 [1,2,3]을 담아 출력하라
# number에 담은 값중 1과 3을 더해 4를 출력하라

# list안에 list 값을 조회 및 덧셈하는 방법
list_ex1 = ['a','b','c',[1,2,3]]
number = list_ex1[3]
print(number[0]+number[2]) # = print(list_ex1[3][0] + list_ex1[3][2])
