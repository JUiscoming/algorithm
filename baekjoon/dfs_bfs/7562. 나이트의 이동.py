# 시간 복잡도: 1초 -> CPU clock 1GHz 기준, N = 300^2 = 90,000일 때, O(NlogN)인 알고리즘이면 통과.
# 공간 복잡도: 256MB -> int 기준 64M (64 * 10^6)개 변수 = 약 6,400만개 = 즉 1,000만 단위 이상이면 잘못된 알고리즘 설계.
from collections import deque

def bfs(board, x_start, y_start, x_end, y_end, MAX):
    # 1. 시작조건
    queue = deque([(x_start, y_start, 0)])
    board[x_start][y_start] = True
    dx = [-2, -1, 1, 2, -2, -1, 1, 2]
    dy = [-1, -2, -2, -1, 1, 2, 2, 1]
    check = lambda x, y, MAX: False if x < 0 or y < 0 or x >= MAX or y >= MAX else True

    # 2. bfs
    while queue:
        x, y, count = queue.popleft()
        if x == x_end and y == y_end:
            return count
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if check(nx, ny, MAX) and not board[nx][ny]:
                board[nx][ny] = True
                queue.append((nx, ny, count+1))


T = int(input())
for test_case in range(T): # 각 test case마다
    L = int(input())
    x_start, y_start = map(int, input().split())
    x_end, y_end = map(int, input().split())

    board = [[False]*L for _ in range(L)]
    print(bfs(board, x_start, y_start, x_end, y_end, L))
    

