# 시간 복잡도: 1초 -> CPU clock 1GHz 기준, N = 100일 때, O(N^3)인 알고리즘이면 통과.
# 공간 복잡도: 128MB -> int 기준 32M (32 * 10^6)개 변수 = 약 3200만개 = 즉 1,000만 단위 이상이면 잘못된 알고리즘 설계.
from collections import deque

def bfs(graph, visited, start):
    queue = deque([start])
    visited[start] = True

    while queue:
        i = queue.popleft()
        for v in graph[i]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
    
N = int(input())
graph = [set() for _ in range(N+1)]
visited = [False] * (N+1)
V = int(input())
for _ in range(V):
    i, j = map(int, input().split())
    graph[i].add(j)
    graph[j].add(i)

graph = [sorted(list(v)) for v in graph]

bfs(graph, visited, 1) # 1번 컴퓨터가 바이러스에 걸렸을 때, 웜바이러스가 걸렸다 = visited가 True인 node 계산

print(sum(visited)-1) # 1번 컴퓨터를 통해, 바이러스에 전염된 컴퓨터의 수 (1번 컴퓨터는 제외)