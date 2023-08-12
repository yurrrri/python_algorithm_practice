from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
board = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * m for _ in range(n)]
for _ in range(n):
	board.append(list(map(int, input().rstrip())))

def bfs():
	q = deque([(0, 0)])
	visited[0][0] = True

	while q:
		x, y = q.popleft()

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and board[nx][ny] == 1:
				board[nx][ny] = board[x][y] + 1
				visited[nx][ny] = True
				q.append((nx, ny))

bfs()
print(board[n-1][m-1])