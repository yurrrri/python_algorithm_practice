import sys, math

N = int(sys.stdin.readline().rstrip())

for _ in range(N):
  x, y = map(int, sys.stdin.readline().rstrip().split())
  print(x*y//(math.gcd(x,y)))