import sys

n, x = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

def first():
  global x
  global n
  
  start = 0 #첫 인덱스
  end = n-1

  while start<=end:
    mid = (start+end)//2

    if (mid==0 or arr[mid-1] < x) and arr[mid] == x:
      return mid

    elif arr[mid] < x:
      start = mid + 1

    else:
      end = mid - 1

  return 0

def last():
  global x
  global n
  
  start = 0 #첫 인덱스
  end = n-1#끝 인덱스

  while start<=end:
    mid = (start+end)//2

    if (mid==n-1 or arr[mid+1] > x) and arr[mid] == x:
      return mid

    elif arr[mid] <= x:
      start = mid + 1

    else:
      end = mid - 1

  return 0

def count_by_value():
  a = first()
  
  if a==0:
    return -1

  b = last()
  
  return b-a+1

print(count_by_value())