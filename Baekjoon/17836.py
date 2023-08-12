from collections import deque
import sys
input = sys.stdin.readline

n, m, t = map(int, input().rstrip().split())   # 제한 시간 t
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
board = []
visited = [[0] * m for _ in range(n)]

for _ in range(n):
	board.append(list(map(int, input().rstrip().split())))

def bfs():  # 공주를 구하는 최단거리이므로 BFS 활용
	q = deque([(0, 0)])
	visited[0][0] = 1
	usedGramTime = 10001
	"""
 	오답노트 1. usedGramTime을 0이 아닌 최대값 (10000을 넘어선 값)으로 세팅해야 하는 이유
	오답노트 3 참고
 	"""

	while q:
		x, y = q.popleft()

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if 0<=nx<n and 0<=ny<m and not visited[nx][ny]: 
				if board[nx][ny] == 0:   # 지나갈 수 있는길이라면, visited에 거리 계산
					visited[nx][ny] = visited[x][y] + 1
					q.append((nx, ny))
				elif board[nx][ny] == 2: #그람이 있으면 벽을 무제한 뚫을 수 있으므로 그램의 위치에서 공주까지의 지점 계산
					usedGramTime = visited[x][y] + n-nx-1 + m-ny-1
					"""
		 			오답노트 2. 계산식이 n - nx-1 + m - ny - 1 인 이유
				예를들어 (1, 5)에서 (5, 5)로 이동한다고 했을 때
				1에서 시작하기 때문에 시간을 계산하기 위해서는 -1, 추가적으로 그램을 거쳤을 떄의 값 -1
					"""
					visited[nx][ny] = usedGramTime

	if visited[n-1][m-1] == 0:  # 도착할 수 없다면
		return usedGramTime 
		"""
		오답노트 3. 10001이 아닌(최대값이 아닌) usedGramTime을 리턴해야하는 이유?: 그램을 거쳤지만, 도착지점에 도착할 수 없는 경우에는 그램을 썼을 때의 시간이 곧 공주를 구할 수 있는 시간이며, 만약 도착도 못하고 그램도 거치지 못할 경우에는 공주를 구할 수 있는 방법이 없으므로, usedGramTime이 갱신되지 않은 상태(10001)를 리턴함으로써 아래 t 조건을 넘기게 하기 위함
	  """
	else:  # 도착할 수 있다면,그램을 썼을 때와 그램을 거치지 않을 때의 값 비교 
		return min(usedGramTime, visited[n-1][m-1]-1)  #처음부터 공주를 구하는 데 걸리는 시간을 구하는 것이고, 첫번째 값을 1로 세팅후에 탐색을 시작했으므로 마지막에는 1을 빼야함

result = bfs()
if result > t:  # 최소시간이 t를 넘어선다면 공주를 구할 수 없으므로 Fail
	print("Fail")
else:
	print(result)