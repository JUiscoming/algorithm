# 시간 복잡도: 2초 -> CPU clock 1GHz 기준, N = 1,000^2 = 1,000,000일 때, O(NlogN)인 알고리즘이면 통과.
# 공간 복잡도: 192MB -> int 기준 48M (48 * 10^6)개 변수 = 약 4,800만개 = 즉 1,000만 단위 이상이면 잘못된 알고리즘 설계.
from collections import deque

# 그래프 G(V, E)에서 필수적인 것: 노드간의 연결관계(인접행렬 또는 인접리스트), 방문체크변수
# 그래프 방문 알고리즘은 연결된 노드들을 따라가면서 각 노드에서 작업을 처리해주면 됨.

def bfs(maze, x_max, y_max):
    # 1. 초기조건
    queue = deque([(0, 0, 0)]) # 방문할 노드들이 담긴 리스트
    maze[0][0][0] = 1
    dx = [-1, 1, 0, 0] # 2d, 3d 행렬의 경우 dx, dy 행렬을 미리 만들어 놓으면 편함.
    dy = [0, 0, -1, 1]
    check = lambda x, y, x_max, y_max: False if x < 0 or y < 0 or x >= x_max or y >= y_max else True

    # 2. 최소거리 찾기
    # 노드간의 연결관계는 상하좌우에서 벽 체크만 하면 되기 때문에 추가적인 변수가 필요하지 않음.
    # 방문체크변수는 maze변수와 함께 값을 저장할 수 있음. (방문 시 1 이상의 값을 넣어주면 됨.) 고로 추가적인 변수선언 X

    while queue:
        # 방문 안한 노드만 queue에 넣도록 하자. 넣어줄 때 현재 값에 1 더해서
        x, y, breaked = queue.popleft()
        if x == x_max-1 and y == y_max-1:
            return maze[x][y][breaked]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if check(nx, ny, x_max, y_max): # 맵 안인 경우,
                if maze[nx][ny][breaked] == 0:
                    maze[nx][ny][breaked] = maze[x][y][breaked] + 1
                    queue.append((nx, ny, breaked))
                elif maze[nx][ny][breaked] == 1 and not breaked:
                    maze[nx][ny][1] = maze[x][y][breaked] + 1
                    queue.append((nx, ny, 1))
            
    return -1


maze = []
N, M = map(int, input().split())
for _ in range(N):
    maze.append([[v, v] for v in map(int, input())]) # 문자열도 char 리스트이기 때문에 이렇게!
print(bfs(maze, N, M))
