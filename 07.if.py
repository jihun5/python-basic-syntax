a = 10
if (a>5) | (a>100) : #소괄호를 묶어줘야 |실행
                     # a >5 | a > 100 의 오류 5 | a를 묶어서 
                     # 계산 5를 2진법으로 계산하여 101이라면 마지막이 1이라 참 
                     # 1100이라면 0이라서 거짓이고 print()값이 나오지 않음 
     print("참입니다")
if a > 5 or a > 100:
     print("참입니다")
# if not (a > 5 or a > 100): not (true) = 결과적으로 false

# 비트 연산이란 2진법의 숫자를 or, and, xor 등으로 
# cpu 내부적으로 계산하는 방식
# ex)
# 1111 and 1000 => 1000 0은 거짓 이여서 1000이 출력
# 1111 or 1000 => 1111 1은 참이니까 마지막1이 참이라 1111출력

# and = &, or = | 와 같고, not은 부정의 의미,  
# not (true) = 결과적으로 false, not (false) = True

print(10 or 1) # = 10 0을 제외한숫자는 True, 비트연산이 아닌 단순 True, false
print(10 | 1)  # = 11 비트연산을해서 10또는 1 11 10과1 11

# 대입연산자
a = 10 
# a = a+1 이렇게 표현해도 되고, a += 1 이렇게 표현해도된다
a += 1  # = a+1
print(a)
# -=, /=, *=
a/=5 #=>  a/5 
a*=3 #=>  a*3
print(a)

# 비교연산자 중에 chaining(범위로 표현할 수 있다.)
a = 10 
if a > 5 and 100 < a: # 5 < a < 100
     print("참입니다")

# if문의 기본 문법
# if 참조건 :   
#     실행문   if가 참이면 실행
# else:        if가아니면 실행
#     실행문
a = int(input("숫자를 입력하시오:"))
if a > 10:
     print("a는 10보다 큽니다.")
else: # if문이 거짓일 경우 else 실행
     print("a는 10보다 작습니다.")
print("a는 10보다 큽니다.") # 이 문은 독립적으로 사용(if, else 문에 걸리지 않음, 들여쓰기 X)

a = int(input("숫자를 입력하시오:"))
if a > 10:
     print("a는 10보다 큽니다.")
     if a<100:
         print("a는 100보다 작습니다.") # if 아래에 if 두가지 다 참인 경우 두 가지다 실행

while True:
    print("무한 반복 됩니다")

trueOrFalse = True
if trueOrFalse:
     print("참입니다")
else:
     print("거짓입니다")

# <, >, <=, >=, ==(같음), !=(좌항 우항이 다르면 참), and, or, not(true ->false)
# 얼마를 가지고 있습니까?를 변수에 담고 만약 3만원 이상이 있으면 
# 택시를 타러 가시오를 출력, 그렇지 않으면 걸어가시오를 출력.
a = int(input("얼마를 가지고 있습니까?"))
if a >= 30000:
    print("택시를 타고 가시오")
else:
    print("걸어가시오") # else 는 생략이 가능
