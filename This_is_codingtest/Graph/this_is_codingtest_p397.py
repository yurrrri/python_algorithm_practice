n, m = map(int, input().split())
edges = []
parent = [0] * n
total = 0

for i in range(n):
  parent[i] = i

for _ in range(m):
  a, b, cost = map(int, input().split())
  edges.append((cost, a, b))
  total += cost

edges.sort()

def find_parent(parent, x):
  if parent[x] != x:
    return find_parent(parent, parent[x])
  return parent[x]

def union_find(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)

  if a<b:
    parent[b] = a
  else:
    parent[a] = b

min_cost = 0
for edge in edges:
  cost, a, b = edge

  if find_parent(parent, a) != find_parent(parent, b):
    union_find(parent, a, b)
    min_cost += cost

print(min_cost)
print(total)
  