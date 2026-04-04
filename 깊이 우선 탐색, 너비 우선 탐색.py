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

"""
제공해주신 코드를 블록별로 나누어 한 줄씩 핵심 기능을 설명해 드릴게요.
## 1. 그래프 구조 정의

graph = {
    'A': ['B', 'C'],        # A는 B, C와 연결됨
    'B': ['D'],             # B는 D와 연결됨
    'C': ['G', 'H', 'I'],   # C는 G, H, I와 연결됨
    'D': ['E', 'F'],        # D는 E, F와 연결됨
    'E': [],                # 자식 없음 (리프 노드)
    'F': [],
    'G': [],
    'H': [],
    'I': ['J'],             # I는 J와 연결됨
    'J': []
}


* 해석: 딕셔너리 자료형을 사용해 각 노드(Key)와 연결된 인접 노드들(Value)을 리스트로 표현한 인접 리스트입니다.

------------------------------
## 2. 재귀를 이용한 DFS (dfs_recursive)

def dfs_recursive(graph, node, visited): # 함수 정의 (그래프, 현재 노드, 방문 목록)
    if node not in visited:              # 현재 노드를 아직 방문하지 않았다면
        visited.append(node)             # 방문 목록에 현재 노드 추가
        for neighbor in graph[node]:     # 현재 노드와 연결된 이웃 노드들을 하나씩 확인
            dfs_recursive(graph, neighbor, visited) # 이웃 노드를 대상으로 함수를 다시 호출(재귀)


* 해석: 함수가 자기 자신을 계속 호출하며 가장 깊은 곳까지 들어갔다가, 더 갈 곳이 없으면 되돌아오며 탐색합니다.

------------------------------
## 3. 스택을 이용한 DFS (dfs_stack)

def dfs_stack(graph, start):             # 함수 정의 (그래프, 시작 노드)
    visited = []                         # 방문한 노드들을 담을 빈 리스트 생성
    stack = [start]                      # 탐색할 노드를 담을 스택 생성 (시작 노드 포함)

    while stack:                         # 스택에 탐색할 노드가 남아있는 동안 반복
        node = stack.pop()               # 스택의 맨 위(마지막) 요소를 꺼냄

        if node not in visited:          # 꺼낸 노드가 아직 방문 전이라면
            visited.append(node)         # 방문 목록에 추가

            # 왼쪽부터 방문하기 위해 자식들을 역순으로 스택에 넣음
            for neighbor in reversed(graph[node]): 
                stack.append(neighbor)   # 스택에 이웃 노드들을 쌓음

    return visited                       # 최종 방문 순서 반환


* 해석: 재귀 대신 LIFO(후입선출) 구조인 리스트(스택)를 활용해 직접 탐색 순서를 제어합니다.

------------------------------
## 4. 큐를 이용한 BFS (bfs)

from collections import deque            # 효율적인 큐 사용을 위해 deque 모듈 로드
def bfs(graph, start):                   # 함수 정의 (그래프, 시작 노드)
    visited = []                         # 방문한 노드들을 담을 빈 리스트 생성
    queue = deque([start])               # 시작 노드를 담은 큐 생성

    while queue:                         # 큐에 탐색할 노드가 남아있는 동안 반복
        node = queue.popleft()           # 큐의 맨 앞(가장 먼저 들어온) 요소를 꺼냄

        if node not in visited:          # 꺼낸 노드가 아직 방문 전이라면
            visited.append(node)         # 방문 목록에 추가
            for neighbor in graph[node]: # 이웃 노드들을 확인
                queue.append(neighbor)   # 큐의 뒤쪽에 이웃 노드들을 추가

    return visited                       # 최종 방문 순서 반환


* 해석: FIFO(선입선출) 구조인 큐를 활용해 시작점에서 가까운 노드부터 차례대로(너비 방향으로) 탐색합니다.

------------------------------
## 요약하자면:

   1. 재귀 DFS: 시스템 스택을 빌려 쓰는 방식 (코드가 짧음).
   2. 스택 DFS: 내가 직접 스택 메모리를 관리하는 방식 (안정적임).
   3. 큐 BFS: 옆으로 퍼지며 찾는 방식 (최단 경로 찾기에 유리).

코드의 각 줄이 수행하는 역할이 이제 명확해지셨나요? 이 코드의 결과값(방문 순서)이 왜 그렇게 나오는지 궁금하시다면 더 자세히 설명해 드릴 수 있습니다.

"""
