import sys
position = sys.stdin.readline()

pos_row = int(position[1]) #행 위치
pos_col = ord(position[0])-ord('a')+1 #열 위치
answer = 0

direction = [(-2, -1), (2, -1), (-2, 1), (2, 1), (-1, 2), (1, -2), (-1, 2), (1, 2)] #이동할수 있는 방향
for dir in direction:
  next_row=pos_row+dir[0]
  next_col=pos_col+dir[1]

  if next_row>=1 and next_row<=8 and next_col>=1 and next_col<=8:
    answer+=1

print(answer)