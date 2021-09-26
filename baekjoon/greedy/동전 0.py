# 시간 복잡도: 1초 -> CPU clock 1GHz 기준, N = 10일 때, O(N^8)인 알고리즘이면 통과.
# 공간 복잡도: 128MB -> int 기준 32M (32 * 10^6)개 변수 = 약 3200만개 = 즉 1,000만 단위 이상이면 잘못된 알고리즘 설계.

def solution(N, K, coin_list):
    count = 0
    for coin in coin_list[::-1]:
        count += (K // coin)
        K %= coin
    return count

N, K = map(int, input().split(' '))
coin_list = []
for _ in range(N):
    coin_list.append(int(input()))

print(solution(N, K, coin_list))
