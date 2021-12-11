# 시간 복잡도: 1초 -> CPU clock 1GHz 기준, N=500,000, M=500,000일 때, O(NlogN) 이하로 설계 (log_2(10) ~ 3.3)
# 공간 복잡도: 256MB -> int 기준 64M (64 * 10^6)개 변수 = 약 6,400만개 , 1,000만 이하로 설계 (int: 4 Byte)
# 계획: 정렬 (NlogN) + M번 탐색 (logN) + 주변 확장 (N) = logN(2N+1) = O(NlogN)

def bin_search(array, st, end, target):
    while st <= end:
        mid = (st+end)//2

        if array[mid] == target:
            return mid, st, end
        elif array[mid] > target:
            end = mid-1
        else:
            st = mid+1
    return -1, -1, -1

def repeat_bs(array, st, end, target):
    # st mid end end+1(정답) mid~end에 있는게 확정
    tgt_idx, st, end = bin_search(array, st, end, target)

    if tgt_idx == -1:
        return 0

    left = tgt_idx
    while True: # left-side
        tmp, _, _ = bin_search(array, st, left-1, target)
        if tmp >= 0:
            left = tmp
        else:
            break
    right = tgt_idx
    while True: # right-side
        tmp, _, _= bin_search(array, right+1, end, target)
        if tmp >= 0:
            right = tmp
        else:
            break
    
    return right - left + 1

N = int(input())
num_list = list(map(int, input().split(' ')))
num_list.sort()
M = int(input())
target_list = list(map(int, input().split(' ')))
result_dict = dict()

answer = []
for target in target_list:
    if target not in result_dict:
        result_dict[target] = repeat_bs(num_list, 0, N-1, target)
    answer.append(str(result_dict[target]))

print(' '.join(answer))