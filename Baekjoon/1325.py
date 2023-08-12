from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
	x, y = map(int, input().rstrip().split())
	graph[y].append(x) #B를 해킹하면 A를 해킹할 수 있음

answer = []
mx = -1

def bfs(v):
	global n
	global mx
	
	count = 0
	
	q = deque([v])
	visited = [False] * (n+1)
	visited[v] = True

	while q:
		poped = q.popleft()
 
		for i in graph[poped]:
			if not visited[i]:
				q.append(i)
				visited[i] = True
				count += 1

	mx = max(mx, count)
	answer.append((v, count))

for i in range(1, n+1):
	if graph[i]:
		bfs(i)

for v, count in answer:
	if count == mx:
		print(v, end=' ')