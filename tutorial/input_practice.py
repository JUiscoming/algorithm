# 1개의 입력값
x = input()

# 공백으로 구분되는 L개의 입력 (이 때 L개의 입력 각각을 변수로 받는 경우)
N, K = input().split(' ') # 문자열 1줄을 받아와서 문자열을 공백을 기준으로 구분.
# 공백으로 구분되는 2개의 입력(iterable)의 각 원소에 함수 적용(map)
N, K = map(int, input().split(' '))

# 공백으로 구분되는 N개의 입력 (하나의 리스트에 받는 경우)
LIST = list(input().split(' '))
# 받아오면서 각 원소에 함수 적용
LIST = list(map(int, input().split(' ')))

# NxM 행렬 (N행 M열 = 각 줄마다 M개의 원소, N개의 줄 존재)
N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))
