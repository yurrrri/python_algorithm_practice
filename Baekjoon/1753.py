import sys
import heapq

#이 문제는 v와 e의 범위가 커서 다익스트라로 풀어야함 (메모리 초과가 발생할 수 있기 때문)
v, e = map(int, sys.stdin.readline().rstrip().split()) #v: 정점의 개수 e: 간선의 개수
start = int(sys.stdin.readline().rstrip()) #시작 정점

INF = int(1e9)
distance = [INF] * (v+1)
q = []
graph = [[] for _ in range(v+1)]

for _ in range(e):
  a, b, c = map(int, sys.stdin.readline().rstrip().split())
  graph[a].append((b, c))

def dijkstra(start):
  distance[start] = 0
  heapq.heappush(q, (0, start))

  while q:
    dist, now = heapq.heappop(q)

    if dist > distance[now]: #이미 처리한 것으로 간주하고 무시
      continue

    for i in graph[now]:
      cost = i[1] + dist
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0])) 

dijkstra(start)  
  
for i in range(1, v+1):
  if distance[i] == INF:
    print("INF")
  else:
    print(distance[i])