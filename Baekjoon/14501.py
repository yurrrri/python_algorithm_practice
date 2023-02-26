import sys

n = int(sys.stdin.readline().rstrip())
t = [0]
p = [0]

for _ in range(n):
  a, b = map(int, sys.stdin.readline().rstrip().split())
  t.append(a)
  p.append(b)

