import sys

input = sys.stdin.readline
n, x = map(int, input().rstrip().split()) # n, x
visitors = list(map(int, input().rstrip().split()))

if max(visitors) == 0:
  print("SAD")
  exit()

sum = 0
maxValue = 0
prefix_sum = [0] # 인덱스를 위한 껍데기 데이터

for i in visitors:  # 누적합 구하기
  sum += i
  prefix_sum.append(sum)
  
start = 1
end = x

while end <= n:
  maxValue = max(maxValue, prefix_sum[end] - prefix_sum[start-1])
  end += 1
  start += 1

start = 0
end = x-1
sum = prefix_sum[x]
answer = 0

while True:  # 슬라이딩 윈도우
  if sum == maxValue:
    answer += 1
  sum -= visitors[start]
  start += 1
  end += 1
  if end == n:
    break
  sum += visitors[end]

print(maxValue)
print(answer)