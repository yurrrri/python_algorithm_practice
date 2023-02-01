n, m = map(int, input().split())
# 초기값을 0으로 하고 계속 작은값을 대입하면서 큰값을 비교함
result = 0

for i in range(n):
  data = list(map(int, input().split()))
  data_min = min(data)
  result = max(result, data_min)

print(result)
