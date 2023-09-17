import sys
from collections import defaultdict

input = sys.stdin.readline
n, d, k, c = map(int, input().rstrip().split()) # 접시의 수, 초밥의 가지수, 연속되는 접시의 수, 쿠폰번호
rails = []
for _ in range(n):
  rails.append(int(input()))
dic = defaultdict(int)
dic[c] = 1

start = 0
end = 0
answer = 0

while end < k:
  dic[rails[end]] += 1
  end += 1
end -= 1

while start < n:
  answer = max(len(dic), answer)

  dic[rails[start]] -= 1
  if dic[rails[start]] == 0:
    del dic[rails[start]]
  start += 1

  end = (end+1) % n
  dic[rails[end]] += 1

print(answer)