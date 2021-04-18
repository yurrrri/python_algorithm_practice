board = [[0]*19 for _ in range(19)]
n = int(input())
for _ in range(n):
  a, b = map(int, input().split())
  board[a-1][b-1]=1

for i in range(19):
  for j in range(19):
    print(board[i][j], end=' ')
  print()