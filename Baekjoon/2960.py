import math

n, k = map(int, input().split())

arr = [True] * (n+1) # 처음에는 다 소수
count = 0

for i in range(2, int(math.sqrt(n))+1):
	if arr[i]:
		j = 2
		while i*j <= n:
			arr[i*j] = False

			if count == k:
				print(i*j)
				exit(0)
			j += 1
			

