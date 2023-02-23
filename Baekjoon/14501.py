import sys

n = int(sys.stdin.readline().rstrip())
dp = []

for _ in range(n):
  dp.append(list(map(int, sys.stdin.readline().rstrip().split())))

