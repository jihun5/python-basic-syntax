# while문의 기본구조
# while 조건식 : # 조건식이 참인 경우 => 무한 반복이 기본전제
#     실행문
# a = 10
# while  a>5:
#     print("참입니다.")

# 조건을 체크 후 true 이면 실행문을 1회 실행시키고
# 다시 조건을 체크하고, true이면 다시 실행
# 조건이 false가 되는 순간 while 문 종료
a = 0
while a<5:
    print(str(a)+"번 반복")          # a +=1이 print 위로 가면
    a += 1                          # 반복횟수는 동일하지만 값이 달라질 수 있다.

# # 1~1000까지만 프린트 되도록 출력.
# # 1~1000까지 모두 더한 값을 출력 + 평균값 
sum = 0
a = 0
while a < 1000:
      a += 1  #sum 을 안에다가 넣으면 반복될때마다 sum = n n값으로 초기화
      sum += a
print(sum)  
print(sum/1000)

# # while문에서 반복을 진행하다가 break를 만나면, 반복문 종료.
# # if 문을 써서 n조건하에 break
sum = 0
a = 0
while True:
     a += 1  
     sum += a
     if a == 1000:
         break    
print(sum)  

# continue : 이 구문을 만나면, 다시 반복문 조건으로 이동
# 아래와 같이 코딩하면 hello가 무한 출력이 된다.
# a = 0
# while a<1000:
#     print("hello")
#     continue           #다시 조건문으로, a += 1 무시하기때문에 무한 반복
#     a += 1

# 홀수만 더해서 출력하기
sum = 0
a = 0
while a<1001:
    a += 1
    if a%2 == 0:
        #continue 문을 할용해서 coding
print(sum)
