import sys

input = sys.stdin.readline
n = int(input().rstrip())
board = []
for _ in range(n):
  board.append(list(map(int, input().rstrip().split())))
visited = [False] * n #한번 갔던 도시로는 다시 갈 수 없다.
answer = int(1e9)
start = 0

def dfs(arr, sum, depth, cur):  
  global answer
  print(arr, cur)
  
  if cur == start and depth == n: 
        #cur==start: 다시 돌아옴 depth==n: n개의 도시를 거침
    print(cur)
    answer = min(answer, sum)
    return

  # 1 - 3 - 2 - 0 != 1 - 2 - 3 - 0은 다르므로 순열
  for i in range(n):
    if not visited[i] and board[cur][i] != 0: # 방문하지 않은 도시만 방문 가능
      visited[i] = True
      dfs(arr + [board[cur][i]], sum + board[cur][i], depth+1, i)
      visited[i] = False

dfs([], 0, 0, 0)
print(answer)