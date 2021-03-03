N = int(input())
times = list(map(int, input().split()))
result = 0
sum = 0

times.sort()
for i in times:
  sum+=i
  result+=sum

print(result)