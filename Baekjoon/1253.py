from itertools import combinations

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

answer = 0
for i in range(n):
  temp = arr[:i] + arr[i+1:]
  start = 0
  end = n-2
  while start < end:
    sum = temp[start] + temp[end]
    if sum == arr[i]:
      answer += 1
      break
    elif sum < arr[i]:
      start += 1
    else:
      end -= 1
print(answer)