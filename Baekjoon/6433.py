import sys

input = sys.stdin.readline
N = int(input().rstrip())
arr = []

for _ in range(N):
  arr.append(sorted(input().rstrip()))

def backtracking(n, current, goal):
  global visited
  
  if n == goal:
    print(''.join(current))
    return

  for i in visited: #visited 딕셔너리에 들어있는 키값중에,
    if visited[i]: #키값이 0이 아니면
      visited[i] -= 1 #사용했다는 의미로 -1
      backtracking(n+1, current+i, goal)
      visited[i] += 1 #다시 원상복구

for str in arr:
  visited = {}

  # 각 문자열의 문자 개수를 딕셔너리 형태로 저장
  for s in str:
    if s in visited:
      visited[s] += 1
    else:
      visited[s] = 1
      
  backtracking(0, '', len(str))