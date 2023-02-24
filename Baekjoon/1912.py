import sys

n = int(sys.stdin.readline().rstrip())
dp = list(map(int, sys.stdin.readline().rstrip().split()))

if n==1: #n이 1이면 첫번째 수가 최대임이 필연적이므로 바로 출력
  print(dp[0])
  exit(0)

#dp: 현재 수까지 있을 때의 최적의 해
#i-1는 그 전까지의 최대의 합이므로 신경쓸 필요가 없음
for i in range(1, n):
  dp[i] = max(dp[i], dp[i-1]+dp[i])

print(max(dp))