
'''  
문자열을 다 합친것을 꼬리 문자열이라고 부르는디
특정 문자열을 제외하고 출력하는 것을 구하려고한다
'''
# str_list = ["abc", "def", "ghi"]
# ex = "ef"
# answer = ""
# for a in str_list: # abc, def, ghi
#     if not ex in a: #만약 ex가 abc, def, ghi쪽에 없으면
#         answer += a # a를 answer에다가 추가하라 -가 안되는 이유는 문자열끼리 -는 안되니까
# print(answer)

'''
빈배열 x가 있고 양의 정수 배열 arr가 매개 변로 주어질때
arr앞에서부터 차례대로 원소를 원소 a가 x의 맨뒤에 a번추가 하는 일을
반복적으로 한뒤 배열 x를 리턴하라
'''
# arr = [5,1,4]
# # answer = [5,5,5,5,5,1,4,4,4,4]
# # # a = arr[0]*5
# # # print(a)
# # for a in arr:
# #     b = arr.append(a)
# # print(b)

# answer = []
# for i in range(len(arr)): # 012
#     answer.append(i)

# mySting = "AABAA"
# A = mySting.replace("A", "B")
# B = mySting.replace("B", "A")
# for a in mySting:
#     "A" == "B" and "B" == "A"
# print(a)

# '''
# 연산 *은 두 정수에 대한 연산으로 두 정수를 붙여쓴 값을 반환한다
# '''
# #글자로 나타태고 합쳐버리고
# # mySting = "abstract alagebra"
# # a = mySting.lower()
# # print(a)
# # a.replace("a", "A")
# # print(a.replace("a", "A"))
# a= "ccs"
# a.upper
# import requests
# import json
# url = "https://api.binance.com/api/v3/ticker/24hr"
# response = requests.get(url)
# data_json = json.loads(response.text)
# print(data_json[0])
# # 출력 결과
# # "symbol" : "BTCUSDT", "lastPrice" : xxxxx(가격)
# for a in data_json:
#     if a['symbol'] == "BTCUSDT":
#         print(f"{a['symbol']}코인의 price는 {a['lastPrice']}입니다.")
# # print(f"{a['symbol']}코인의 price는 {a['lastPrice']} 입니다.")
# # print가 아니라, 값을 변수에 담아서, DB에 저장
# return my_string.split(" ")

'''
arr과 정수 n arr의 길이가 홀수면 arr의 짝수 인덱스 위치에 n을 더하고
arr길이가 짝수라면 arr 모든 홀수 인덱스 위치에 n을 더한 배열을 출력하라

'''

# arr = [49, 12, 100, 276, 33]
# a1 = []
# n =27
# for a in range(len(arr)):
#     if len(arr)%2 != 0:
#         if a%2 == 0:
#             arr[a] += n
#             a1.append(arr[a])
#         else:
#             a1.append(arr[a])
#     elif len(arr)%2 == 0:
#         if a%2 != 0:
#             arr[a] += n
#             a1.append(arr[a])
#         else:
#             a1.append(arr[a])
    
    
    
     # (짝수항에다가 더한 값들만 출력이 됐어)
# print(a1) 

