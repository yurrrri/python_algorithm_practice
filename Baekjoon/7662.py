import heapq
import sys

input = sys.stdin.readline
minheap = []
maxheap = []

def sync(arr): #최소힙과 최대힙의 원소를 동일한 상태로 유지해야함
    while arr and not visited[arr[0][1]]:
        heapq.heappop(arr)

t = int(input())
for _ in range(t):
  minheap = []
  maxheap = []
  k = int(input())
  visited = [True] * k
  
  for i in range(k):
    cal, num = input().split()
    num = int(num)
    
    if cal == "I":
      heapq.heappush(minheap,(num,i))
      heapq.heappush(maxheap,(-num,i))
    else:
    ## 원소를 제거함과 동시에 해당하는 숫자의 인덱스를 통해 False로 표시하여 삭제됨을 표시
      if num == -1:
        sync(minheap)
        if minheap:
          visited[heapq.heappop(minheap)[1]] = False
      elif num == 1:
        sync(maxheap)
        if maxheap:
          visited[heapq.heappop(maxheap)[1]] = False
  
  if not (minheap and maxheap):
    print("EMPTY")
  else:
    print(-maxheap[0][0], minheap[0][0])