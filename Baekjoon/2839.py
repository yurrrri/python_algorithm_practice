n = int(input())
dp = [-1] * 5001 #N이 3부터 5000까지이기 때문          

#bottom up 방식
dp[3] = dp[5] = 1

for i in range(6, n+1): #6부터 시작 
  if dp[i-3] != -1:
    dp[i] = dp[i-3] + 1
  elif dp[i-5] != -1:
    dp[i] = dp[i-5] + 1

  if dp[i-3]>-1 and dp[i-5]>-1:
    dp[i] = min(dp[i], dp[i-5] + dp[i-3]+1)

print(dp[n])