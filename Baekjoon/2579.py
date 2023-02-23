import sys

n = int(sys.stdin.readline().rstrip())
arr = []
dp = [0] * 300

for _ in range(n):
  arr.append(int(sys.stdin.readline().rstrip()))

if n==1:
  print(arr[0])
  exit(0)
elif n==2:
  print(arr[0]+arr[1])
  exit(0)
elif n==3:
  print(max(arr[0]+arr[2], arr[1]+arr[2]))
  exit(0)

#여기서 멈춰주어야 아래를 참조 안함

dp[0] = arr[0]
dp[1] = arr[0] + arr[1]
dp[2] = max(arr[0]+arr[2], arr[1]+arr[2])

#dp[i-3]+arr[i-1]+arr[i] : 3계단 연속 뛸 수 없으므로, i-3에서의 최대값과 그 전, 현재의 값을 더한 값
#dp[i-2]+arr[i] : 3계단 연속 뛸 수 없으므로, i-2에서 건너뛰어서 계산한 값

for i in range(3, n):
  dp[i] = max(dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i])

print(dp[n-1])