'''     
cipher를 주고 받는데 code번째의 글짜만 암호다



# a1 = []
# a = (box[0]//n)
# b = (box[1]//n)
# c = (box[2]//n)
# answer = a*b*c
# print(answer)

# ineq = "<"
# eq = "="
# n = 20
# m = 
# 선분 세 개로 삼각형을 만들기
# 가장 긴 변의 길이는 다른 두변의 길이의 합보다 작아야한다
# sides가 [3,6]일 떼 될 수 있는 나머지 변은 4,5,6으로 3개
# 나머지 한변이 가장 긴 경우는 7,8로 2개
# sides가 [11,7]인 경우 가장 긴변이 11인 경우5,6,7,8,9,10,11로 7개
# 나머지 한변이 가장 긴 경우는 12,13,14,15,16,17로 6개다 7+6 13개를 리턴
# sides를 오름차순해서 -1번째 index를 구하고
# 그 값이 가장 긴변일 경우 와 나머지 한 변이 가장 긴 변일 경우 2가지 경우를 구하면 된다.
# sides = [3,6]
# sides.sort()
# print(sides)
# # 가장 긴 변은 sides[-1]인경우
# # 나머지 변의 경우 sides[0]+sides[-1] > 나머지 변
# # num = 0
# lista =[]
# listb =[]
# for i in range(0, sides[1]+1): # a = 7부터 11까지 
#      if sides[0]+i > sides[-1]:
#           lista.append(i) # 가장 기변의 경우 7개
# for a in range(i+1, sides[0]+sides[-1]): # 0부터 18까지
#      if sides[0]+sides[-1] > a:
#           listb.append(a) # 가장 긴 변이 나머지 인경우 6개
# answer = len(lista)+len(listb)
# print(answer)

# n = 3
# num = ""
# for a in range(1, n+1): #a = 0,1,2,3
, false, true, false]
# temp = []
# finished[0] = 1
# finished[1] = 0
# finished[2] = 1
# finished[3] = 0
# # finished[0] = True
# # answer = []
# # for i in finished:
# #      if finished[i] == True:
# #           answer.append(todo_list.remove(i))
# # print(answer)
# prin
#             lista[a] = lista[b]
#             lista[b] = temp

# direction = "left"
# numbers = [4,455,6,4,-1,45,6]
# # temp = []

# lista = list(my_string)
# temp = []
# temp = lista[num1]
# lista[num1] = lista[num2]
# lista[num2] = temp
# print(lista)
# answer = "".join(lista)
# print(answer)
나머지는 다른경우
(a+b+c)x(a**2+b**2+c**2)
세 숫자가 모두 같다면
(a+b+c)x(a**2+b**2+c**2)x(a**3+b**3+c**3)
'''
# a =2
# b =6
# c= 1
# if (a != b) and (a != c) and (b != c):
#      answer = a + b + c
# if a == b and a == c:
#      answer = (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
# if a == b and a != c or b == c and a != b:
#      answer = (a+b+c)*(a**2+b**2+c**2)

'''   
num과 k가 매개변수로 주어질 때
num을 이루는 숫자중에 k가있으면 
num의 그 숫자가 있는 자리수를 return하라
'''
# num = [1,2,3]
# num.index(2)
# print(num.index(1))

# num = 29183
# k = 1
# # answer = 3
# lista = list(str(num))
# # print(lista)
# # print(lista.index(str(k))+1)
# # answer = 0
# # for a in range(len(lista)): # a = 0,1,2,3,4
# #      if lista[a] in str(k):
# #           answer = lista.index(k)
# # print(answer)
# ansnwer = 0
# for a in range(len(lista)): #a = 0,1,2,3,4
#      if lista[a] == k:
#           print(a) 
#      # break
# print(k)

# number = "123"
# int(number)
# print(number)
# print(int(number)%9)

# arr = [0, 0, 0, 1]
# idx = 1
# # result = 3

# for a in arr:
#      if arr[a] == idx:
#           answer = arr.index(a)
# print(arr.index(a))

# for a in arr:
#      if arr[a] == idx:
#           answer = arr.index(a)

# emergency = [3,76,24]
# # answer =[3,1,2]
# # 오름차순정렬 후 순서 매기기
# # max2 = 0 
# temp = []
# # emergency.sort(reverse=True)
# # print(emergency)
# temp = sorted(emergency, reverse=True)
# print(temp)
# for a in emergency:
#      temp.append(emergency.index(a)+1)
# print(temp)
# print(emergency)

# num = 29183
# lista = list(str(num))
# print(lista)
# k = 1
# A = str(k)
# print(A)
# # temp = []
# # A = lista.index('k')+1
# # print(A)    

