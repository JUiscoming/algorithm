# 시간 복잡도: 2초 -> CPU clock 1GHz 기준, N = 5,000일 때, O(N^2)인 알고리즘이면 통과.
# 공간 복잡도: 128MB -> int 기준 32M (32 * 10^6)개 변수 = 약 3200만개 = 즉 1,000만 단위 이상이면 잘못된 알고리즘 설계.

def solution(n):
    count_5, rem_5 = divmod(n, 5)

    # 1. 5의 배수인 경우
    if not rem_5:
        return count_5
    else:
        while count_5 >= 0:
            count_3, rem_3 = divmod(n-(5*count_5), 3)
            if not rem_3:
                return count_3 + count_5
            count_5 -= 1
        return -1

n = int(input())
print(solution(n))
    