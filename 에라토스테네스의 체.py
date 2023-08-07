import math

n = 1000
arr = [True] * (n+1) # 소수인지 여부를 담을 배열 -> 처음엔 다 소수로 가정

for i in range(2, int(math.sqrt(n))+1):
	if arr[i]:
		# i를 제외한 i의 모든 배수 제거
		j = 2
		while (i*j) <= n:
			arr[i*j] = False
			j += 1

for i in range(2, n+1): # 모든 소수 출력
	if arr[i]:
		print(i)