# binomial = "43 + 12"
# result =  55
# lista = list(binomial)
# print(lista)
# num = []
# if binomial in "+":
#      print(int(binomial)) 

# answer = []
# arr = [293, 1000, 395, 678, 94]
# delete_list = [94, 777, 104, 1000, 1, 12]
# for i in arr:
#      if i not in delete_list:
#           answer.append(i)
# # print(answer)
# myString = "dxccxbbbxaaaa"
# # result = ["a","b","c","d"]
# lista = list(myString)
# answer = []
# for a in lista:
#      if a not in "x":
#           answer.append(a)  
# print(answer)
# # 같은 글자를 더하면 되잖아
# temp = []
# num = 0
# for i in range(len(answer)):
#      if answer[i] == :
#           num *= i
#           temp.append(i)
# print(temp)

# def solution(strings, n):
#     return sorted(strings, key=lambda x:(x[n],x))
# num_list = [12]
# # result = 11
# num = 1
# temp = []
# for a in num_list:
#      if a%2 == 0:
#           num /= a
#           temp.append(num)
#      # elif a%2 != 0:
#      #      a-1
#      #      num /= a
#      #      temp.append(num)
# print(temp)

# import re
# def solution(my_string):
#      answer = re.findall(r'\d', my_string)
#      answer = [int(i) for i in answer]
#      return sum(answer)

# s = "abcabcadc"
# answer = ""
# for a in s:
#      if s.count(a) == 1:
#           answer = a
# print(answer)

# my_string = "apporoograpemmemprs"
# indices = [1, 16, 6, 15, 0, 10, 11, 3]
# # A = sorted(indices)
# # print(A) 
# # lista = list(my_string)
# # print(lista)
# # for a in A:
# #      del lista[a]
# # my_string.replace(str(indices), '')
# # for a in indices:
# #      my_string.replace(a, "")
# # print(my_string)

# nums = ["zero","one","two","three"""""""""""""]

# my_string = "cvsgiorszzzmrpaqpe"
# index_list = [16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7]
# # result = "programmers"
# lista = list(my_string)
# answer = []
# for a in index_list:
#      answer.append(lista[a])
# print(answer)     

# strArr[0]은 짝수번째 인덱스의 문자열이므로 소문자로 바꿔서 "abc"가 됩니다.
# strArr[1]은 홀수번째 인덱스의 문자열이므로 대문자로 바꿔서 "ABC"가 됩니다.
# 따라서 ["abc","ABC"]를 return 합니다.
# strArr = ["AAA","BBB","CCC","DDD"]
# result = ["aaa","BBB","ccc","DDD"]
# answer = []
# # for i in strArr: 
# #      answer.append(i.lower())
# for a in range(len(strArr)):
#      if a%2 == 0:
#           answer.append(strArr[a].lower())
#      elif a%2 != 0:
#           answer.append(strArr[a].upper)
# print(answer)


# answer = 0
# for i in range(1, n):
#      if n < 6:
#           answer = 0
#      if (n*i)%6 == 0:
#           answer = (n*i)//6
#           break
# return answer

# strArr = ["and","notad","abcd"]
# answer = []
# for a in strArr:
#      if "ad" not in a:
#           answer.append(a)
# print(answer)     
# a = 2
# b = 91
# lista = list(str(a))
# listb = list(str(b))
# A = (lista+listb)
# line = ''.join(map(str, A))
# mul = 2*a*b
# # 단 같으면 line 리턴하라는 거네
# if line >= mul:
#      answer = line
# elif line < mul:
#      answer = mul

# arr = [5,1,4]
# # result = [5,5,5,5,5,1,4,4,4,4]
# A = "5"
# B = "1"
# C = "4"
# print(A*arr[0]) # A의 첫번째와 arr의 첫번째요소가 곱해지면돼
# print(B*arr[1])
# print(C*arr[2])
# lista = list(A+B+C)
# print(lista)

