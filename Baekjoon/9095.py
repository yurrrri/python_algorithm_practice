import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
  a = int(sys.stdin.readline().rstrip())
  dp(a)

def dp(num):
  arr = []
  
