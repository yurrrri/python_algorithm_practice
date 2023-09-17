import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline
n = int(input())
board = [list(input().rstrip().split()) for _ in range(n)]

empty_list = []
teacher = []

dx = [1,-1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
  for j in range(n):
    if board[i][j] == "X":
      empty_list.append((i, j))
    elif board[i][j] == "T":
      teacher.append((i, j))
      
canSetO = list(combinations(empty_list, 3))

def bfs():
  q = deque(teacher)

  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x
      ny = y
      # 직선 방향으로 확인
      while True:
        nx += dx[i]
        ny += dy[i]
        if not(0<=nx<n and 0<=ny<n):
          break
        if board[nx][ny] == 'O':
          break
        elif board[nx][ny] == 'S': # 1명의 학생이라도 감시 안에 들었다면 실패
          return False

  return True # 모든 학생을 감시할 수 없다면 True return

for c in canSetO:
  count = 0
  for x, y in c:
    board[x][y] = "O"
    
    count += 1

    if count == 3:
      result = bfs()
      if result: # 모든 학생을 감시할 수 없는 경우가 하나라도 있다면 YES 출력 후 종료
        print("YES")
        exit()

  for x, y in c:
    board[x][y] = "X"

print("NO")   # 위에서 감시할 수 없는 경우가 없는 경우가 1개라도 없었따면, NO 출력