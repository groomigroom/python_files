# 그래프(트리) 구조를 인접 리스트로 표현
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['G', 'H', 'I'],
    'D': ['E', 'F'],
    'E': [],
    'F': [],
    'G': [],
    'H': [],
    'I': ['J'],
    'J': []
}

# 재귀를 이용한 DFS (깊이 우선 탐색) 함수 또 부르고 하는거는 컴퓨터를 망가뜨릴 수 있음.
#재귀 함수는 함수 본인을 호출하는 거라서 stack을 사용하는게 효과적임. (break 없이 달리는 자동차 느낌)
#차라리 stack을 쓰는게 맞음. (메모리 절약을 위해서 고민이 중요함)

def dfs_recursive(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited)

visited = []
dfs_recursive(graph, 'A', visited)

print("DFS 방문 순서:", visited)

#스택으로 직접 구현한 DFS (이 방법을 쓰는게 좋음)


def dfs_stack(graph, start):
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)

            # DFS는 나중에 넣은 것이 먼저 나오므로
            # 왼쪽부터 방문하려면 역순으로 스택에 넣음
            for neighbor in reversed(graph[node]):
                stack.append(neighbor)

    return visited

result = dfs_stack(graph, 'A')
print("DFS 방문 순서:", result)

#너비 우선 탐색 (BFS)

from collections import deque

def bfs(graph, start):
    visited = []              # 방문한 노드 저장
    queue = deque([start])    # 큐 생성, 시작 노드 넣기

    while queue:
        node = queue.popleft()   # 큐의 맨 앞 노드 꺼내기

        if node not in visited:
            visited.append(node)
            for neighbor in graph[node]:
                queue.append(neighbor)

    return visited

result = bfs(graph, 'A')
print("BFS 방문 순서:", result)
