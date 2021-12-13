# 시간 복잡도: 2초 -> CPU clock 1GHz 기준, K=10,000일 때, O(K^2)=10^8 이하로 설계 (log_2(10) ~ 3.3)
# 공간 복잡도: 128MB -> int 기준 32M (32 * 10^6)개 변수 = 약 3,200만개 , 1,000만 이하로 설계 (int: 4 Byte)

# K <= 10,000이므로 랜선 길이 다 저장해도 공간복잡도 만족

import sys

def upper_bound(array, N, st, end):
    while st < end:
        counts = 0
        mid = (st+end)//2

        for length in array: # O(N)
            counts += (length//mid)
        if counts >= N:
            st = mid + 1
        else:
            end = mid
    return end

input = sys.stdin.readline

K, N = map(int, input().split(' '))

len_list = []
for _ in range(K):
    len_list.append(int(input()))

len_list.sort() # O(KlogK)

st = 1
end = len_list[-1]+1

print(upper_bound(len_list, N, st, end)-1)