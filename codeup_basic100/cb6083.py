r, g, b = map(int, input().split())
answer = 0
for i in range(r):
  for j in range(g):
    for k in range(b):
      print("%d %d %d" %(i, j, k))
      answer+=1
print(answer)

# r, g, b = map(int, input().split())
# answer = 0
# for i in range(r):
#   for j in range(g):
#     for k in range(b):
#       print(f'{i} {j} {k}')
#       answer+=1
# print(answer)