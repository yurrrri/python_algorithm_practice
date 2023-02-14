#라이브러리 사용한 버전
import sys
from bisect import bisect_left, bisect_right

n, x = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

def count_by_range(array, left_value, right_value):
  left = bisect_left(array, left_value) #배열, 찾는 값
  right = bisect_right(array, right_value)

  return right-left

a = count_by_range(arr, x, x)
if a==0:
  print(-1)
else:
  print(a)