import heapq
import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
INF = int(1e9)

for _ in range(m):
  a, b, c = map(int, input().rstrip().split())
  graph[a].append((b, c))
start, end = map(int, input().rstrip().split())
distance = [INF] * (n+1)

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
      continue

    for e, c in graph[now]: # 연결된 그래프들을 탐색하면서
      if dist + c < distance[e]: # 만약에 한 그래프와의 거리가 현재 비용에서 거리를 더한 값보다 크면 현재의 거리에서 비용을 더한 값으로 갱신 후 힙에 추가
        distance[e] = dist + c
        heapq.heappush(q, (dist + c, e))

dijkstra(start)
print(distance[end])