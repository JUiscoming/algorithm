# 시간 복잡도: 2초 -> CPU clock 1GHz 기준, N = 100,000일 때, O(NlogN)인 알고리즘이면 통과.
# 공간 복잡도: 128MB -> int 기준 32M (32 * 10^6)개 변수 = 약 3200만개 = 즉 1,000만 단위 이상이면 잘못된 알고리즘 설계.

def solution(time_list):
    time_list.sort(key=lambda x: (x[1], x[0]))
    count = 0
    end_last = 0
    for (st, end) in time_list:
        if st >= end_last:
            count += 1
            end_last = end
    return count


N = int(input())
time_list = [[0, 0] for _ in range(N)]
for i in range(N):
    time_list[i][0], time_list[i][1] = map(int, input().split(' '))

print(solution(time_list))