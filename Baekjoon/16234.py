from collections import deque
import sys
input = sys.stdin.readline

n, l, r = map(int, input().rstrip().split())  #인접한 나라끼리 l명이상 r명이하면 국경 오픈
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
board = []
visited = []

for _ in range(n):
	board.append(list(map(int, input().rstrip().split())))

def bfs(i, j):
	global board
	global visited
	
	q = deque([(i, j)])
	visited[i][j] = True
	sum = board[i][j]
	union = [(i, j)]

	while q:
		x, y = q.popleft()

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and l<=abs(board[nx][ny]-board[x][y])<=r:   #연합(구역)을 짓기 위해 방문처리: visited[nx][ny] = True
				q.append((nx, ny))
				visited[nx][ny] = True
				sum += board[nx][ny]
				union.append((nx, ny))

	for i, j in union:
		board[i][j] = sum // len(union)  #소수점은 벌

	return len(union)
				
answer = 0
while True:
	visited = [[False] * n for _ in range(n)]
	flag = False

	for i in range(n):
		for j in range(n):
			if not visited[i][j]:
				if bfs(i, j) > 1:  # 1개 이상 -> 인구 이동이 일어났음을 의미
					flag = True

	if not flag:   # 인구 이동이 한번도 일어나지 않았다면 중지
		break

	answer += 1  #일어났다면 answer + 1

print(answer)