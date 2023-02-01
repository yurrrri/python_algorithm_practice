import sys

board = []

for _ in range(5):
  board.append(map(int, sys.stdin.readline().rstrip().split()))

print(board)