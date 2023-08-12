from collections import Counter
n = int(input())

for _ in range(n):
	count = Counter(list(input().replace(' ', ''))).most_common()
	count.sort(key=lambda x:x[1], reverse=True)

	if len(count) > 1:
		if count[0][1] == count[1][1]:
			print("?")
		else:
			print(count[0][0])
	else:
		print(count[0][0])