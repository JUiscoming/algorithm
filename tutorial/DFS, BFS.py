from collections import deque

# graph와 visited는 탐색 알고리즘 (bfs, dfs)가 끝나도 유지될 수 있도록 파라미터로 제공

"""
N개의 노드로 구성된 그래프 탐색 알고리즘 시 필요한 준비물
입력
1. graph
    노드간의 연결관계
    - 인접 리스트: 인접 리스트 안에는 N개의 리스트가 존재하고, i번째 리스트는 i번째 노드와 연결된 노드의 인덱스가 들어 있음. (edge에 방향성이 없다면 인접 리스트 작성시 양방향으로 원소 삽입)
        graph[i].append[j] & graph[j].append[i]
    - 인접행렬: N x N 행렬로, (i,j) entry에는 연결여부가 들어 있음.
    - 만약 그래프가 matrix 형태라면, 연결관계는 상하좌우로 알고 있으므로 노드간의 연결관계 변수가 필요 없음.
    - 그래프가 matrix 형태라면, 주변 노드 탐색 여부가 현재 노드 값과 주변 노드 값들의 연산으로 결정될 수 있음.

    각 노드의 value (선택):
    - 각 노드는 어떠한 값을 가질 수 있음.
2. start (탐색 시작 변수)
3. visited (방문처리 변수)
    - 각 노드에 대해서 한 번씩만 처리하기 위해 필요한 변수
----------------------------------------------------------------
알고리즘
    탐색 시작점 노드들은 stack 또는 queue에 들어가 있음.
    DFS는 stack에서 빼면서 방문처리
    BFS는 queue에 넣으면서 방문처리
    주변 노드 방문 여부를 잘 정하는 것이 핵심(노드의 값을 비교해서 방문 여부를 정한다던지 또는 단순한 문제에서는 단순히 연결만 되있으면 방문)

DFS_recursive
1. 탐색 시작 노드 방문 처리 (pop 된 상태라고 생각; 실제로는 스택 메모리에 있음)
2. 시작 노드의 인접 노드중 방문 하지 않은 노드들에 대해서 DFS_recursive 수행

DFS_iterative
시작 상태: stack = [start]
1. 스택 최상위 노드 pop & 방문처리 후, 인접 노드중 방문하지 않은 노드 append 
2. 1 반복

BFS (iterative)
시작 상태: queue = deque([start]) & 시작노드 방문처리
1. 큐 popleft 후, 인접 노드 중 방문하지 않은 노드 append & 방문처리
2. 1 반복
""" 
def dfs_rec(graph, start, visited):
    visited[start] = True
    print(f'{start}', end=' ')

    for v in graph[start]:
        if not visited[v]:
            dfs_rec(graph, v, visited)

def dfs_iter(graph, start, visited):
    stack = [start]

    while stack:
        top = stack.pop()
        visited[top] = True
        print(f'{top}', end=' ')
        for v in graph[top]:
            if not visited[v] and v not in stack: # 아직 stack에 방문처리되지 않은 노드들이 있는데 또 stack에 넣으면 안되므로
                stack.append(v)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(f'{v}', end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

N = 9
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visited = [False] * N

print('\ndfs_recursive')
dfs_rec(graph, 1, visited)

N = 9
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visited = [False] * N

print('\ndfs_iteration')
dfs_iter(graph, 1, visited)

N = 9
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visited = [False] * N

print('\nbfs')
bfs(graph, 1, visited)