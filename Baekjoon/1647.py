n, m = map(int, input().split())
edges = []
parent = [0] * (n+1)

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_find(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)

  if a < b:
    parent[b] = a
  else:
    parent[a] = b

for i in range(1, n+1):
  parent[i] = i

for _ in range(m):
  a, b, c = map(int, input().split())
  edges.append((c, a, b)) #정렬하기 위해 cost를 앞으로

edges.sort()

result = 0
last = 0

for edge in edges:
  c, a, b = edge
  if find_parent(parent, a) != find_parent(parent, b):
    union_find(parent, a, b)
    result += c
    last = c

print(result-last)