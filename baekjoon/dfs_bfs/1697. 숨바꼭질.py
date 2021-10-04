# +1 / -1 / *2 선택지 셋 중 하나를 고르는 문제.
# depth 계산

# def dfs(N, K):
#     checkpoint_list = [K]
#     checkpoint = K>>1
#     diff_min = max(N-K, K-N)

#     while checkpoint:
#         diff = max(N - checkpoint, checkpoint - N)
#         if diff < diff_min:
#             diff_min = diff
#             checkpoint_list.append(checkpoint)
#             checkpoint >>= 1
#         else:
#             break
    
#     checkpoint_now = checkpoint_list.pop()
#     sec = diff_min

#     while checkpoint_list:
#         checkpoint_next = checkpoint_list.pop()
#         if checkpoint_now << 1 == checkpoint_next:
#             sec += 1
#         else:
#             sec += 2
#         checkpoint_now = checkpoint_next
    
#     return sec
from collections import deque

def bfs(N, K):
    MAX = 10 ** 5
    queue = deque([(N, 0)])
    visited = [False] * (MAX+1)

    while queue:
        pos, sec = queue.popleft()
        if pos == K:
            return sec
        visited[pos] = True

        for n_pos in [pos-1, pos+1, pos*2]:
            if n_pos >= 0 and n_pos <= MAX and not visited[n_pos]:
                queue.append((n_pos, sec+1))


N, K = map(int, input().split())
print(bfs(N, K))