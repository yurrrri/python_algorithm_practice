import sys
# 냅색 알고리즘
input = sys.stdin.readline
n, m = map(int, input().rstrip().split()) # m: m바이트 이상의 메모리를 추가로 확보해야함
memory = [0] + list(map(int, input().rstrip().split()))
cost = [0] + list(map(int, input().rstrip().split()))
length = sum(cost) + 1  # 
dp = [[0] * length for _ in range(n+1)]  # dp테이블: 앱을 비활성화함에 따라 가질 수 있는 메모리의 최대값
answer = int(1e9)

for i in range(1, n+1): # i: 물건의 개수
  for j in range(1, sum(cost)+1):  # j: 비활성화했을 때의 비용
    ci, mi = cost[i], memory[i]

    if j >= ci: #j가 현재 비용보다 크거나 같으면, ci를 넣는게 더 최소 비용으로 가치를 낼 수 있으므로 뺀 경우와 이전의 값을 비교해야함
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-ci] + mi) # 이전의 값과 현재 가방에서 이전의 값을 빼고 ci를 넣었을 때의 가치 비교
    else:  # 비교할 필요가 없으므로 이전의 값 가져옴
      dp[i][j] = dp[i-1][j]

    if dp[i][j] >= m: # 만약에 현재의 값이 m보다 크거나 같으면 최소의 비용 비교
      answer = min(answer, j)
        
print(answer)