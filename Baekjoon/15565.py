import sys
from collections import defaultdict

input = sys.stdin.readline
n, k = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))

dic = defaultdict(int)

start = 0  # 1. start, end 모두 0에서 시작
end = 0

dic[arr[start]] = 1  # 2. start 지점 원소 딕셔너리에 추가
answer = int(1e9)

while end < n:
  if dic[1] < k: # 3. 라이언 인형의 개수가 모자라다면 end 포인터를 이동해야함
    end += 1
    if end >= n:
      break
    dic[arr[end]] += 1
  else:  # 라이언 인형의 개수가 충족한다면, 가장 작은 연속된 집합을 구하기 위해 start를 뒤로 이동
    answer = min(answer, end - start + 1)
    dic[arr[start]] -= 1
    start += 1

if answer == int(1e9):
  print(-1)
else:
  print(answer)