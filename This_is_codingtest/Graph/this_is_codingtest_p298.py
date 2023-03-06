n, m = map(int, input().split())
parent = [0] * (n+1)
edges = []

for i in range(1, n+1): #처음에 부모 노드 자기 자신으로 초기화
  parent[i] = i

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
  
for _ in range(m):
  oper, a, b = map(int, input().split())
  if oper == 0:
    union_find(parent, a, b)
  else:
    if find_parent(parent, a) == find_parent(parent, b):
      print("YES")
    else:
      print("NO")