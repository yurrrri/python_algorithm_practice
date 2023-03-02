import sys
import heapq

start, k = map(int, sys.stdin.readline().rstrip().split())
q = []
INF = int(1e9)
distance = [INF] * (100001)

def dijkstra(start):
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    dist, n = heapq.heappop(q)

    for i in [(1, n+1), (1, n-1), (0, 2*n)]: #현재 시점 기준으로 갈곳 정해서 그 노드와의 최단거리 갱신
      if 0<=i[1]<=100000: #범위 체크
        cost = dist + i[0]
        if cost < distance[i[1]]:
          distance[i[1]] = cost
          heapq.heappush(q, (cost, i[1]))

dijkstra(start)

print(distance[k])