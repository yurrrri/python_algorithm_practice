import heapq

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
INF = int(1e9)

def dijkstra():
  distance = [[INF] * n for _ in range(n)]
  q = []
  distance[0][0] = board[0][0]   # 시작점 거리 배열에 초기화하기
  heapq.heappush(q, (board[0][0], (0, 0)))# 시작점 큐에 넣기

  while q:
    dist, (x, y) = heapq.heappop(q)

    if distance[x][y] < dist: # 이미 처리했다면
      continue

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<=nx<n and 0<=ny<n:
        cost = dist + board[nx][ny]
        if cost < distance[nx][ny]:
          distance[nx][ny] = cost
          heapq.heappush(q, (cost, (nx, ny)))

  return distance[n-1][n-1]
  
num = 0
while True:
  n = int(input())
  if n == 0:
    break

  num += 1
  board = []
  for _ in range(n):
    board.append(list(map(int, input().split())))

  result = dijkstra()
  print(f"Problem {num}: {result}")