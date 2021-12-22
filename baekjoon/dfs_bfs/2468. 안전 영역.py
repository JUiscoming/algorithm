# 시간 복잡도: 1초 -> CPU clock 1GHz 기준, N = 10,000 * 100 = 10^6일 때, O(NlogN)인 알고리즘이면 통과.
# 공간 복잡도: 128MB -> int 기준 32M (32 * 10^6)개 변수 = 약 3,200만개 = 즉 1,000만 단위 이상이면 잘못된 알고리즘 설계.
import sys
import copy
from collections import deque

def bfs(array, start, threshold):
    r, c = start
    if array[r][c] <= threshold:
        return 0
    array[r][c] = 0
    queue = deque([(r, c)])
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while queue:
        r, c = queue.popleft()
        
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if array[nr][nc] > threshold:
                queue.append((nr, nc))
                array[nr][nc] = 0
    return 1

input = sys.stdin.readline

array = []

N = int(input())
for _ in range(N):
    array.append(list(map(int, input().rstrip().split())))

max_h, min_h = 1, 100
for i in range(N):
    for j in range(N):
        if array[i][j] > max_h:
            max_h = array[i][j]
        if array[i][j] < min_h:
            min_h = array[i][j]

max_counts = 0
for h in range(min_h-1, max_h):
    array_copy = copy.deepcopy(array)
    counts = 0
    for i in range(N):
        for j in range(N):
            counts += bfs(array_copy, (i,j), h)
    if max_counts < counts:
        max_counts = counts

print(max_counts)