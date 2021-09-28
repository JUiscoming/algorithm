# 시간 복잡도: 2초 -> CPU clock 1GHz 기준, N = 1,000일 때, O(N^2)인 알고리즘이면 통과.
# 공간 복잡도: 128MB -> int 기준 32M (32 * 10^6)개 변수 = 약 3200만개 = 즉 1,000만 단위 이상이면 잘못된 알고리즘 설계.

from collections import deque

def dfs(graph, visited, i):
    visited[i] = True
    print(f'{i}', end=' ')
    
    for v in graph[i]:
        if not visited[v]:
            dfs(graph, visited, v)

def bfs(graph, visited, start):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(f'{v}', end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


N, M, V = map(int, input().split()) # N: 정점의 갯수, M: 간선의 갯수, V: 시작 노드 번호

graph = [set() for _ in range(N+1)] # 0번 인덱스는 사용하지 않음.
visited = [False] * (N+1)

for _ in range(M):
    st, end = map(int, input().split())
    graph[st].add(end)
    graph[end].add(st)

for v in range(N+1):
    graph[v] = sorted(list(graph[v]))

dfs(graph, visited[:], V)
print('')
bfs(graph, visited[:], V)