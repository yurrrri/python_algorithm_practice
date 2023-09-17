from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
      
def bfs():
  q = deque([(0, 0)])
  visited[0][0] = 1
  count = 0

  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<=nx<n and 0<=ny<m:
        if board[nx][ny] == 1:   # 맞닿은 면이 치즈라면, 해당 치즈의 공기 맞닿은 수를 +1을 해줌
          visited[nx][ny] += 1
        elif board[nx][ny] == 0 and not visited[nx][ny]:  # 공기인 경우에 더 판단할 가능성이 없으므로 바로 방문처리 해줌
          visited[nx][ny] = 1
          q.append((nx, ny))

  for i in range(n):
    for j in range(m):
      if visited[i][j] >= 2:  # 2면 이상 닿았다면
        board[i][j] = 0  # 치즈를 녹이고
        count += 1  # 녹은 치즈 + 1

  return count

answer = 0
while True:
  visited = [[0] * m for _ in range(n)]  # 방문여부 + 공기와 몇변을 맞닿았는지를 세기 위한 배열
  count = bfs()   # 녹은 치즈의 개수 --> 이게 0이면 바로 answer 반환
  if count == 0:
    print(answer)
    exit()
  answer += 1  # 시간 count