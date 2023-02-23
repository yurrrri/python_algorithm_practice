import sys
import math

n = int(sys.stdin.readline().rstrip())
dp = [0] * 50001

dp[1] = 1 
dp[2] = 2
dp[3] = 3

if n==1 or n==2 or n==3:
  print(dp[n])
  exit(0)

for i in range(4, n+1):
  if math.sqrt(n) == int(math.sqrt(n)):
    dp[i] = min(int(math.sqrt(i)), dp[i-1]+1)
  else:
    dp[i] = dp[i-1] + 1

print(dp[n])
