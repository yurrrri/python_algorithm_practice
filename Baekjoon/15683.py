import copy

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
#6은 벽, 0은 빈칸, 1-5는 CCTV의 번호
answer = int(1e9) # 사각 지대의 최소 크기
cctv = []
mode = [
  # cctv가 회전할 때마다 가능한 방향을 0을 동쪽으로 정의 후에 리스트로 저장
  # dx, dy 리스트와 매칭시켜야함
    [],
    [[0], [1], [2], [3]], #1번 cctv
    [[0, 2], [1, 3]], #2번 cctv
    [[0, 1], [1, 2], [2, 3], [0, 3]], #3번 cctv
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]], #4번 cctv
    [[0, 1, 2, 3]], #5번 cctv
]

dx = [0, 1, 0, -1] # 차례대로 동, 서, 남, 북
dy = [1, 0, -1, 0]

for i in range(n): # cctv 번호와 좌표 먼저 세기 (번호별로 mode에서 cctv의 방향을 얻어와야하므로 번호도 같이 저장)
  for j in range(m):
    if 1 <= board[i][j] <= 5:
      cctv.append((board[i][j], i, j))

def countSafeArea(board): # 안전영영역의 크기를 세는 함수
  count = 0
  
  for i in range(n):
    for j in range(m):
      if board[i][j] == 0:
        count += 1

  return count

def fill(board, mode, x, y): # 감시할 수 있는 영역에 마크하기
  for i in mode:
      nx = x
      ny = y
      while True:
          nx += dx[i]
          ny += dy[i]
          if not (0 <= nx < n and 0 <= ny < m): # 범위를 벗어나면 break
              break
          if board[nx][ny] == 6: # 벽을 마주치면 멈춤
              break
          elif board[nx][ny] == 0: #빈공간이면 7을 할당하여 감시 가능한 영역으로 마킹
              board[nx][ny] = 7

def dfs(depth, arr):
    global answer

    if depth == len(cctv) :
        answer = min(countSafeArea(arr), answer)
        return
  
    copied = copy.deepcopy(arr)
    cctv_num, x, y = cctv[depth]
    for i in mode[cctv_num]:
        fill(copied, i, x, y)
        dfs(depth+1, copied)
        copied = copy.deepcopy(arr)
     # 오답노트 1) 반복문을 통해 감시 영역을 채우고 depth + 1 을 하는 이유
    # cctv의 number의 각 방향 + 그 다음 cctv의 각 방향의 조합에 따라 영역이 달라지므로 브루트 포스 형식으로 모든 조합을 생각해야함
    
dfs(0, board)
print(answer)