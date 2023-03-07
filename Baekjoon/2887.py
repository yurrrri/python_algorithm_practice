import sys

input = sys.stdin.readline

n = int(input())
edges = []

  #이렇게 하면 행성의 개수가 10000까지이므로 메모리 초과 발생함 -> 다른 아이디어가 추가적으로 필요
# for i in range(1, n):
#   for j in range(i+1, n+1):
#     min_cost = min(abs(data[i][0] - data[j][0]), abs(data[i][1]-data[j][0]), abs(data[i][2]-data[j][2]))
#     edges.append((min_cost, i, j))

x = []
y = []
z = []
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