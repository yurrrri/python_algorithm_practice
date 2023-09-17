import sys
import heapq

input = sys.stdin.readline
n, k = map(int, input().rstrip().split()) #k: 가방의 개수
jewels = []
bags = []
for _ in range(n):
  jewels.append(list(map(int, input().rstrip().split())))  # 차례대로 무게, 가격
for _ in range(k):
  bags.append(int(input()))  # 각 가방에 담을 수 있는 최대 무게 --> 가방에는 최대 1개의 보석만 넣을 수 있음

bags.sort()  # 가방 무게와 보석의 무게를 정렬하는 이유는, 가방을 차례대로 탐색하면서 가방에 담길 수 있는 보석 중 가치가 최대인 보석을 골라야하기 때문이다.
jewels.sort()

result = 0
heap = []
"""
힙을 써야 유리한 이유는, n과 k의 범위가 30만인데 이중반복문을 통해 찾아내면 시간초과가 걸림
가방 별로 담을 수 있으면서, 가격을 최대로 해야하므로 O(1)으로 최대값을 찾는 최대힙을 사용하여 문제풀이가 유리
"""

for bag in bags:  # 가방 별로 훔칠 수 있는 보석을 힙을 통해 탐색
  while jewels and jewels[0][0] <= bag:  # 가방에 넣을 수 있는 보석들을 최대힙에 무게 추가
    heapq.heappush(heap, -jewels[0][1])
    heapq.heappop(jewels)
  if heap: # 만약 위 조건을 만족하는 보석이 있다면 (heap에 값이 있음)
    result -= heapq.heappop(heap) # 가치가 최대값을 가지는 보석을 추가함

print(result)