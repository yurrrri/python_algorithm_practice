import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
listen = []
see = []

for _ in range(n):
  listen.append(sys.stdin.readline().rstrip())

for _ in range(m):
  see.append(sys.stdin.readline().rstrip())

listen = set(listen)
see = set(see)

listensee = listen & see
print(listensee)