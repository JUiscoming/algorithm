# 시간 복잡도: 1초 -> CPU clock 1GHz 기준, N = 100,000일 때, O(NlogN)인 알고리즘이면 통과.
# 공간 복잡도: 256MB -> int 기준 64M (64 * 10^6)개 변수 = 약 6,400만개 변수 (인접행렬: 10^10으로 메모리 넘침, 인접리스트: 2*10^5으로 메모리 안넘침)
import sys
from collections import deque

input = sys.stdin.readline

def bfs(graph, visited, start, N):
    parent_list = [0 for _ in range(N+1)]
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                parent_list[i] = v
                visited[i] = True
                queue.append(i)
    return parent_list

N = int(input())
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for _ in range(N-1):
    idx1, idx2 = map(int, input().split())
    graph[idx1].append(idx2)
    graph[idx2].append(idx1)

parent_list = bfs(graph, visited, 1, N)
for i in range(2, N+1):
    print(parent_list[i])