import sys

numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()

for i in numbers:
  print(i, end=' ')