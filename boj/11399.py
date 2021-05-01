import sys

n = int(sys.stdin.readline())
times = list(map(int, sys.stdin.readline().split()))
result = 0
sum = 0

times.sort()
for i in times:
  sum+=i
  result+=sum

print(result)