from collections import deque

v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
indegree = [0] * (v+1) #처음에 모든 노드의 진입차수는 0

for _ in range(e):
  a, b = map(int, input().split())
  graph[a].append(b)
  indegree[b] += 1 #진입차수 1 증가

def topology_sort():
  result = [] #큐에서 빠져나가는 순서를 담을 결과 배열
  q = deque()

  #처음 시작할때에는 진입차수가 0인 노드를 큐에 삽입
  for i in range(1, v+1):
    if indegree[i] == 0:
      q.append(i)

  while q:
    now = q.popleft()
    result.append(now) #노드에서 나오는 순서대로 result에 원소 추가

    for i in graph[now]:
      indegree[i] -= 1

      if indegree[i] == 0:
        q.append(i)

  for i in result:
    print(i, end=' ')

topology_sort()