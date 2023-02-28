import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
q = [] #우선순위 큐
distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append((b,1)) #a에서 b로 거쳐가는 거리가 1
  graph[b].append((a,1)) #양방향

def dijkstra(start):
  distance[start] = 0
  heapq.heappush(q, (0, start)) #초기화

  while q:
    dist, now = heapq.heappop(q) #거리, 현재 노드

    if distance[now] < dist:
      continue

    for i in graph[now]:
      cost = dist + i[1]

      if cost < distance[i[0]]: #그래프에 연결된 노드와의 거리가 기존 거리보다 작다면
        distance[i[0]] = cost #갱신
        heapq.heappush(q, (cost, i[0])) #추가

dijkstra(1) #1번 헛간에서 출발

max_index = []
count = 0

distance[0] = 0 #최대값을 구하기 위한 초기화
max_distance = max(distance)

for i in range(1, n+1):
  if distance[i]==max_distance:
    count += 1
    max_index.append(i)

print(min(max_index), max_distance, count)