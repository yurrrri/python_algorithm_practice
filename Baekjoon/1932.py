import sys

n = int(sys.stdin.readline().rstrip())
dp = []

for _ in range(n):
  dp.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(1, n): #두번째 줄부터 확인
  for j in range(i+1):
      if j == 0 :
        dp[i][0] += dp[i-1][0] #위에서만 내려올 수 있음
      elif j == i :
        dp[i][j] += dp[i-1][j-1] #왼쪽 위에서만 내려올 수 있으므로 더함
      else:
        dp[i][j] += max(dp[i-1][j-1], dp[i-1][j]) # 두 화살표중 더 큰 경우 더하기

print(max(dp[n-1]))