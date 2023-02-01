import sys

n = int(sys.stdin.readline()) #n, list 초기화
direc_list = sys.stdin.readline().split()

x, y = 1, 1 # 시작좌표 초기화
for i in direc_list:
  if i=='R' and y!=5:
    y+=1
  elif i=='U' and x!=1:
    x-=1
  elif i=='L' and y!=1:
    y-=1
  elif i=='D' and x!=5:
    x+=1

print(x, y)