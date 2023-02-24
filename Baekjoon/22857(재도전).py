import sys

n, s = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
dp = [1] * n

for i in range(1, n):
  for j in range(0, i):
    if arr[i]%2 == 0 and arr[j]%2 == 0:
      dp[i] = max(dp[i], dp[j]+1)

    if n-max(dp) == s:
      break

print(max(dp))
  