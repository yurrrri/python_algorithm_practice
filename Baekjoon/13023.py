from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)  #a와 b가 친구
    graph[b].append(a)

visited = [False] * n

def dfs(i, depth):
  if depth == 4:
    print(1)
    exit(0)

#백트래킹으로 탐색하는 이유: 방문처리만 하고 다시 방문해제 처리를 해주지 않으면, [2, 4] [2, 3] [3, 4] 이렇게 있을 때 모든 연결하는 노드를 탐색하지 못함
  for v in graph[i]:
    if not visited[v]:
      visited[v] = True
      dfs(v, depth+1)
      visited[v] = False

for i in range(n):
  dfs(i, 0)

print(0)