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
  if int(math.sqrt(i)) == math.sqrt(i): #해당 수 자체가 제곱수라면 최소가 1
    dp[i] = 1
  else: #아니라면 n이 포함하고 있는 제곱수의 합의 조합으로 나올 수 있는지 판단
    minValue = 1e9
    for j in range(1, int(math.sqrt(i)) + 1):
        minValue = min(minValue, dp[i - j**2])
    dp[i] = minValue+1
      
print(dp[n])