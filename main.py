N, K = map(int, input().split())
coins = list(int(input()) for _ in range(N))
result = 0

for i in range(len(coins)):
  if int(K/coins[i])==0:
    break


# 나누어 떨어지는 가장 큰수부터 나누기
for j in range(i, -1, -1):
  if K==0:
    break

  result+=K//coins[j]
  K = K%coins[j]

print(result)