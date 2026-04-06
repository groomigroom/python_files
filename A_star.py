# ----------------------------------------
# 그래프 구조 정의
# 각 노드에서 갈 수 있는 다음 노드와 이동 비용(cost)을 저장
# 형식:
#   '현재노드': [('다음노드', 비용), ...]
# ----------------------------------------
graph = {
    'X': [('A', 50)],
    'A': [('B', 150), ('F', 300)],
    'B': [('C', 180), ('G1', 270)],
    'C': [],
    'G1': [],

    'F': [('G2', 100), ('J', 140)],
    'G2': [('H', 150), ('K1', 220)],
    'H': [],
    'J': [('K2', 300)],

    'K1': [('I', 400), ('Y', 350)],
    'K2': [],
    'I': [],
    'Y': []
}

# ----------------------------------------
# 휴리스틱 h(n) 정의
# 목표 노드 Y까지 "대략 얼마나 남았는지"를 추정한 값
# 그림에 적힌 마지막 숫자들을 참고하여 작성
# ----------------------------------------
"""
휴리스틱(Heuristics)은 시간이나 정보가 부족하여 합리적·체계적 판단이 어려울 때, 과거 경험이나 직관을 바탕으로 어림짐작하여 빠르게 의사결정을 내리는 '정신적 지름길' 또는 '발견법'을 의미합니다. 정석적인 방법보다 빠르고 효율적이지만, 인지적 편향으로 인해 오류가 발생할 수 있습니다.
"""
heuristic = {
    'X': 800,
    'A': 800,
    'B': 700,
    'C': 650,
    'G1': 500,

    'F': 600,
    'G2': 500,
    'H': 450,
    'J': 400,

    'K1': 300,
    'K2': 300,
    'I': 500,
    'Y': 0
}

import heapq

def a_star(graph, heuristic, start, goal):
    """
    A* 알고리즘 함수

    매개변수:
        graph      : 그래프(인접 리스트)
        heuristic  : 각 노드의 휴리스틱 값 h(n)
        start      : 시작 노드
        goal       : 목표 노드

    반환값:
        path       : 최종 경로 리스트
        total_cost : 최종 경로의 실제 비용 g(goal)
    """

    # -------------------------------------------------
    # 우선순위 큐(open list)
    # 가장 f값이 작은 노드를 먼저 꺼내기 위해 heapq 사용
    #
    # 저장 형식:
    #   (f값, 현재까지 실제비용 g값, 현재노드)
    # -------------------------------------------------
    open_list = []
    heapq.heappush(open_list, (heuristic[start], 0, start))

    # -------------------------------------------------
    # 각 노드까지 도달하는 최소 실제 비용 g(n)을 저장
    # 시작 노드의 g값은 0
    # -------------------------------------------------
    g_cost = {start: 0}

    # -------------------------------------------------
    # 경로 복원을 위한 딕셔너리
    # parent[현재노드] = 이전노드
    # -------------------------------------------------
    parent = {start: None}

    # -------------------------------------------------
    # 이미 최종 처리한 노드 집합(closed set)
    # -------------------------------------------------
    closed_set = set()

    while open_list:
        # f값이 가장 작은 노드를 꺼냄
        current_f, current_g, current_node = heapq.heappop(open_list)

        # 이미 처리한 노드면 건너뜀
        if current_node in closed_set:
            continue

        # 현재 노드를 처리 완료로 표시
        closed_set.add(current_node)

        # 현재 노드 정보 출력
        print(f"[선택] 노드={current_node}, g={current_g}, h={heuristic[current_node]}, f={current_f}")

        # 목표 노드에 도착하면 탐색 종료
        if current_node == goal:
            path = []
            node = goal

            # parent를 따라가며 역으로 경로 복원
            while node is not None:
                path.append(node)
                node = parent[node]

            # 역순으로 뒤집으면 시작 -> 목표 경로가 됨
            path.reverse()
            return path, g_cost[goal]

        # 현재 노드와 연결된 이웃 노드 탐색
        for neighbor, cost in graph[current_node]:
            # 시작점부터 이웃 노드까지의 새 실제 비용 계산
            tentative_g = current_g + cost

            # 아직 방문하지 않았거나,
            # 더 싼 비용으로 neighbor에 도달할 수 있으면 갱신
            if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g
                parent[neighbor] = current_node

                # A*의 핵심: f(n) = g(n) + h(n)
                f_value = tentative_g + heuristic[neighbor]

                # 우선순위 큐에 삽입
                heapq.heappush(open_list, (f_value, tentative_g, neighbor))

                print(
                    f"   -> 후보 추가: {neighbor}, "
                    f"이동비용={cost}, g={tentative_g}, "
                    f"h={heuristic[neighbor]}, f={f_value}"
                )

    # open_list가 빌 때까지 goal을 못 찾으면 실패
    return None, float('inf')



