
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

