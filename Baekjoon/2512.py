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

  if total <= m: #m이하에서 생각해봐야하므로
    start = mid + 1 #상한선을 더 늘려야함 (예산보다 작으니까)
    answer = mid
  else: #예산보다 크면 안되므로 상한선을 더 낮춤
    end = mid - 1

print(answer)