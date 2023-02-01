N, M, K = map(int, input().split())
data = list(map(int, input().split()))

# 오름차순정렬
data = data.sort()

# 합
sum = 0
# 큰수
max = data[-1]
# 두번째로 큰수
second_max = data[-2]

while M >= 1:
    for _ in range(K):
        sum += max
        M = M - 1
    sum += second_max
    M = M - 1

print(sum)
