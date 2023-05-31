# file 시스템 입출력 라이브러리 : open
# open 함수는 mode(w,r,a)를 가지고 있다.
# w:write(덮어쓰기), r:read, a:추가
# open을 했을 때 해당 파일명이 없으면 자동생성

# f = open("test.txt", "w")
# f.close()

f = open("text.txt","w", encoding="UTF-8")# encoding="UTF-8" 이없으면 한글이 깨져서 나옴
for i in range(0, 10):
    date = "%d 번째 줄입니다.\n" %i
    f.write(date)
f.close()