# ----------------------------------------
# 실행
# ----------------------------------------
start_node = 'X'
goal_node = 'Y'

path, total_cost = a_star(graph, heuristic, start_node, goal_node)

print("\n최종 결과")
if path:
    print("최단 경로:", " -> ".join(path))
    print("총 실제 비용:", total_cost)
else:
    print("경로를 찾지 못했습니다.")

"""
제공해주신 A* 알고리즘 코드를 핵심 동작 단위로 한 줄씩 해석해 드릴게요.
## 1. 초기 설정 및 데이터 구조

* import heapq: 우선순위 큐를 구현하기 위해 heapq 모듈을 가져옵니다. (f값이 가장 작은 노드를 자동으로 맨 앞으로 보냅니다.)
* open_list = []: 탐색 대기열(Open List)입니다.
* heapq.heappush(open_list, (heuristic[start], 0, start)): 시작 노드를 큐에 넣습니다. 형식은 (f값, g값, 노드이름)입니다.
* g_cost = {start: 0}: 시작점에서 각 노드까지 실제 이동한 거리($g$)를 저장합니다. 시작점은 0입니다.
* parent = {start: None}: 경로 추적을 위해 "어느 노드에서 왔는지" 기록합니다.
* closed_set = set(): 이미 방문이 끝난 노드를 기록해 중복 탐색을 막습니다.

## 2. 메인 루프 (탐색 과정)

* while open_list:: 탐색할 노드가 남아있는 동안 계속 반복합니다.
* current_f, current_g, current_node = heapq.heappop(open_list): $f(n)$이 가장 작은 노드를 꺼냅니다. (A*의 핵심: 가장 유망한 곳부터 가기)
* if current_node in closed_set: continue: 이미 방문한 노드라면 무시하고 다음으로 넘어갑니다.
* closed_set.add(current_node): 현재 노드를 방문 완료 처리합니다.
* if current_node == goal:: 현재 꺼낸 노드가 목표(Y)라면 탐색을 성공적으로 종료합니다.

## 3. 경로 복원 (목표 도착 시)

* path = [] / node = goal: 빈 리스트를 만들고 역추적을 시작합니다.
* while node is not None: path.append(node); node = parent[node]: parent를 따라 목표에서 시작점까지 거꾸로 올라갑니다.
* path.reverse(): 거꾸로 담긴 경로를 시작 -> 끝 순서로 뒤집습니다.
* return path, g_cost[goal]: 최종 경로와 총 비용을 반환합니다.

## 4. 이웃 노드 확장 (자식 노드 탐색)

* for neighbor, cost in graph[current_node]:: 현재 노드에서 갈 수 있는 다음 노드들을 하나씩 확인합니다.
* tentative_g = current_g + cost: 현재까지 온 거리($g$)에 다음 노드까지의 비용을 더해 새로운 $g$값을 계산합니다.
* if neighbor not in g_cost or tentative_g < g_cost[neighbor]:: 이 노드에 처음 오거나, 기존보다 더 짧은 경로를 발견했다면 정보를 갱신합니다.
* g_cost[neighbor] = tentative_g: 최단 거리($g$) 기록을 업데이트합니다.
* parent[neighbor] = current_node: 어디서 왔는지 부모 노드를 기록합니다.
* f_value = tentative_g + heuristic[neighbor]: $f(n) = g(n) + h(n)$ 공식을 계산합니다.
* heapq.heappush(open_list, (f_value, tentative_g, neighbor)): 계산된 $f$값을 가지고 대기열에 넣습니다.

## 5. 결과 출력

* path, total_cost = a_star(...): 함수를 실행해 경로와 비용을 받습니다.
* if path: print(...): 경로가 있으면 화살표(->)로 이어 출력하고, 없으면 실패 메시지를 띄웁니다.

이 코드는 "가장 짧을 것 같은 길(f값)"을 우선적으로 뒤져보되, 실제로 더 짧은 길이 발견되면 즉시 수정하는 영리한 탐색 방식을 보여줍니다.


"""
