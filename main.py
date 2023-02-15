import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())

arr.sort()
answer = 0

start = 1 #예산은 1이상
end = max(arr)

while start<=end:
  total = 0
  mid = (start+end) // 2

  for i in arr:
    if i>=mid:
      total += mid
    else:
      total += i

  if total <= m:
    start = mid + 1 #상한선을 더 늘려야함
    answer = mid
  else: #상한선을 더 작게해보고, 최대값이 있는지 확인
    end = mid - 1

print(answer)