# 시간 복잡도: 1초 -> CPU clock 1GHz 기준, N = 2,500일 때, O(N^2)인 알고리즘이면 통과.
# 공간 복잡도: 512MB -> int 기준 128M (128 * 10^6)개 변수 = 약 1억 2,800만개 = 즉 1억 단위 이상이면 잘못된 알고리즘 설계.

# visited를 저장할 변수만 있으면 됨. why? 연결관계는 상하좌우로 다 연결되어 있기 때문.
# 모든 노드에서 dfs를 실행해서, 방문한 적이 없는 경우에만 dfs 종료 후(dfs를 실행한 노드와 연결된 노드에 방문처리) num_group += 1
from collections import deque

T = int(input()) # test case 갯수

for i in range(T):
    M, N, K = map(int, input().split())
    graph = [[True] * N for _ in range(M)] # 방문했거나 배추가 없는 곳

    for j in range(K):
        x, y = map(int, input().split())
        graph[x][y] = False

    def dfs(x, y): # 런타임 에러 (RecursionError)
        if x <= -1 or x >= M or y <= -1 or y >= N:
            return False
        if not graph[x][y]: #not visited
            graph[x][y] = True
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)
            return True
        return False
    
    def bfs(x, y):
        queue = deque([(x, y)])
        is_group = True if not graph[x][y] else False
        
        while queue:
            i, j = queue.popleft()
            if not graph[i][j]:
                graph[i][j] = True
                if i-1 >= 0:
                    queue.append((i-1, j))
                if i+1 < M:
                    queue.append((i+1, j))
                if j-1 >= 0:
                    queue.append((i, j-1))
                if j+1 < N:
                    queue.append((i, j+1))

        return is_group

    result = 0
    for x in range(M):
        for y in range(N):
            if bfs(x, y):
                result += 1
            
    print(result)