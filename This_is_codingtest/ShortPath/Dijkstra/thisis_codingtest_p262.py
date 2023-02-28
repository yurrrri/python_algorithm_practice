 import sys
import heapq

INF = int(1e9)
graph = [[] for _ in range(n+1)] #연결 정보를 나타내는 그래프
distance = [INF] * (n+1) #거리를 나타내는 리스트
q = [] #우선순위 큐

n, m, start = map(int, sys.stdin.readline().rstrip().split())

for _ in range(m):
  a, b, c = map(int, sys.stdin.readline().rstrip().split())
  graph[a].append((b, c))

def dijkstra(start):
  distance[start] = 0
  heap.heappush(q, (0, start)) #초기화

  while q:
    dist, now = heap.heappop(q)

    if distance[now] < dist: #이미 처리된 것으로 보고 무시함
      continue

    for i in graph[now]: #현재 노드에 연결되어있는 노드 검토
      cost = i[1] + dist 
      if cost < distance[i[0]] #기존 distance보다 작으면
        distance[i[0]] = cost #갱신하고
        heapq.heappush(q, (cost, i[0])) #우선순위 큐에 비용과 해당 노드 추가
   
dijkstra(start)

count = 0
max_distance = 0

for d in distance:
    # 도달할 수 있는 노드인 경우
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)
      
print(count-1, max_distance)