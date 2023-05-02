import heapq

n = int(input())
arr = []

for i in range(n):
  input = list(map(int, input().split()))
  for j in range(n):
    heapq.heappush(arr, map(int, input[i][j]))

print(arr[n-1])