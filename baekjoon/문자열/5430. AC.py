# 시간 복잡도: 1초 -> CPU clock 1GHz 기준, N = 100,000일 때, O(NlogN) 이하로 설계 (log_2(10) ~ 3.3)
# 공간 복잡도: 256MB -> int 기준 64M (64 * 10^6)개 변수 = 약 6,400만개 , 1,000만 이하로 설계 (int: 4 Byte)

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = input().rstrip()
    N = int(input())
    try:
        array = list(map(int, input().rstrip()[1:-1].split(',')))
    except:
        array = []
    
    left_pop = 0
    right_pop = 0
    left = True

    for c in p:
        if c == 'R':
            left = not(left)
        else:
            if left:
                left_pop += 1
            else:
                right_pop += 1
    # 시작 원소 수보다 제거 원소 수가 많은 경우 에러
    if (left_pop + right_pop) > N:
        print('error')
    else:
        array = array[left_pop:] if not right_pop else array[left_pop: -right_pop]
        if not left:
            array = array[::-1]
        answer = '[' + ','.join(map(str, array)) + ']'
        print(answer)
