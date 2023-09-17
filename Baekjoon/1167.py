from collections import deque
import sys

input = sys.stdin.readline

n = int(input().rstrip())
graph = [[] for _ in range(n+1)]
first = 0

for _ in range(n):
  read = list(map(int, input().rstrip().split()))
  for idx in range(1, len(read)-2, 2):
    graph[read[0]].append((read[idx], read[idx+1]))

answer = 0
def bfs(start, n):
  visited = [0] * n # 거리는 자연수이므로 0으로 초기화 후 not visited로 해도 방문처리 판단 가능
  visited[start] = 1 # 방문처리 위해 1로 초기화
  q = deque([start])
  maxValue = (0, 0) # 정점, 거리

  while q:
    node = q.popleft()

    for n, d in graph[node]:
      if not visited[n]:
        visited[n] = visited[node] + d
        q.append(n)
        if visited[n] > maxValue[1]: # 임의의 점에서 연결된 노드 중 최대값 찾기 (가장 먼 길이)
          maxValue = (n, visited[n])

  return maxValue

node, dist = bfs(1, n+1)
node, dist = bfs(node, n+1)

"""
트리 지름
1) 임의의 노드에서 가장 길이가 먼 노드 찾기
2) 그 노드에서 다시 가장 길이가 먼 길이를 찾으면 해당 길이가 트리의 지름
"""
print(dist-1)