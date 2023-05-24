# list의 정렬은 srot()함수 사용
# sort()는 오름차순 정렬
# reverse=True는 내림차순 정렬
numa = [5,3,18,4,2,1]
numa.sort()
print(numa)
numa.sort(reverse=True)
print(numa)
print(numa[0]) # 내림차순 시 가장 점수가 높은 사람

# 문자의 정렬
chlist = ['brad','john','abc']
chlist.sort()
print(chlist) #알파벳 순서, 한글 순서 a b c, ㄱ ㄴ ㄷ

# list(뒤집기) : reverse()
chlist.reverse()
print(chlist)

# list위치 반환 : index
lista = ["김돌쇠", "김갑돌", "김갑순", "김철수"]
print(lista.index("김철수"))
#  배열(타 언어) = 리스트 

# 마지막요소 끄집어 내기 : pop()
# remove and return last value
lista.pop()
lastValue = lista.pop() # pop이 실행이 되는순간 remove가 
                        # 되기때문에 김철수가 지워지고 그 다음 마지막인 김갑순이 출력
print(lastValue)
