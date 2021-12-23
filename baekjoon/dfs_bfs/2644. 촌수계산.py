import sys
from collections import deque

"""
1. graph 형성
2. 그 후 루트 노드부터 내려가면서 각 node에 level값 넣음
3. 촌수 계산
"""
def search(graph, target1, target2):
    level1, level2 = 0, 0
    parent1, parent2 = target1, target2
    parent_hist = []

    while True:
        if parent1 == target2:
            return level1
        if graph[parent1] != 0:
            parent1 = graph[parent1]
            parent_hist.append(parent1)
            level1 += 1
        else:
            break
    
    while True:
        if parent2 == target1:
            return level2
        if graph[parent2] != 0:
            parent2 = graph[parent2]
            level2 += 1
            if parent2 in parent_hist and parent_hist.index(parent2) != -1: # parent2의 (idx+1)번째 부모와 target2의 level2 번째 부모가 겹침.
                return level2 + 1 + parent_hist.index(parent2)
        else:
            break

    return -1

input = sys.stdin.readline
N = int(input())
idx1, idx2 = map(int, input().split())
M = int(input())
graph = [0 for _ in range(N+1)] # 각 사람의 부모는 1명, 부모 인덱스만 가지고 있고 루트노드가 같으면 친척관계 존재.
for _ in range(M):
    p_idx, c_idx = map(int, input().split())
    graph[c_idx] = p_idx

print(search(graph, idx1, idx2))