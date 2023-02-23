import sys

t = int(sys.stdin.readline().rstrip())
  
def dp(num):
  if num==1:
    return 1
  elif num==2:
    return 2
  elif num==3:
    return 4
    
  arr = [0] * 11 #n은 양수이며 11보다 작다는 조건
  arr[1] = 1
  arr[2] = 2
  arr[3] = 4
  
  for i in range(4, num+1):
    arr[i] = arr[i-1] + arr[i-2] + arr[i-3] #
  
  return arr[num]

for _ in range(t):
  a = int(sys.stdin.readline().rstrip())
  print(dp(a))