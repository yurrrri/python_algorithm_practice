import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())

count = 0
def bfs(start):
  global count
  
	queue = deque([start])
	visit = [False for _ in range(n+1)]
	visit[start] = True

	while queue:
		cur = queue.popleft()

		for nx in graph[cur]:
			if not visit[nx]:
				visit[nx] = True
				count += 1
				queue.append(nx)
        
graph = [[] for _ in range(n+1)]

for _ in range(m):
	a,b = map(int,input().split())
	graph[b].append(a)

maxCnt = 1
ans = []

for i in range(1,n+1):
  count = 0
  bfs(i)
	if cnt > maxCnt:
		maxCnt = cnt
		ans.clear()
		ans.append(i)
	elif cnt == maxCnt:
		ans.append(i)

print(*ans)