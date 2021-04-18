n, m = map(int, input().split())
x, y, direction = map(int, input().split())
board = []

for i in range(n):
  board.append(list(map(int, input().split())))
board[x][y] = 1 #현재 위치 방문처리

#북동남서 방향 list 만들기
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left(): #왼쪽방향으로 회전
  global direction #함수 바깥에서 선언된 전역변수이기 때문
  direction -=1
  if direction==-1:
    direction = 3

count = 1
blocked=0
while True:
  turn_left() #1) 현재방향 기준으로 왼쪽방향부터 회전
  nx = x+dx[direction] #이동!!
  ny = y+dy[direction] #이동!!
  if board[nx][ny]==0: #아직 안가본곳
    x = nx #그 방향으로 전진
    y = ny
    board[x][y] =1
    count+=1
    blocked = 0
  else:
    blocked+=1 #막혀있으면 다시 돌아가기

  if blocked==4:
    nx = x-dx[direction]
    ny = y-dy[direction]
    if board[nx][ny]==0:
      x = nx
      y = ny
      board[nx][ny] = 1
    else:
      break
    blocked = 0

print(count)