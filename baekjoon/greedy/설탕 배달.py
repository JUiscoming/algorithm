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
    