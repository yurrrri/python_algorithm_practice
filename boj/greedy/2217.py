N = int(input())
rope_list = []
for i in range(N):
  rope_list.append(int(input()))

rope_list.sort(reverse=True) # 내림차순 정렬
answer = rope_list[0]

for i in range(N):
  if answer<rope_list[i]*(i+1):
    answer = rope_list[i]*(i+1)

print(answer)