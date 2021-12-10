from collections import deque
import sys

input = sys.stdin.readline

def bfs(graph, start, max_rc):
    if graph[start[0]][start[1]] == 0:
        return 0
    queue = deque([start])
    graph[start[0]][start[1]] = 0

    dr = [-1, -1, -1, 0, 0, 1, 1, 1]
    dc = [-1, 0, 1, -1, 1, -1, 0, 1]
    co_check = lambda nr, nc, max_r, max_c: not(nr<0 or nr>=max_r or nc<0 or nc>=max_c)

    while queue:
        r, c = queue.popleft()
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if co_check(nr, nc, max_rc[0], max_rc[1]):
                if graph[nr][nc] == 1:
                    queue.append((nr, nc))
                    graph[nr][nc] = 0
    return 1

# 1. 입력 받아오기 (1: 땅, 0: 바다)
graph_list = []
max_rc_list = []
while True:
    C, R = map(int, input().split())
    if C == 0 and R == 0:
        break

    max_rc_list.append((R, C))
    graph = []
    for _ in range(R):
        graph.append(list(map(int, input().split())))
    graph_list.append(graph)

# 2. 각 그래프에서 섬 갯수 구하기 (BFS 횟수 == 섬 갯수)
for graph, max_rc in zip(graph_list, max_rc_list):
    count = 0
    for r in range(max_rc[0]):
        for c in range(max_rc[1]):
            count += bfs(graph, (r, c), max_rc)
    print(count)