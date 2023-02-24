n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n

if n==1:
  print(1)
  exit(0)

for i in range(1, n): #2번째 원소부터 비교
  for j in range(0, i): #i전까지의 모든 원소와 비교하며 점화식 계산
    if arr[j] < arr[i]:
      dp[i] = max(dp[i], dp[j] + 1)


print(max(dp))