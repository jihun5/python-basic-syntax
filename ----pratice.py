numbers = [1, 2, -3, 4, -5]
# result = 15
#  절대 값 해놓고 하기
# 그냥 곱한값이 최대한 나오는 경우를 max로 구해야 겠다
# 절대값이 나오는 경우랑 비교 해서 더 높은 숫자 고르기
# max = 1
# for a in numbers:
#     if a*numbers[a] >= max:
#         a = max
# print(max)
# numbers[0] = 1
# numbers[1] = 2
# max1 = 1 
# for a in range(len(numbers)):
#     if a*numbers[a]
# 오름차순으로 정렬하면 가장 큰 값이 맨앞과 바로 맨뒤로 오기때문에
# -의 경우 맨뒤로 가기때문에 맨앞 두 수와 맨 뒤 두수의 비교를 통해
# max를 구하면 된다
# numbers.sort()
# print(numbers)

# num_list = [3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1]
# # result = 51
# num1 = 0
# num2 = 1
# for a in num_list:
#     if len(num_list) >= 11:
#         num1 += a
#     elif len(num_list) <= 10:
#         num2 *= a
# print(num2) 


# '''한자리 정수로 이루어진 문자열 num_str있을 때 각 자리수의 합을 return 하도록'''
# num_str = "100000"
# num = list(map(int, num_str))
# # print(a)
# print(num)
# add = 0
# for a in num:
#     add += a
# print(add)

# num_list = [12, 4, 15, 46, 38, -2, 15]
# #각각의 요소를 꺼내어 0보다 작을시 그 인덱스 값을 출력하도록 하라
# search = 0
# for a in range(len(num_list)):
#     if num_list[a] < 0:
#         search = num_list[a]
#         answer = num_list.index(search)
#     elif num_list[a] > 0:
#         answer = -1
# # 인덱스의 몇번째가 -2인가?
# print(answer)

'''
emergency가 매개변수일때
진료순서를 정하시오
'''
emergency = [3, 76, 24]
# result = [3, 1, 2]
# emer전시에 0번쨰 1번째 2번째를 비교하면되잖아
# ex) emergency[0] < emergency[1] 
# answer = [위에꺼결과를 순서대로 넣기]