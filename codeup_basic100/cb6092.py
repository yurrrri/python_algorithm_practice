n = int(input())
a_list = list(map(int, input().split()))
b_list = []
for i in range(23):
  b_list.append(0)

for i in range(n):
  b_list[a_list[i]-1]+=1

for i in range(23):
  print(b_list[i], end=' ')