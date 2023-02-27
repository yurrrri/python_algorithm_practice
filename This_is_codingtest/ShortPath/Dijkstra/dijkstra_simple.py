import sys

n, m = map(int, sys.stdin.readline().rstrip().split()) #노드, 간선의 개수
INF = 1e9 #무한 수
start = int(sys.stdin.readline().rstrip()) #시작 노드
graph = [[] for _ in range(n+1)] #인덱스 1부터 접근하기 위해 인덱스 n으로 끝나는 이중 리스트 만들기
visited = [False] * (n+1) #방문했는지 여부에 대한 리스트
distance = [INF] * (n+1) # 최단거리 테이블

for _ in range(m):
  a, b, c = map(int, sys.stdin.readline().rstrip().split()) #a노드, b노드, a->b 비용
  graph[a].append((b, c))

def small_node():
  min_value = INF

  for i in range(1, n+1):
    if distance[i] < min_value and not visited[i]:
      min_value = distance[i]
      index = i

  return index

def dijkstra(start):
  #시작노드 초기화
  distance[start] = 0
  visited[start] = True

  for i in graph[start]:
    distance[i[0]] = i[1]

  #시작 노드를 제외한 전체 n-1개 노드에 대해서 반복
  for _ in range(n-1):
    now = small_node() #가장 최단거리를 가지는 노드
    visited[now] = True

    for j in graph[now]:
      cost = distance[now] + j[1]
      #현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우 테이블 갱신
      if cost < distance[j[0]]:
        distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1):
  if distance[i] == INF:
    print("INFINITY")
  else:
    print(distance[i])