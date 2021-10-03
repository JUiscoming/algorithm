# 시간 복잡도: 1초 -> CPU clock 1GHz 기준, N = 100^2 = 10000일 때, O(N^2)인 알고리즘이면 통과. 하지만 brute-force는 X, 가지치기 필요
# 공간 복잡도: 192MB -> int 기준 48M (48 * 10^6)개 변수 = 약 4,800만개 = 즉 천만 단위 이상이면 잘못된 알고리즘 설계.

from collections import deque

def bfs(graph, start_x, start_y, max_x, max_y):
    # 2d-matrix이고 연결관계는 상하좌우로 정해져 있기 때문에, 간선을 저장할 필요 없음. 그러므로 방문 여부와 길 여부만 저장하면 됨.
    # 이미 방문한 지점의 경우 길이 아니라고 저장하면 됨. 고로 각 지점당 하나의 변수만이 필요.

    queue = deque([(start_x, start_y)]) # x좌표, y좌표
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()
        if graph[x][y] != 0:
            if x == (max_x-1) and y == (max_y-1):
                return graph[x][y]

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= max_x or ny <0 or ny >= max_y:
                    continue
                if graph[nx][ny] == 0:
                    continue
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))

    
N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))
print(bfs(graph, 0, 0, N, M))