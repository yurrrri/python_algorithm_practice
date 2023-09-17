# 참고: https://c4u-rdav.tistory.com/62
import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
        
# 열 수 있는 문을 빈 공간으로 변경
def unlock():
    for i in range(1, h+1):
        for j in range(1, w+1):
            if building[i][j].isupper() and building[i][j].lower() in keys:
                building[i][j] = '.'
                
def bfs():
    res = 0
    visited = [[False] * w for _ in range(h)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < h and 0 <= ny < w and building[nx][ny] != '*' and not visited[nx][ny]:  # 범위 내이고, 벽이 아니라면
                if building[nx][ny] == '.':
                    visited[nx][ny] = True
                    q.append((nx, ny))
                else:
                    # 다음 포지션에 문서가 있으면 res 증가
                    if building[nx][ny] == '$':
                        res += 1
                        visited[nx][ny] = True
                        q.append((nx, ny))
                        building[nx][ny] = '.'  # 문서를 가져갔으므로 빈공간 표시
                    else:
                        # 다음 포지션에 문이 있으면 열 수 있으면 빈 공간으로 만들고 큐에 삽입
                        if building[nx][ny].isupper():
                            if building[nx][ny].lower() in keys:
                                building[nx][ny] = '.'
                                visited[nx][ny] = True
                                q.append((nx, ny))
                        # 다음 포지션에 열쇠가 있으면 히스토리 초기화 --> 지나쳤던 문을 다시 열 수 있으므로 처음부터 다시 탐색하도록 처리
                        elif building[nx][ny].islower():
                            keys.append(building[nx][ny])
                            building[nx][ny] = '.'
                            visited = [[False] * w for _ in range(h)]
                            q = deque()
                            q.append((nx, ny))
    return res

"""
오답노트: 탐색 중 열쇠가 있는 경우에 visited와 q를 초기화해서 처음부터 탐색하는 로직의 이유
열쇠를 획득하면, 기존 visited 처리가 되었거나 탐색 경로중에 지나쳤었던 문을 열면 결과가 달라질 수 있으므로 visited와 q를 초기화하여 탐색을 다시 할 수 있도록 처리함
"""

t = int(input())
for _ in range(t):
    h, w = map(int, input().split())
    building = []
    # 외곽에 빈 공간 추가 --> 아무 빈 공간을 찾아서 들어갈 수 있기 위해서, 외곽을 양옆으로 추가해서 좌표 x=0, y=0에서 시작하면 탐색하면서 자연스럽게 외곽의 들어갈 수 있는 모든 빈공간을 찾아 탐색할 수 있게됨
    building.append(['.'] * (w + 2))
    for _ in range(h):
        building.append(['.'] + list(input().rstrip()) + ['.'])
    building.append(['.'] * (w + 2))
    
    keys = list(input().rstrip())
    unlock() # 먼저 현재 열쇠로 열 수 있는 문이 빌딩에 있다면 먼저 연다음에 BFS 탐색을 시작함
    
    h, w = h+2, w+2  # 외곽 추가때문에 양옆에 1씩 추가되었으므로 탐색 범위가 h+2, w+2로 변경됨
                         
    print(bfs())