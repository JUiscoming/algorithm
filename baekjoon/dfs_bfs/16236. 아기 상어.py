import sys
from collections import deque

input = sys.stdin.readline

def bfs(array, start, shark_size, N):
    r, c = start
    dist = 0 # 현재 거리
    queue = deque([(r, c, dist)])
    visited = [[False for j in range(N)] for i in range(N)]
    visited[r][c] = True
    min_dist = 0 # min_dist 1 이상의 값으로 설정되면 그 level까지만 탐색
    candidate_list = []

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while queue:
        r, c, dist = queue.popleft()
        if min_dist !=0 and dist >= min_dist:
            break
        
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if nr<0 or nr>=N or nc<0 or nc>=N or visited[nr][nc]:
                continue
            visited[nr][nc] = True
            if array[nr][nc] == 0 or shark_size == array[nr][nc]:
                queue.append((nr, nc, dist+1))
            elif shark_size > array[nr][nc]:
                candidate_list.append((nr, nc))
                min_dist = dist+1 # 최단거리
    
    if candidate_list:
        candidate_list.sort(key=lambda x: (x[0], x[1]))
        r, c = candidate_list[0]
        array[r][c] = 0
    else:
        candidate_list.append((-1, -1))
    
    return min_dist, candidate_list[0]

# 방문 여부 변수 필요: 상어가 한 번 이동하면 초기화 -> BFS 함수 지역변수로 선언
# 최단거리 계산: 모든 edge의 가중치는 1 -> BFS
# 후보 노드까지의 거리는 queue에 넣을때 함께 저장, BFS는 레벨 순서로 탐색 -> 후보 노드 레벨 까지의 노드만 탐색하면 됨.
# 물고기를 먹은 이후에는 array[nr][nc] = 0

# 상어 포식을 위한 변수
shark_size = 2
eat_count = 2
# 지도를 나타낼 변수
N = int(input())
array = []
for _ in range(N):
    array.append(list(map(int, input().split(' '))))

start = (-1, -1)
for i in range(N):
    for j in range(N):
        if array[i][j] == 9:
            start = (i, j)
            break
    if start[0] != -1:
        break
array[start[0]][start[1]] = 0 # 상어 시작자리 빈칸으로 설정


dist_sum = 0
dist = 1

while dist:
    dist, start = bfs(array, start, shark_size, N)
    if dist != 0:
        eat_count -= 1
        if eat_count == 0:
            shark_size += 1
            eat_count = shark_size
    dist_sum += dist

print(dist_sum)