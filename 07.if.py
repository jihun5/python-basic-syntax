# if문의 기본 문법
# if 참조건 :
#     실행문
# else:
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
