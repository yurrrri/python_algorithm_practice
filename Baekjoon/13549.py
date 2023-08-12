from collections import deque
import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
# visited = [False] * 100001

# 1) 0-1 BFS
# 가중치가 낮은 (0) 노드를 큐 맨 앞에 추가 (q.appendleft())
# def bfs():
# 	global visited
	
# 	q = deque([(n, 0)])

# 	while q:
# 		x, dist = q.popleft()

# 		if x == k:
# 			print(dist)
# 			break

# 		if 0<=2*x<=100_000 and not visited[2*x]:
# 			q.appendleft((2*x, dist))
# 			visited[2*x] = True

# 		for nx in [x-1, x+1]:
# 			if 0<=nx<=100_000 and not visited[nx]:
# 				q.append((nx, dist+1))
# 				visited[nx] = True

# bfs()

# 2) 다익스트라
INF = int(1e9)
distance = [INF] * 100001
def dijkstra(start):
	q = []
	heapq.heappush(q, (0, start))
	distance[start] = 0

	while q:
		dist, now = heapq.heappop(q)

		for i in [(1, now+1), (1, now-1), (0, now*2)]:
			if 0<=i[1]<=100_000:
				cost = dist + i[0]
				if cost < distance[i[1]]:
					distance[i[1]] = cost
					heapq.heappush(q, (cost, i[1]))

dijkstra(n)
print(distance[k])