from collections import deque

def dfs(graph, v, visited):
    # graph: 인접 리스트
    # v: 탐색 노드 index
    # visited: 방문 처리

    # 현재 노드를 방문 처리 -> 종료 조건 존재
    visited[v] = True 
    print(f'{v}', end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    # graph: 인접 리스트
    # start: 시작 노드 index
    # visited: 방문 처리

    # 1. 시작노드 처리
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

print('DFS:')
dfs(graph, 1, visited)

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

print('\nBFS:')
bfs(graph, 1, visited)