import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
first_arr = list(map(int, sys.stdin.readline().rstrip().split()))
second_arr = list(map(int, sys.stdin.readline().rstrip().split()))

first_arr.sort()
second_arr.sort(reverse=True)

count = 0
for i in range(n):
  if first_arr[i] < second_arr[i]:
    count+=1
    first_arr[i], second_arr[i] = second_arr[i], first_arr[i]

  if count == k:
    break

print(sum(first_arr))

