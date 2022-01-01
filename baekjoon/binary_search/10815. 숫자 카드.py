# 시간 복잡도: 2초 -> CPU clock 1GHz 기준, N = 5*10^5일 때, O(NlogN) 이하로 설계 (log_2(10) ~ 3.3)
# 공간 복잡도: 256MB -> int 기준 64M (64 * 10^6)개 변수 = 약 6,400만개 , 1,000만 이하로 설계 (int: 4 Byte)
import sys
input = sys.stdin.readline

def bin_search(array, target, st, end):
    while st <= end:
        mid = (st+end)//2

        if target == array[mid]:
            return 1
        elif target > array[mid]:
            st = mid+1
        else:
            end = mid-1
        
    return 0

N = int(input())
card_list = list(map(int, input().split()))
M = int(input())
target_list = list(map(int, input().split()))
card_list.sort()
target_dict = dict()

for i in range(len(target_list)):
    if target_list[i] not in target_dict:
        output = bin_search(card_list, target_list[i], 0, N-1)
        target_dict[target_list[i]] = output
    output = target_dict[target_list[i]]
    target_list[i] = str(output)
print(' '.join(target_list))