import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

arr = list(map(int, sys.stdin.readline().rstrip().split()))

start = 0
end = max(arr)

arr.sort() #일단 정렬
result = 0

while start<=end:
  total = 0 #가져가는 나무 길이
  mid = (start+end)//2

  for i in arr:               
    if i > mid:
      total += i-mid
  
  if total < m:
    end = mid - 1
  else:
    start = mid + 1
    result = mid

print(result)