from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v+1)
graph = [[] for _ in range(v+1)]

for _ in range(e):
  a, b = map(int, input().split())
  graph[a].append(b)
  indegree[b] += 1 #진입차수 1 증가

def topology_sort():
  result = [] #결과 출력하기 위한 리스트
  q = deque()

  for i in range(1, n+1):
    if indegree[i] == 0:
      q.append(i) #진입차수가 0인 노드를 큐에 넣음

  while q:
    now = q.popleft()
    result.append(now)

    for i in graph[now]:
      indegree[i] -= 1
      if indegree[i] == 0:
        q.append(i)

  for i in result:
    print(i, end=' ')

topology_sort()
  