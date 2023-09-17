from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, input().split())
visited = [[0] * m for _ in range(n)]
board = []

for i in range(n):
  board.append(list(input()))

answer = 0
def bfs(i, j):
  q = deque([])
  q.append((i, j))
  visited = [[0] * m for _ in range(n)]

  """
  오답노트: visited를 매번 탐색 시 초기화해줘야하는 이유
  일단 문제에서 구역으로 나뉘어져있다는 정확한 제시가 없고, 첫번째 탐색 시도 시 탐색하지 않은 L이 있는 구역이 남아있을 수도 있어서 해당 부분에서 새롭게 탐색을 시작하여 최단거리의 최대값을 구해서 갱신할 필요가 있음
  """
  visited[i][j] = 1
  count = 0
  
  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<=nx<n and 0<=ny<m and board[nx][ny] == "L" and not visited[nx][ny]:
        visited[nx][ny] = visited[x][y] + 1
        q.append((nx, ny))
        count = max(count, visited[nx][ny])  # 최단 거리 중 가장 긴 시간을 구해야함

  return count-1  # 두 최단 거리 사이의 거리이므로 -1을 해줘야함

for i in range(n):
  for j in range(m):
    if not visited[i][j] and board[i][j] == "L":
      answer = max(answer, bfs(i, j))

print(answer)