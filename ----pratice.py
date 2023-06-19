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
# # lista
# 세 숫자가 모두 같다면
# (a+b+c)x(a**2+b**2+c**2)x(a**3+b**3+c**3)
# '''
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
# lista = list

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

# .... = h
# . = e
# .-.. = l
# --- = o
# .--. = p
# -.-- = y
# - = t
# -. = n
#
# def solution(letter):
#     morse = { 
#     '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
#     '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
#     '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
#     '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
#     '-.--':'y','--..':'z'
# }
#     print(morse['.-'])
    
#     letter = letter.split(' ')
#     answer = []
#     for i in letter:
#         answer.append(morse[i])
#     return ''.join(answer)

'''   
before에 revsere 한값이 after과 일치하면 1
안에 요소 순서를 바꾸어서 해당이 안되는 경우
일치하지 않으면 0
'''
# before = "olleh"
# after = "hello"
# A = "".join(reversed(before))
# B = 
# if before == after:
#      answer = 1
# else:
#      answer = 0

# i = 1
# j = 13
# k = 1
# result = 6
# # 정수 i,j,k가 매개 변수일때
# # i부터 j까지 k가 몇번 등장하는 지 return
# # num = 0
# num = []
# for a in range(i, j+1):
#      if str(k) in str(a):
#           num.append(a)
# str(num)
# answer = str(num).count("1")
# print(answer)

'''   
정수가 있을 때 짝이라면 반으로 나누고
홀수라면 1을 뺀뒤 반으로 나누고
반복
모든 원소를 1로 나누기 위해 필요한 연산의 횟수를 return
'''
'''
문자열 my_stirng이 매개 변수로 주어지는디
소문자, 대문자, 자연수로만 구성이 되어있는데
my_string 안의 자연수들의 합을 구하라
ex) aAB1B2CC34pOp
= 1+2+34 = 37
'''
# import re
# my_string = "aAb1B2cC34oOp"
# # answer = 37 # 1+2+34
# numbers = re.findall(r'\d+',"",my_string)
# print(numbers)


# participant = ["mislav", "stanko", "mislav", "ana"]
# completion = ["stanko", "ana", "mislav"]
# # result = "mislav"
# answer = ""
# dicta = {}
# for a in completion: # a = stanko, ana, mislava
#     if a not in dicta.keys(): # dicta에 a가없으면 딕셔너리 형태로만든다
#         dicta[a] = 1 # dicta{mislav : 1....} 
#     else:
#         dicta[a] = dicta[a] +1 # 아니면 dicta{mislav : 2}
# for i in participant: # mislav, stanko, mislav, ana
#     if i in dicta and dicta[i] > 0: # i가 dicta에 있고 dicta에 [i]값을 가지고 있으면
#         dicta[i] = dicta[i] -1 # -1하면 된다{mislav : 2 -1} 
#     else:
#         answer = i 
#         # values값이 0인친구가 출력되겠지? 즉
#         # 참여자 목록에 없는 dicta가 0이되는 친구가 출력이 될것이다.
# print(answer)

# participant = ["leo", "kiki", "eden", "ji"]
# completion =  ["eden", "kiki"]
# # result = "leo"
# dicta = {}
# answer = ""
# for a in completion:
#     if a not in dicta.keys():
#         dicta[a] = 1 # {leo : 1, kiki : 1, eden : 1}
#     else:
#         dicta[a] = dicta[a] +1 # 하는 이유 동명이인의 경우{leo : 2}가 될 수 있게
# for i in participant:
#     if i in dicta and dicta[i] > 0: # 즉 value값을 가지는가?
#         dicta[i] = dicta[i] -1 # {leo: 1} = {leo :1} -1 value
#     else:
#         answer = i # 참여자중 완주자 목록의 value값이 0이되는 순간 
#                     # 참여자중 완주하지 못한 자가 출력
# print(answer)

# dict1 = {"이름" : "홍길동", "age" : "25"}
# dict1['성별'] = "남성"
# print(dict1)

# del dict1['성별']
# print(dict1)

# keylist = dict1.keys()
# print(keylist)

# for a in dict1:
#     print(a)

# for a in dict1.values():
#     print(a)

# lista = ['A', 'A', 'B','O','O','AB','AB']
# dicta = {}
# # for a in lista:
# #     if a not in dicta.keys():
# #         dicta[a] = 1
# #     else:
# #         dicta[a] = dicta[a] +1
# for a in lista:
#     if a not in dicta.keys():
#         dicta[a] = lista.count(a)
# print(dicta)

# import requests
# import json


# import pandas
# import numpy
# from sklearn.preprocessing import MinMaxScaler
# url = "https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
# names = ['preg','plas','pres','skin','test','mass','pedi','age','class']
# dataframe = pandas.read_csv(url, names=names)
# array = dataframe.values

# X=array[:,0:8]
# Y =array[:,8]
# scler = MinMaxScaler(feature_range=(0,1))
# rescaledX = scler.fit_transform(X)
# numpy.set_printoptions(precision=3)
# print(rescaledX[0:5,:])

# from sklearn.svm import SVC

# x_train, x_test, y_train, y_test = train_test_split(cancer.data, cancer.target, random_state=0)
# svm = SVC(C=100)
# svm.fit(x_train, y_train)
# print("테스트 세트 정확도 : {:2f}".format(svm.score(x_test, y_test)))

# import requests
# import json
# from pandas import DataFrame

# urlFmt = "https://dapi.kakao.com/v3/search/book?query={query}&page={page}&size={size}"
# # 주소 값에 마지막에 ?를 넣어 원하는 결과를 덧붙이고 
# # 홈페이지에서 주어진 변수 값을 설정한 것 대로 넣을 수 있는공간
# # query, page, size가 변수값이고 각각을 연결하기 위해서는 처음을 제외하고
# # &문을 넣고 변수 = {} format변수를 사용하여 값을 지정한다.
# query = "파이썬"
# page = 1
# size = 50
# key = "899a1eedbcb6713b4e78b75f1e3ed026"
# session = requests.Session()
# session.headers.update({
#     "Authorization" : "KakaoAK %s" % key     
# })
# isEnd = False
# # 반복 수행 도중 추출되는 검색결과 리스트 결합할 빈 리스트 
# mylist = []
# # 1페이지부터 시작
# query = "은혼"
# page = 1
# while not isEnd:
#     #-----------------------------------------------------------------
#     # 이전 예제 코드 시작
#     url = urlFmt.format(query=query, page=page, size=size)
#     url
#     #출력된 데이터의 변수값 확인
#     r = session.get(url)
#     if r.status_code != 200:
#         msg = "[%d Error] %s 에러가 발생함" % (r.status_code, r.reason)
#         raise Exception(msg)
#     r.encoding = "utf-8"
#     data = json.loads(r.text)
#     # data
#     # -------------------------------------------------------------------
#     # 이전 예제 코드 끝 
#     # 추출한 리슽으를 미리 준비한 빈 리스트에  추가
#     searchList = data['documents']
#     mylist.extend(searchList)
#     # 증감식에 해당하는 isend변수 추출
#     isEnd = bool(data['meta']['is_end'])
#     page += 1
#     sum_price = [i.get('price') for i in mylist]
#     sale_price = [a.get('sale_price') for a in mylist]
#     normal_sale = [e.get("status") for e in mylist]
# print("은혼의 총 가격은?", sum(sum_price), "sale_price는?", sum(sale_price))
# print("총가격은: %d" % sum('price'))

# dict1 = {"이름" : "홍길동", "age" : "25"}
# dict1['성별'] = "남성"
# print(dict1)

# keylist = dict1.keys()
# print(keylist)