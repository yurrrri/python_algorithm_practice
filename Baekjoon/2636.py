from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = [] # 치즈조각의 개수를 저장할 리스트

def bfs():
  q = deque([(0, 0)])
  visited[0][0] = 1
  count = 0
  
  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
        if board[nx][ny] == 1:  # 맞닿은 면이 치즈라면, 
          visited[nx][ny] = 2   # 치즈임을 표시
        elif board[nx][ny] == 0: # 공기라면 탐색을 위해 큐에 추가
          q.append((nx, ny))
          visited[nx][ny] = 1   # 방문표시

  for i in range(n):   # 1시간 마다 공기와 맞닿은 치즈를 녹임
    for j in range(m):
      if visited[i][j] == 2:   # 치즈인 경우에만 
        count += 1
        board[i][j] = 0   # 녹이기

  ans.append(count)
  return count

answer = 0
while True:
  visited = [[0] * m for _ in range(n)]
  count = bfs()
  if count == 0:
    print(answer)
    print(ans[-2])
    exit()
  answer += 1