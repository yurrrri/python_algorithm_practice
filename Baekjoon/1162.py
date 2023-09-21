import sys
import heapq

input = sys.stdin.readline
INF = 9999888777666
q = []
n, m, k = map(int, input().rstrip().split())  # k --> 최대 포장할 수 있는 도로의 개수
graph = [[] for _ in range(n+1)] 
distance = [[INF] * (k+1) for _ in range(n+1)]  # (r, c) --> 1에서 r 도시로 갈 때 포장 도로 개수가 c일 때의 최소 비용

for _ in range(m):
  a, b, c = map(int, input().rstrip().split())
  graph[a].append((b, c))
  graph[b].append((a, c))  # 양방향 도로

def dijkstra(start):
  heapq.heappush(q, (0, start, 0))  # 차례대로 비용, 노드, 포장한 도로의 개수
  for i in range(k+1):
    distance[start][i] = 0

  while q:
    dist, now, p = heapq.heappop(q)

    if distance[now][p] < dist:
      continue

    # 포장을 하는 경우
    if p + 1 <= k:
      for (next, cost) in graph[now]:
        if dist < distance[next][p+1]:
          distance[next][p+1] = dist  # 포장을 하면 포장 비용이 0이므로 현재 dist를 그대로 가져옴
          heapq.heappush(q, (dist, next, p+1))

    # 포장을 하지 않는 경우
    for (next, cost) in graph[now]:
      if dist + cost < distance[next][p]:
        distance[next][p] = dist + cost
        heapq.heappush(q, (dist + cost, next, p))

dijkstra(1)
answer = INF

for i in range(k+1):
  answer = min(answer, distance[n][i])

print(answer)