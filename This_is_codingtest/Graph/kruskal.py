def find_parent(parent, x): #경로 압축 기법 : 해당 루트 노드가 바로 부모 노드
  if parent[x] != x: #루트 노드가 아니라면 찾을때까지 계속 호출
    parent[x] = find_parent(parent, parent[x])
  return parent[x] #루트 노드가 곧 부모 노드임

def union_parent(parent, a, b): #a, b가 속한 루트 노드 찾기
  a = find_parent(parent, a)
  b = find_parent(parent, b)

  if a < b:
    parent[b] = a
  else:
    parent[a] = b

v, e = map(int, input().split())

edges = [] #그래프 정보 담는 리스트
result = 0 
parent = [0] * (v+1) #부모 노드를 담은 리스트

for i in range(1, v+1): #1. 부모 노드를 자기 자신으로 먼저 초기화
  parent[i] = i

for _ in range(e): #2. 간선, 비용 정보 담기
  a, b, cost = map(int, input().split())
  edges.append((cost, a, b)) #정렬하기 위해 비용을 앞으로

edges.sort() #3. 정렬

for edge in edges: #이미 정렬된 상태임
  cost, a, b = edge

  if find_parent(parent, a) != find_parent(parent, b): #사이클이 아닐경우 둘이 합침
    union_parent(parent, a, b)
    result += cost

print(result)
