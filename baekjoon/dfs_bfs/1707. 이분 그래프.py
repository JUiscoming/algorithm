# 시간 복잡도: 2초 -> CPU clock 1GHz 기준, V = 20,000일 때, O(NlogN)인 알고리즘이면 통과.
# 공간 복잡도: 256MB -> int 기준 64M (64 * 10^6)개 변수 = 약 6,400만개 = 즉 1,000만 단위 이상이면 잘못된 알고리즘 설계.

from collections import deque
import sys

def bfs(graph, visited, start):
    # 1. 시작조건
    queue = deque([start])
    visited[start] = 1

    while queue:
        v = queue.popleft()
        
        for next_v in graph[v]:
            if not visited[next_v]:
                visited[next_v] = 1 if visited[v] == 2 else 2
                queue.append(next_v)
            elif visited[next_v] == visited[v]:
                return False
    return True


K = int(input())
for test in range(K):
    V, E = map(int, input().split()) # 정점 번호는 1~V
    graph = [[] for _ in range(V)]
    visited = [0 for _ in range(V)] # 0: not visited, 1: color1, 2: color2
    # V의 가능한 범위는 20,000 -> 인접행렬로 구현시 4*10^8개 변수

    for edge in range(E):
        u, v = map(int, sys.stdin.readline().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)

    # 2. 각 노드마다 인접한 애들은 다른 그룹으로 보냄. 보내질 그룹의 애들과 연결관계가 있으면 이분 X
    painted = False
    for i in range(V):
        if not visited[i]:
            painted = bfs(graph, visited, i)
            if not painted:
                print('NO')
                break
    if painted:
        print('YES')
    