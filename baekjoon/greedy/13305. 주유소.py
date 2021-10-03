# 시간 복잡도: 2초 -> CPU clock 1GHz 기준, N = 100,000일 때, O(NlogN)인 알고리즘이면 통과.
# 공간 복잡도: 512MB -> int 기준 128M (32 * 10^6)개 변수 = 약 3200만개 = 즉 1,000만 단위 이상이면 잘못된 알고리즘 설계.

# 문제 해결: 시작 지점부터 가격을 확인하면서, 현재 위치부터 가격이 더 싸지는 위치까지 갈 수 있도록 기름을 사면 됨.

def solution(N, lengths, prices):
    stop = [(0, prices[0])]
    st = 0

    # 1. 멈출 지점 구하기
    while st < N-1:
        end = st+1
        while end < N-1:
            if prices[st] > prices[end]:
                stop.append((end, prices[end]))
                break
            else:
                end += 1
        st = end
    # 2. 가격 계산
    answer = 0
    for i in range(len(stop)):
        idx_st, price_st = stop[i]
        if i+1 == len(stop):
            idx_end = N
        else:
            idx_end = stop[i+1][0]
        answer += price_st * sum(lengths[idx_st: idx_end])

    return answer


N = int(input()) # 도시의 갯수
lengths = list(map(int, input().split(' '))) # lengths[i]: i-1 번째 지점에서 i 번쨰 지점까지의 거리
prices = list(map(int, input().split(' ')))
print(solution(N, lengths, prices))