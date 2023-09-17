import sys
sys.setrecursionlimit(10**6)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dp = [[0] * n for _ in range(n)]
answer = 0

def dfs(x, y):
  if dp[x][y]: # 이미 방문해서 건널 수 있는 칸의 개수를 아는 상태 --> 기존 dp값 반환
    return dp[x][y]

  dp[x][y] = 1 # 방문처리

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0<=nx<n and 0<=ny<n and board[x][y] < board[nx][ny]:
      dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1) # 이후 탐색했을 때의 경우의 수와 자기 자신의 값을 비교하여 최대값을 비교하여 할당
      
  return dp[x][y]

for i in range(n):   # 모든곳에서 이동 가능 --> 모든 좌표에서 DFS를 시작한다는 의미이므로 모든 좌표에서 시작하는 dfs를 돌리면서 최대값을 찾아냄
  for j in range(n):
    answer = max(answer, dfs(i, j))

print(answer)