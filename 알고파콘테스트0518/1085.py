import sys

x, y, w, h = map(int, sys.stdin.readline().rstrip().split())

width = abs(w-x)
height = abs(h-y)

print(min(x, y, width, height))