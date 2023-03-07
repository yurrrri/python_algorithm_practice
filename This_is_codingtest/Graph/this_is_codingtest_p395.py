g = int(input())
p = int(input())

parent = [0] * (g+1)

for i in range(1, g+1):
  parent[i] = i

def find_parent(parent, x):
  if parent[x] != x:
    return find_parent(parent, parent[x])
  return parent[x]

def union_find(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

result = 0
for _ in range(p):
  data = find_parent(parent, int(input()))
  if data == 0:
    break
  union_find(parent, data, data-1) #전 탑승구랑 합침
  result += 1

print(result)