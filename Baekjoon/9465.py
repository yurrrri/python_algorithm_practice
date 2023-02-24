import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
  dp = []
  answer = 0
  num = int(sys.stdin.readline().rstrip())
  for _ in range(2):
    dp.append(list(map(int, sys.stdin.readline().rstrip().split())))

  if num==1:
    print(max(dp[0][0], dp[1][0]))
  else:
    #dp: 각 행, 열에서 최대가 될 수 있는 값
    dp[0][1] += dp[1][0]
    dp[1][1] += dp[0][0]

    for i in range(2, num):
      dp[0][i] = dp[0][i] + max(dp[1][i-1], dp[1][i-2])
      dp[1][i] = dp[1][i] + max(dp[0][i-1], dp[0][i-2])
      #여기서 i-2과 비교하는 이유는 스티커를 사용하는 경우의 수중 하나이기 때문 + 그 이전의 값은 이미 정해져있기때문에 비교대상x

    print(max(dp[0][num-1], dp[1][num-1]))