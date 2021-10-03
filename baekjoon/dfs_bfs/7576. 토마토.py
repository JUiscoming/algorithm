# 시간 복잡도: 1초 -> CPU clock 1GHz 기준, N = 1,000^2 = 10^6일 때, O(NlogN)인 알고리즘이면 통과.
# 공간 복잡도: 256MB -> int 기준 64M (64 * 10^6)개 변수 = 약 6,400만개 = 즉 천만 단위 이상이면 잘못된 알고리즘 설계.

from collections import deque

# 1: 익은 토마토, 0: 익지 않은 토마토, -1: 토마토가 들어있지 않음
# 1인 토마토에서 bfs를 수행. 
def bfs(matrix, vertices, max_x, max_y):
    queue = deque(vertices)
    max_day = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        x, y, day = queue.popleft()

        for i in range(4): # 4-directions
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= max_x or ny < 0 or ny >= max_y:
                continue
            if matrix[nx][ny] == 0:
                matrix[nx][ny] = 1
                queue.append((nx, ny, day+1))
                if day+1 > max_day:
                    max_day = day+1
    return max_day
            
def solution(matrix, max_x, max_y):
    candidates = [(row, column, 0) for column in range(M) for row in range(N) if matrix[row][column] == 1]
    result = bfs(matrix, candidates, N, M)
    
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0:
                return -1
    
    return result


M, N = map(int, input().split()) #M: 가로 칸의 수(열), N: 세로 칸의 수(행)
box = []
for _ in range(N):
    box.append(list(map(int, input().split())))

print(solution(box, N, M))

            