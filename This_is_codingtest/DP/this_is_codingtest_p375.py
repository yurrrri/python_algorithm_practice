import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
  n, m = map(int, sys.stdin.readline().rstrip().split())
  temp = list(map(int, sys.stdin.readline().rstrip().split())) 
    
  dp = []

  for i in range(n):
    temp_arr = temp[i*m:(i*m)+m]
    dp.append(temp_arr)

  for j in range(1, m):
    for i in range(n):
      if i==0: #가장 위면 왼쪽위로부터 올 수 없음
        left_up = 0
      else:
        left_up = dp[i-1][j-1]

      if i==n-1: #가장 아래라면 오른쪽 아래로부터 올 수 없음
        right_up = 0
      else:
        right_up = dp[i+1][j-1]

      dp[i][j] = dp[i][j] + max(left_up, right_up, dp[i][j-1]) #dp[i][j-1] : 왼쪽에서 오는경우

  result = 0
  for i in range(n):
    result = max(result, dp[i][m-1]) #가장 오른쪽 열에 있는값 중 최대값 찾기
  print(result)