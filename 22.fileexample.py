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

import os
# os 라이브러리를 활용한 디렉터리 내에 파일 검색
# .py로 끝나는 파이썬확장파일을 search
# 현재 폴더에서만 검색
# searchDir = r'C:\Users\user\Desktop\오지훈' #\python-basic-syntax
# 파일, 디렉토리 목록을 뽑아내는 listdir 함수 사용
# dirList = os.listdir(searchDir)
# print(dirList)
# for dir in dirList:
#     dirTuple = os.path.splitext(dir)
#     if(dirTuple[1]=='.py'):
#         fullpath = os.path.join(searchDir, dir)
#         print(fullpath)
# 그 다음 폴더까지 검색
searchDir = r'C:\Users\user\Desktop\오지훈' 
dirList = os.listdir(searchDir) #searchDir 목록안에 있는 파일들 꺼내기
for dir in dirList: # searchDir 목록안에 있는 파일들 꺼내기 
    filename = os.path.join(searchDir, dir) # filename = searchDir 목록안에 있는 dir 값 경로꺼내기 
    if os.path.isdir(filename): # 만약 filename과 isdir의 경로가 같다면  
        dirlist2 = os.listdir(filename) #dirlist2 의 경로는 filename경로 값에 listdir 
        for dir2 in dirlist2:  # filename경로 값에 listdir 값에 dir2를 넣고
            dirTuple2 = os.path.splitext(dir2) # dirTuple2 = os.path.splitext(dir2) dir2의 값에 경로를 dirTuple2에넣고
            if(dirTuple2[1]=='.py'): #만약 dirTuple2에 뒤에 즉 (파일명)뒤에 확장자가 py의 값을 가지게 되면 
                fullPath = os.path.join(filename, dir2) # fullpath의 경로는filname(상위폴더)에서 dir2(filename의 경로 값)
                print(fullPath) #결국 여기서 가져올 수 있는것은 경로인데 무슨 경로나filname내부에 폴더를 뒤져서 나온 .py파일들을 가져갈 수 있는 것
    dirTuple = os.path.splitext(dir)
    if(dirTuple[1]=='.py'):
        fullPath = os.path.join(searchDir, dir)
        print(fullPath)
#알아 내고자하는 것 : 내 파일 경로 안에 py확장자를 쓰는 것의 경로 
# 상위폴더랑 내에는 py파일명확장자가 없기때문에 하위폴더를 검색하고 그안에서 py값을 찾아내서 그 경로를 업데이트 시켜야 한다.
# 모든 폴더까지검색 