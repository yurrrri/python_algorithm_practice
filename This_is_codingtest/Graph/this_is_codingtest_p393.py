n, m = map(int, input().split())

parent = [0] * (n+1)

for i in range(1, n+1):
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

for i in range(n):
  data = list(map(int, input().split()))
  for j in range(n):
    if data[j] == 1:
      union_find(parent, i+1, j+1)

nums = list(map(int, input().split()))
possible = True
for i in range(m-1):
  if find_parent(parent, nums[i]) != find_parent(parent, nums[i+1]):
    possible = False

if possible:
  print("YES")
else:
  print("NO")