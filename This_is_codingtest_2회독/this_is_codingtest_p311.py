n = int(input())
arr = list(map(int, input().split()))

arr.sort()
result = 0
len = len(arr)

for i in arr:
  if i<len:
    result +=1
    len -= i

print(result)