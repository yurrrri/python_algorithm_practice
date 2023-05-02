n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
result = 0

first = data[0]
second = data[1]

count = m//k
result = ((first * k) + second) * count

print(result)