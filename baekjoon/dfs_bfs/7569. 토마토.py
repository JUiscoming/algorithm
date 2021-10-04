from collections import deque

# 임의의 익지않은 토마토가 익은 토마토들에게 영향을 받을 수 있는데, 그 중 최소 거리를 계산하자.
# root node를 익은 토마토들로 설정 후, bfs를 수행! 각 노드마다 방문 시 day를 함께 저장하면 풀 수 있음.

def bfs(box, start_vertices, H, R, C):
    Q = deque(start_vertices) # vertex: (z, x, y, day)
    max_day = 0
    # 상하좌우앞뒤
    dx = [0, 0, -1, 1, 0, 0]
    dy = [0, 0, 0, 0, -1, 1]
    dz = [-1, 1, 0, 0, 0, 0]
    condition = lambda z, x, y, max_z, max_x, max_y: z<0 or x<0 or y<0 or z>=max_z or x>=max_x or y>=max_y

    while Q:
        z, x, y, day = Q.popleft()
        
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            
            if condition(nz, nx, ny, H, R, C):
                continue
            if box[nz][nx][ny] == 0:
                Q.append((nz, nx, ny, day+1))
                box[nz][nx][ny] = day+1
                if max_day < day+1:
                    max_day = day+1
        
    return max_day

def solution(box, H, R, C):
    start_vertices = []

    for h in range(H):
        for r in range(R):
            for c in range(C):
                if box[h][r][c] == 1:
                    start_vertices.append((h, r, c, 0))
    
    result = bfs(box, start_vertices, H, R, C)

    for h in range(H):
        for r in range(R):
            for c in range(C):
                if box[h][r][c] == 0:
                    return -1
    return result


# 3D-box
C, R, H = map(int, input().split())
box = []
for level in range(H):
    layer = []
    for row in range(R):
        layer.append(list(map(int, input().split())))
    box.append(layer)

print(solution(box, H, R, C))