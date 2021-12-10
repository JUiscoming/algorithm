# 시간 복잡도: 3초 -> CPU clock 1GHz 기준, N = 1,000, M = 1000*999/2 ~ 10^6일 때, O(M) 이하로 설계 (K=10^3, M=10^6, G=10^9)
# 공간 복잡도: 256MB -> int 기준 64M (64 * 10^6)개 변수 = 약 6,400만개 , 1,000만 이하로 설계 (int: 4 Byte)
from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, visited, start):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

N, M = map(int, input().split()) # num of nodes = N, num of vertice = M

graph = [[] for _ in range(N)]
for i in range(M):
    v1, v2 = map(int, input().split())
    graph[v1-1].append(v2-1) # v는 1부터 시작!
    graph[v2-1].append(v1-1) # 무방향 그래프이므로

visited = [False]*N

# 탐색하지 않은 노드에서부터 BFS
answer = 0

for i in range(N):
    if not visited[i]:
        bfs(graph, visited, i)
        answer += 1

print(answer)