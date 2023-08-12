from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
visited = [0] * 100001

def bfs():
	global board
	global visited
	
	q = deque([n])
	visited[n] = 0

	while q:
		x = q.popleft()

		if x == k:    # x가 k일 떄 스탑하는 이유? 처음부터 동생과 수빈이의 위치가 같을 수 있으므로, 이 때를 고려해서 k를 마주칠 때 더이상 진전하지 않아야함
			print(visited[k])
			break

		for nx in [x-1, x+1, 2*x]:
			if 0<=nx<=100_000 and not visited[nx]:
				q.append(nx)
				visited[nx] = visited[x] + 1

bfs()