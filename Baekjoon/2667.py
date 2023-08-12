from collections import deque
import sys
input = sys.stdin.readline

n = int(input().rstrip())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * n for _ in range(n)]
board = []
for _ in range(n):
	board.append(list(map(int, input().rstrip())))

count = 0
house_count = 0

def dfs(x, y):
	global house_count
	
	visited[x][y] = True
	house_count += 1

	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		
		if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and board[nx][ny] == 1:
			dfs(nx, ny)

answer = []
for i in range(n):
	for j in range(n):
		if board[i][j] == 1 and not visited[i][j]: #1인데 아직 방문처리가 안된 -> 구역 짓기 시작
			house_count = 0
			count += 1
			dfs(i, j)
			answer.append(house_count)

print(count)
print('\n'.join(list(map(str, sorted(answer)))))