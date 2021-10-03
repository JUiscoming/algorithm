# 시간 복잡도: 1초 -> CPU clock 1GHz 기준, N = 25^2 = 625일 때, O(N^2)인 알고리즘이면 통과.
# 공간 복잡도: 128MB -> int 기준 32M (32 * 10^6)개 변수 = 약 3,200만개 = 즉 천만 단위 이상이면 잘못된 알고리즘 설계.

# 행렬의 각 요소에서 bfs를 수행한 후, 방문한 노드는 표시! 이미 방문한 그룹에 대해서는 방문을 재차 수행하지 않기 때문에 중복으로 count할 일은 없음.
# 그룹 (sub-graph) 당 하나의 값 count를 계산!

from collections import deque

def bfs(graph, start_x, start_y, max_size):
    # 2d-matrix bfs -> graph에 visited 여부 저장하면 됨.
    queue = deque([(start_x, start_y)])
    count = 0

    if graph[start_x][start_y]:
        while queue:
            x, y = queue.popleft()
            if graph[x][y]:
                graph[x][y] = 0
                count += 1
                if x-1 >= 0:
                    queue.append((x-1, y))
                if x+1 < max_size:
                    queue.append((x+1, y))
                if y-1 >= 0:
                    queue.append((x, y-1))
                if y+1 < max_size:
                    queue.append((x, y+1))
    return count

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

counts = []

for x in range(N):
    for y in range(N):
        count = bfs(graph, x, y, N)
        if count:
            counts.append(count)
counts.sort()

print(len(counts))
for c in counts:
    print(c)