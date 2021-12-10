import sys
from collections import deque
import copy
from itertools import combinations

input = sys.stdin.readline

def count_zero(graph, N, M):
    count = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                count += 1
    return count

def bfs(graph, start, max_r, max_c):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    queue = deque(start)

    co_check = lambda nr, nc, max_r, max_c: not(nr < 0 or nr >= max_r or nc < 0 or nc >= max_c) #coordinates check

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if co_check(nr, nc, max_r, max_c):
                if graph[nr][nc] == 0:
                    queue.append((nr, nc))
                    graph[nr][nc] = 2


# 1. 그래프 입력받기
N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

# 2. 바이러스 위치, 빈 칸 위치 찾기
virus = []
empty = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            virus.append((i, j))
        elif graph[i][j] == 0:
            empty.append((i, j))

# 3. 벽 3개 세우는 조합
wall_candidate_list = list(combinations(empty, 3))

# 4. 각 조합마다 안전구역 개수 세기
max_count = 0
for wall_candidate in wall_candidate_list:
    graph_c = copy.deepcopy(graph)
    for wall_r, wall_c in wall_candidate:
        graph_c[wall_r][wall_c] = 1 # 벽 세움
    bfs(graph_c, virus, N, M)
    count = count_zero(graph_c, N, M)
    if max_count < count:
        max_count = count

print(max_count)