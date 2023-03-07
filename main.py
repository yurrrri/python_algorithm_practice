import sys

input = sys.stdin.readline

n = int(input())
x = []
y = []
z = []
edges = []
parent = [0] * n

for i in range(n):
  xdata, ydata, zdata = map(int, input().split())
  x.append((xdata, i))
  y.append((ydata, i))
  z.append((zdata, i))

x.sort()
y.sort()
z.sort()

for i in range(n-1):
  edges.append((x[i+1][0] - x[i][0], x[i][1], x[i+1][1]))
  edges.append((y[i+1][0] - y[i][0], y[i][1], y[i+1][1]))
  edges.append((z[i+1][0] - z[i][0], z[i][1], z[i+1][1]))

edges.sort()

for i in range(n):
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

for edge in edges:
  cost, a, b = edge

  if find_parent(parent, a) != find_parent(parent, b):
    union_find(parent, a, b)
    result += cost

print(result)