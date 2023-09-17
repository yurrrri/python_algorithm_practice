n = int(input())
graph = [[] for _ in range(n+1)]

for a in range(1, n+1):
    b = int(input())
    graph[b].append(a) # 입력값을 인덱스로 하는 이유 --> 27번째줄에서 방문 여부를 처리할 때, 1부터 n까지의 값을 인덱스로 넣게되면 이미 방문해서 사이클여부를 확인한 숫자도 확인하게 되므로 입력받는 숫자를 인덱스로 함

visited = [False] * (n+1) # 노드 방문 여부 확인
result = [] # 결과 집합
def dfs(node, route):
    global result

    route.append(node)
    visited[node] = True
    for i in graph[node]:
        if i not in route:
            dfs(i, route.copy())
        else:# 이미 node가 route에 포함되어있으므로 사이클이 생기는 경우 추가
            result += list(route)
            return
"""
오답노트: route가 아닌 route.copy()를 넘겨야하는 이유
route는 기존 넘겨준 []를 계속 가리키고 있고, route.copy()는 값을 복사한 새로운 리스트를 만들어주는데
route에서 계속 append를 한 값이 있게되면 not in route에서 다른 결과를 가져올 수 있음
"""

for i in range(1, n+1):
    if not visited[i]:
        dfs(i, [])

result.sort()
print(len(result))
for i in result:
    print(i)