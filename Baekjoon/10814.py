import sys

n = int(sys.stdin.readline())
list = []
for _ in range(n):
  list.append(tuple(sys.stdin.readline().split()))

list.sort()
print(list)