import sys

n = int(sys.stdin.readline().rstrip())
list = []
for _ in range(n):
  x, y = sys.stdin.readline().rstrip().split()
  list.append((int(x), y))
result = sorted(list, key=lambda x:x[0])

for i in range(n):
  print(result[i][0], result[i][1])