# my_string = ["progressive", "hamburger", "hammer", "ahocorasick"]
# parts = [[0,4], [1,2], [3,5], [7,7]]
# a2 = parts[0]
# A = list(my_string[0])
# A1 = A[a2]
# print(A1)
# answer = ''
# for idx, part in enumerate
# names = ["nami", "ahri", "jayce", "garen", "ivern", "vex", "jinx"]
# answer = []
# a1 = names[:5]
# a2 = []
# for a in names:
#      if a not in a1:
#           a2.append(a)
# print(a2)
# answer.append(a1[0])
# answer.append(a2[0])
# print(answer)

# myString = "ABBAA" # BAABB
# pat = "AABB"
# new = ""
# new1 = ""
# A = myString.replace("A", "N")
# A1 = A.replace("B", "A")
# B = A1.replace("N", "B")
# print(B)
# if pat not in myString:
#      answer = 1
# else:
#      answer = 0
# for a in myString: # a = A B B A A 
#      if myString in "A":
#           myString.replace("A", "N") # mysyting = N B B A A 
#      elif     

'''
연산 * 은 두정수를 붙여쓴 것을 말한다
a*b와 b*a를 비교한 것중 높은 것을 출력하고
같으면 a*b를 출력하라
'''
# a = 9
# b = 91
# A = str(a)
# B = str(b)
# answer = 0
# if A+B >= B+A:
#      answer = int(A+B)
# else:
#      answer = int(B+A) 

'''
두 배열의 대소관계 비교
길이가 다르면 길이가 긴쪽이 더 크다.
배열의 길이가 같으면 모든 원소의 합을 비교하여 더큰 쪽이더 크고
같으면 같다    
arr1 , arr2를 비교할건디
arr2가 크면 -1
arr1이 크면 1
같으면 0
'''
# arr1 = [100, 17, 84, 1]
# arr2 = [55, 12, 65, 36]
# answer = 0
# num1 = 0
# num2 = 0
# if len(arr1) < len(arr2):
#      answer = -1
# elif len(arr1) > len(arr2):
#      answer = 1
# if len(arr1) == len(arr2):
#      for a in arr1:
#           num1 += a
#      for i in arr2:
#           num2 += i
#           if num1 > num2:
#                answer = 1
#           elif num1 < num2:
#                answer = -1
#           elif num1 == num2:
#                answer = 0
# print(answer)

# import re
# my_string = "hi12392"
# # result= [1,2,3,9,2] 오름차순
# numbers = re.sub(r'[^0-9]',"", my_string)
# print(numbers)
# numbers = re.findall(r'\d+', my_string)
# print(numbers)
# numbers = re.findall(r'\d', my_string)
# print(numbers)


# my_strings = ["progressive", "hamburger", "hammer", "ahocorasick"]
# parts = [[0, 4], [1, 2], [3, 5], [7, 7]]
# # parts[i] = [0,4]
# # my_strings[i] = "progressive"
# # i = 0 일떄 "progr"
# A = my_strings[0]
# B = my_strings[1]
# C = my_strings[2]
# D = my_strings[3]
# # print(A)
# # print(A[parts[0]:parts[1]])
# # print(A[0:4]) # 이게 맞음
# for a in parts:
#      print(a)
# A1 = a[0]
# print(A1)
# my_strings = ["progressive", "hamburger", "hammer", "ahocorasick"]
# parts = [[0, 4], [1, 2], [3, 5], [7, 7]]
# answer = ""
# for i in range(len(my_strings)):
#      answer += my_strings[i][parts[i][0] : parts[i][1] +1]
#      # answer += my_strings[0]parts[0][0] : parts[0][1] + 1]
#      # answer += my_strings[1]parts[1][0] : parts[1][1] + 1]
# A = my_strings[0][parts[0][0] : parts[0][1]+1] 
# print(A)
# I = "SISOKO"
# B = I[parts[0][0]:parts[0][1]+1]
# # print(B)
# result = []
# my_string = "banana"
# for a in my_string:
#      result.append(my_string[a:])
# print(result)