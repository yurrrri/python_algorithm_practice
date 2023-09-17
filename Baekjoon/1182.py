import sys

input = sys.stdin.readline
n, s = map(int, input().rstrip().split())
board = list(map(int, input().rstrip().split()))
answer = 0

def dfs(idx, sum):
  global answer
  
  if idx > 0 and sum == s:
    answer += 1

  """
  여기서 return을 넣지 않는 이유?
  [-1, 1, 0] 같은 케이스를 커버하지 못함. 여기서 return을 넣으면 -1, 1 인 상태에서 이전 상태로 돌아가게 됨
  현재 상황에서 돌아가야할지 돌아가지 않아야할지를 고민해야함
  """

  for i in range(idx, n):
    dfs(i+1, sum + board[i])

dfs(0, 0)
print(answer)