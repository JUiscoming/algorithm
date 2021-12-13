# 시간 복잡도: 2초 -> CPU clock 1GHz 기준, N=100,000일 때, O(NlogN) 이하로 설계 (log_2(10) ~ 3.3)
# 공간 복잡도: 128MB -> int 기준 32M (32 * 10^6)개 변수 = 약 3,200만개 , 1,000만 이하로 설계 (int: 4 Byte)


import sys

input = sys.stdin.readline

N, C = map(int, input().split(' '))

house_list = []
for _ in range(N):
    house_list.append(int(input()))
house_list.sort() # O(NlogN)

# maximize distance btw. 거리 최소인 두 집

def upper_bound(house_list, N, C, st, end):
    while st < end:
        prev_pos = house_list[0]
        mid = (st+end)//2
        count = 1

        for i in range(1, N): # O(NlogN)
            if (house_list[i] - prev_pos) >= mid:
                prev_pos = house_list[i]
                count += 1
            if count == C:
                break
        if count >= C:
            st = mid + 1
        else:
            end = mid
    return end

print(upper_bound(house_list, N, C, 1, house_list[-1]-house_list[0]+1)-1)