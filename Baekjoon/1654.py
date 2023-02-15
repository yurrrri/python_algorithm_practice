import sys

#k : 가지고 있는 랜선의 개수
#n : 필요한 랜선의 개수
k, n = map(int, sys.stdin.readline().rstrip().split())
arr = []

for _ in range(k):
  arr.append(int(sys.stdin.readline().rstrip()))

arr.sort()
start = 1 #start를 1로 하는 이유는 랜선의 길이가 1 이상일 것이기 때문 + mid가 0이 되면 안되므로
end = max(arr)
result = 0

while start<=end:
  total = 0 #랜선의 총 개수
  mid = (start+end)//2

  for i in arr:
    if i >= mid:
      total += i//mid

  if total < n:
    end = mid-1
  else:
    result = mid
    start = mid + 1

print(result)