from collections import deque
import copy

v = int(input())
graph = [[] for _ in range(v+1)]
indegree = [0] * (v+1)
time = [0]  * (v+1)

for i in range(1, v+1):
  data = list(map(int, input().split()))
  time[i] = data[0] #각 강의를 듣는 데에 걸리는 시간
  for x in data[1:-1]: #마지막 전까지
    indegree[i] += 1
    graph[x].append(i)

def topology_sort():
  result = copy.deepcopy(time)
  q = deque()

  for i in range(1, v+1):
    if indegree[i] == 0:
      q.append(i)

  while q:
    now = q.popleft()

    for i in graph[now]:
      result[i] = max(result[i], result[now] + time[i])
      indegree[i] -= 1
      if indegree[i] == 0:
        q.append(i)

  for i in range(1, v+1):
    print(result[i])

topology_sort()