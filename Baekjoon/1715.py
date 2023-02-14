import sys

n = int(sys.stdin.readline().rstrip())
arr = []

for _ in range(n):
  arr.append(int(sys.stdin.readline().rstrip()))
arr.sort()

if n==1:
  print(arr[0])
elif n==2:
  print(arr[0]+arr[1])
else:
  answer = arr[0]+arr[1]
  for i in range(2, n):
    answer += answer + arr[i]

print(answer)