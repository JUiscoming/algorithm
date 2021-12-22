import sys
from collections import deque

input = sys.stdin.readline

def bfs(array, start, array_size):
    r, c = start
    M, N = array_size
    if array[r][c] == False:
        return 0
    area = 1
    queue = deque([(r, c)])
    array[r][c] = False
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if nr<0 or nr>=M or nc<0 or nc>=N:
                continue
            if array[nr][nc] == True:
                area += 1
                array[nr][nc] = False
                queue.append((nr, nc))
    return area

M, N, K = map(int, input().split())

paper = [[True for j in range(N)] for i in range(M)]

# 최대 10^6번 대입연산 -> 1초 안에 가능
for _ in range(K):
    c_init, r_init, c_end, r_end = map(int, input().split())

    for i in range(r_init, r_end):
        for j in range(c_init, c_end):
            paper[i][j] = False

area_list = []

for i in range(M):
    for j in range(N):
        area = bfs(paper, (i,j), (M,N))
        if area > 0:
            area_list.append(str(area))
area_list.sort(key=lambda x: int(x))

print(len(area_list))
print(' '.join(area_list))