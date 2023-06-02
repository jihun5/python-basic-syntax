# numbers = [1, 2, -3, 4, -5]
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
홀수만 이어붙이기
짝수만 이어붙이기
그리고 두 수를 더하기
'''
# num_list = [3, 4, 5, 2, 1]
# result = 393
# a1 = []
# a2 = []
# for a in num_list:
#     if a%2 != 0:
#         a1.append(a)
#     else:
#         a2.append(a)
# print(a2)

''' 
정수배열 arr 각 50보다 크거나 짝수면 나누기 2
50보다 작은 홀수면 곱하기 2
'''
# arr = [1, 2, 3, 100, 99, 98]
# # result = [2, 2, 6, 50, 99, 49]
# a1 =[]
# a2 = []
# a3 = []
# for a in arr:
#     if (a > 50) and (a%2 == 0):
#         a1.append(a/2)
#     elif (a < 50) and (a%2 != 0):
#         a2.append(a*2)
#     else:
#         a3.append(a)
# print(a1)
# print(a2)
# print(a3)
# answer = a1 +a2 +a3
# answer.sort()
# print(answer)

# i = ("a,e,i,o,u")
# for a in i:
#     answer = answer.replace(i,"")

# '''
# 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1
# 크면 0 출력 
# '''
# num_list = [3, 4, 5, 2, 1]
# #  3*4*5*2*1 > (3+4+5+2+1)**2 0
# #  3*4*5*2*1 < (3+4+5+2+1)**2 1
# mul = 1
# add = 0
# for a in num_list:
#     mul *= a
#     add += a
#     add2 = add**2
# if mul > add2:
#     answer = 0
# else:
#     answer = 1

# '''
# 정수 배열arr 자연수 k가 주어지고
# k가 홀수면 arr * k
# k가 짝수면 arr + k 
# '''
# arr = [1, 2, 3, 100, 99, 98]
# k =3
# answer = []
# for a in range(len(arr)):
#     if k ==3:
#         answer[a] = arr[a]*k
# print(answer)

# print(answer[:])*k

# upper()
# lower()
# strArr = ["AAA","BBB","CCC","DDD"]
# # strArr[0].lower()
# # print(strArr[0].lower())
# # 짝수번째 인덱스 대문자로 바꾸기
# for a in strArr:
#     if strArr[a] == 

# my_string = "banana"
# target = "ana"
# # my_string 안에 target을 포함하고 있으면 1 아니면 0을 출력하라
# lista = list(my_string)
# listb = list(target)
# print(lista)
# for a in range(len(lista)):
#     if lista[a] == listb[0]:
#         answer = 1
#     else:
#         answer = 0
# print(answer)

# 마지막 원소가 그전 원소보다 크면 마지막원소에서 그전 원소 뺀값구하고
# 마지막원소가 그 전 원소보다 크지 않다면 마지막원소를 두배한 값을 추가
# num_list = [2,1,6]
# # 1 < 6 이 크네?  6-1값 찾고 append
# #  7 > 5 전이 더 크네? 5*2 추가
# # for a in num_list:
# # answer = []
# if num_list[-2] > num_list[-1]:
#     num_list[-1]*2
#     num_list.append(num_list[-1]*2)
#     print(num_list)
# else:
#     num_list.append(num_list[-1]-1)
#     print(num_list)

''' 
1부터 6까지 숫자가 적힌 주사위가 2개가 있다
a와 b가 모두 홀수면 a제곱+b제곱의 점수
a와 b중에 하나가 홀수면 2*(a+b)
a와 b 모두가 홀수가 아니라면 a-b인데 절대값기호 abs(a-b)
# '''
# a =3
# b= 5
# answer = 0
# if a%2 !=0 and b%2 !=0:
#     answer = (a**2)+(b**2)
# elif a%2 == 0 and b%2 == 0: 
#     answer = abs(a-b)
# else:
#     answer = 2*(a+b)
# print(answer)

# numbers = [34, 5, 71, 29, 100, 34]
# n = 123
# # answer = 139
# num = 0
# answer = 0
# for a in numbers:
#     num += a
# print(num)
# a = 10/14
# print(a)

# num_list = [4, 2, 6, 1, 7, 6]
# n=2
# a = num_list[::n]
# print(a)

''' 
요소의 홀수의 합과 짝수의 합을 비교하여 더 큰 값 출력하기
'''
# num_list = [4, 2, 6, 1, 7, 6]
# # result = 17
# # 짝수번째, 홀수번째항 따로 뽑아내기
# # a1 = [] #짝수   
# # a2 = [] #홀수
# a = num_list[::2]
# print(a) #홀수번째
# a1 = num_list[1::2] #짝수번째
# print(a1)
# # a랑 a1비교하여 큰 쪽 출력
# num1 = 0
# num2 = 0
# for i in a:
#     num1 += i
# print(num1)
# for e in a1:
#     num2 += e
# print(num2)
# if num1 > num2:
#     answer = num1
# else:
#     answer = num2

# def solution(my_string, is_suffix): 노상관
my_string = "banana" 
is_suffix = "ana"
answer_list = [my_string[i:] for i in range(len(my_string))]
return 1 if is_suffix in answer_list else 0
# answer_list를 만들었고
# 주어진 answer_list에 my_string을 슬라이싱할건데 
# i부터 끝까지 슬라이싱을 할거야 범위는 len(my_string)
# 즉 i값은 012345 i부터 끝까지 다 잘라내기
# retunr 1을 출력할던데 is_suffix가 answer_list안에 있으면 1을 출력하고
# 없으면 0을 출력한다
# nan가 없는 이유는 nana가 짤리고 그다음 ana가 짤리기에 없다는 표시가 뜨는것이다 
