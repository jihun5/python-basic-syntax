# 문자열 포맷팅이란 문자열 중간에 특정 문자(또는 숫자 등)를 삽입하는 방식. *****
# %s : 문자열, %d : 정수, %f : 실수
# 포맷팅을 왜 쓰는가? 
# 1. 문자열을 직접 삽입하면 1회성으로 coding할 수 밖에 없지만 포맷팅을 사용하면 변수값을 삽입할 수 있다.
# 2. 따옴표를 여러번 안써도 된다.
language = input("좋아하는 언어를 입력하시오:")
times = input("그 언어를 몇 번이나 공부하셨나요?:")
a = "I studied %s very hard %d times" % (language, int(times)) # %s자리에 %"a" a를 추가할 것 , 
# # 2역시 같은 원리 같이 사용할 경우 앞과 같은 모습 language 입력 가능 %d자리에 역시 마찬가지로 변수 사용가능
# # %d 가 숫자형이기 때문에 times 자리에 int를 사용해야 오류가 나지 않음 
print(a)
# # # 아래와 같이 코딩하면 따옴표로 열고 닫고 너무 많이해서 귀찮다.
# a = "I studied " + language + "very hard" + str(times) + "times"
print(a)

# # my age is %d, and weight is %f kg
# # 나이가 몇살이신가요?라고 해서 나이를 받고
# # 몸무게가 몇 킬로그램 이신가요?라고 해서 weight 받고 
# # 위 문자열을 포맷팅을 통해 사용자의 입력값에 따라 달라지도록 만들고 그 결과값을 출력하라
age = int(input("나이가 몇살이신가요?:"))
weight = float(input("몸무게가 몇Kg 이신가요?:"))
result = "my age is %d my 몸무게는? %f" %(age, weight)
print(result)

# # 변수 a에 2022 변수 b에 호랑이를 선언하고 
# # 결과 : 올해는 2022년 %s의 해 입니다. %
# print(language)

