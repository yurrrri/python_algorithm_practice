#이 문제는 다시 풀어볼것 
import sys

N = int(sys.stdin.readline().rstrip())

board = [[0] * 101 for _ in range(101)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for _ in range(N):
  x, y, d, g = map(int, sys.stdin.readline().rstrip().split())

  dragon_direction = [d] #첫 시작점은 무조건 들어감
  board[x][y] = 1 # 좌표 1로 칠하기
  for _ in range(g):
    tmp = []
    for j in range(len(dragon_direction)):
      tmp.append((dragon_direction[(len(dragon_direction)-j-1)] + 1) % 4)
    dragon_direction.extend(tmp)

  for i in dragon_direction:
    nx = x + dx[i]
    ny = y + dy[i]

    board[nx][ny] = 1

    x = nx
    y = ny

count = 0 #네 꼭지점이 모두 드래곤 커브의 일부인 것의 갯수
for i in range(100):
  for j in range(100):
    if board[i][j] == 1 and board[i+1][j] == 1 and board[i+1][j+1] == 1 and board[i][j+1] == 1:
      count += 1

print(count)