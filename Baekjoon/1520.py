import sys
input = sys.stdin.readline

m, n = map(int, input().rstrip().split())
board = [list(map(int, input().rstrip().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]  # 거리를 저장할 DP 테이블
#dp[a][b] --> (a, b)에서 (n-1, m-1)까지 갈 수 있는 경로의 수

dx = [0, 0, 1, -1]   # 좌, 우, 상, 하
dy = [-1, 1, 0, 0]

def dfs(x, y):
  if x == m-1 and y == n-1:   # return 1을 해줌으로써 n-1과 m-1에 도달하는 경우의 수 + 1
    return 1

  if dp[x][y] != -1:
    return dp[x][y]

  dp[x][y] = 0 # 방문처리 --> 일단 경로의 수가 0 (이후에 계산하므로)
  
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0<=nx<m and 0<=ny<n and board[nx][ny] < board[x][y]: # 높이가 더 낮은 지점으로만 이동 가능
      dp[x][y] += dfs(nx, ny) #13번째줄에서 return하면서 1과 이전의 dp[nx][ny]값을 차례대로 더해줌
  return dp[x][y]

print(dfs(0, 0))
print(dp)