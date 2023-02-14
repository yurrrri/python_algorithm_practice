import sys
from bisect import bisect_left, bisect_right

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(n):
  if arr[i] == bisect_left(arr, i) or arr[i] == bisect_right(arr, i)-1:
    print(i)
    exit(0)

print(-1)


