import sys

number = [int(n) for n in sys.stdin.readline().rstrip()]
number = sorted(number, reverse=True)

for i in number:
  print(i, end='')