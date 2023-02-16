import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
arr = []

for _ in range(n):
  arr.append(int(sys.stdin.readline().rstrip()))

if m==1: #혼자라면 심사 시간의 최소값이 정답
  print(min(arr))
  exit(0)

start = min(arr) #첫번째 사람이 들어갈때 들어가는 가장 최소의 시간
end = max(arr)*m #모든 사람이 가장 오래걸리는 심사대에서 심사할 경우
answer = 0

while start<=end: #이분탐색
  total = 0
  mid = (start+end)//2

  for time in arr:
    total += mid // time #mid분동안 심사한 사람의 수

    #심사한 사람이 m(받아야할 사람)보다 작은 경우 시간을 더 키움
  if total < m:
    start = mid + 1
  #같거나 큰 경우 : 시간을 더 작게함
  else:
    end = mid-1
    answer = mid

print(answer)