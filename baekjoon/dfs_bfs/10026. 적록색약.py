# 시간 복잡도: 1초 -> CPU clock 1GHz 기준, N = 10,000 = 10^4일 때, O(N^2)인 알고리즘이면 통과.
# 공간 복잡도: 128MB -> int 기준 32M (32 * 10^6)개 변수 = 약 3,200만개 = 즉 1,000만 단위 이상이면 잘못된 알고리즘 설계.
import sys
import copy
from collections import deque
input = sys.stdin.readline

N = int(input())

array = []
for _ in range(N):
    array.append(list(input().rstrip()))

array_blind = [['R' if entry != 'B' else 'B' for entry in row] for row in array]

def bfs(array, start):
    r, c = start
    if array[r][c] == 'X':
        return 0
    color = array[r][c]
    array[r][c] = 'X'
    queue = deque([(r, c)])

    while queue:
        r, c = queue.popleft()
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= N or array[nr][nc] == 'X':
                continue
            if array[nr][nc] == color:
                array[nr][nc] = 'X'
                queue.append((nr, nc))
    return 1

counts = [0, 0]
for blind in range(2):
    for i in range(N):
        for j in range(N):
            counts[blind] += bfs(array_blind, (i, j)) if blind else bfs(array, (i, j))
print(f'{counts[0]} {counts[1]}')