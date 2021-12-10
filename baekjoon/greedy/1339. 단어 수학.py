# 시간 복잡도: 2초 -> CPU clock 1GHz 기준, N = 10일 때, O(N^8) 이하로 설계 (K=10^3, M=10^6, G=10^9)
# 공간 복잡도: 256MB -> int 기준 64M (64 * 10^6)개 변수 = 약 6,400만개 , 1,000만 이하로 설계 (int: 4 Byte)
from collections import defaultdict

weight = defaultdict(int)

N = int(input())

# 1. 각 문자의 weight 계산
for i in range(N):
    s = input()
    d = len(s)

    for idx, ch in enumerate(s):
        weight[ch] += 10**(d-1-idx) # [10을 밑으로 하는 exponent: 10^(d-1-i)]

weight_list = [(k, v) for k, v in weight.items()]
weight_list.sort(key=lambda x: x[1], reverse=True)

answer = 0
for i, (k, v) in enumerate(weight_list):
    answer += (9-i)*v

print(answer)