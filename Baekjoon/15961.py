import sys
from collections import defaultdict

input = sys.stdin.readline
n, d, k, c = map(int, input().rstrip().split()) # 초밥개수, 연속해서 먹는 초밥의 개수: k, 쿠폰번호 c
rail = []
for _ in range(n):
  rail.append(int(input()))
dic = defaultdict(int)
dic[c] = 1 # 쿠폰을 주는 초밥은 무조건 먹는다고 가정하기

start = 0
end = 0
answer = 0

while end < k:
  dic[rail[end]] += 1
  end += 1
end -= 1  # 위 반복문을 마치고나면 end가 k가 되므로, 인덱스를 위해 1을 감소해줌

while start < n:
  answer = max(len(dic), answer)

  dic[rail[start]] -= 1 # 한칸 이동 --> 기존의 start 위치의 원소 제거 후 
  if dic[rail[start]] == 0:  # 해당 value값이 0일때 key-value 쌍을 지워줘야하는데, 그 이유는 현재 먹은 초밥의 종류를 딕셔너리를 통해 세기 때문에 지워줘야 22번째줄에서 제대로 계산할 수 있음
    del dic[rail[start]]
  start += 1   # start 인덱스 이동

  end = (end+1) % n  # 한칸 이동 --> end 증가시키고 증가시킨 인덱스에 위치한 원소 딕셔너리에 추가
  dic[rail[end]] += 1

print(answer)