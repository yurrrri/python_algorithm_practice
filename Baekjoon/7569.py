import sys
from collections import deque

answer = 0 #최소 일수
m, n, h = map(int, sys.stdin.readline().rstrip().split())
graph = []
q = deque([])

for i in range(h):
  temp = []
  for j in range(n):
    temp.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for k in range(m):
      if temp[j][k] == 1:
        q.append([i, j, k])

  graph.append(temp)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

while q:
  x, y, z = q.popleft()

  for i in range(6):
    nx = x+dx[i]
    ny = y+dy[i]
    nz = z+dz[i]

    if 0<=nx<h and 0<=ny<n and 0<=nz<m and graph[nx][ny][nz] == 0:
      q.append([nx, ny, nz])
      graph[nx][ny][nz] = graph[x][y][z]+1 #최소 드는 시간 == 최단 경로


answer = 0
for i in range(h):
  for j in range(n):
    for k in range(m):
      if graph[i][j][k] == 0: #다 안익음
        print(-1)
        exit(0) #break는 가장 인접한 반복문만 빠져나오기 때문에, 아얘 종료를 해버려야함
      answer = max(answer, graph[i][j][k])

print(answer-1)