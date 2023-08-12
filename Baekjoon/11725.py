from collections import deque
import sys
input = sys.stdin.readline

n = int(input().rstrip())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
	x, y = map(int, input().rstrip().split())
	graph[x].append(y)
	graph[y].append(x)

answer = [0] * (n+1)
visited = [False] * (n+1)

"""
오답노트
for i in range(2, n+1):
	print(graph[i][0])
 가 틀린 이유?

=> 간선이 항상 오름차순으로 주어진다는 보장이 없으므로, 연결된 간선을 기준으로 탐색을 진행해야함
"""

def bfs():
	q = deque([1])
	visited[1] = True

	while q:
		v = q.popleft()
 
		for i in graph[v]:
			if not visited[i]:
				q.append(i)
				visited[i] = True
				
				answer[i] = v

bfs()

print('\n'.join(list(map(str, answer[2:]))))