# # file 시스템 입출력 라이브러리 : open
# # open 함수는 mode(w,r,a)를 가지고 있다.
# # w:write(덮어쓰기), r:read, a:추가
# # open을 했을 때 해당 파일명이 없으면 자동생성

# # f = open("test.txt", "w")
# # f.close()

# f = open("text.txt","w", encoding="UTF-8")# encoding="UTF-8" 이없으면 한글이 깨져서 나옴
# for i in range(0, 10):
#     date = "%d 번째 줄입니다.\n" %i
#     f.write(date)
# f.close()

# f = open("text.txt","r", encoding="UTF-8")
# # 첫번쨰 줄만 가져오는 함수
# line = f.readline()
# print(line)
# # line1 = f.readline()
# # print(line1)
# f.close()

# while, if문으로 readline으로 전체 출력

# f = open("text.txt","r", encoding="UTF-8")
# line = f.readline
# while line:
#     print(line)
#     line = f.readline
# f.close()

# while True:
#     line = f.readlines()
#     print(line)
#     if not line:
#         break
# f.close()

f = open("text.txt","r", encoding="UTF-8")
# readlines : 데이터를 리스트형태로 라인별로담아둔다
lines = f.readlines()
for a in lines:
    print(a[0])
print(lines)
# 데이터 파싱하기가 편하다 위 형태가(파싱:가공)

f = open("text.txt","r", encoding="UTF-8")
# readlines : 데이터를 리스트형태로 라인별로담아둔다
lines = f.read()
print(lines)

# a옵션으로 추가모드
f = open("test.txt", "a", encoding="UTF-8")
#0~9번쨰 줄입니다 -> 10번째~19번쨰줄입니다.
for a in range(10,20):
    data = "%d번째 줄입니다. \n" %a
    f.write(data)
f.close()

# 파이썬에서 객체를 생성하고 나면, 힙메모리에 객체 할당된다.
# 객체의 사용이 끝나면 객체를 close 해줘야 하나?
# 그럴 필요가 없는게, 파이썬에서는 GC(Garbage Collector)가 내장되어
# 자동으로 사용빈도가 낮은 데이터는 메모리에서 삭제를 해준다.
# 그러나, 파일 시스템은 그렇지 못하므로 직접닫아줘야 한다.
# 그래야 메모리 낭비가 없다.