# 시간 복잡도: 1초 -> CPU clock 1GHz 기준, N = 100,000일 때, O(NlogN) 이하로 설계 (log_2(10) ~ 3.3)
# 공간 복잡도: 128MB -> int 기준 32M (32 * 10^6)개 변수 = 약 3,200만개 , 1,000만 이하로 설계 (int: 4 Byte)
# 계획: 정렬 (NlogN) + 이진 탐색 M번 (M*logN) = (M+N)logN

def bin_search(num_list, start, end, target):
    # num_list: 정렬된 상태
    while start <= end:
        mid = (start+end)//2
        
        if num_list[mid] == target:
            return True
        elif num_list[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return False

N = int(input())
num_list = list(map(int, input().split(' ')))
num_list.sort()
M = int(input())
target_list = list(map(int, input().split(' ')))
result_dict = dict() # 동일한 입력은 다시 탐색하지 않도록

for target in target_list:
    if target not in result_dict:
        result_dict[target] = bin_search(num_list, 0, N-1, target)

    if result_dict[target]:
        print('1')
    else:
        print('0')
