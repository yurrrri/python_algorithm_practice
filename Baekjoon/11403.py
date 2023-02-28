import sys

n = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(n):
  arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

for k in range(n):
  for a in range(n):
    for b in range(n):
      if arr[a][b] == 1 or (arr[a][k] == 1 and arr[k][b] == 1):
        arr[a][b] = 1


for a in range(n):
  for b in range(n):
    print(arr[a][b], end= ' ')
  print()