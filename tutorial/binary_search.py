"""
Binary search
선형 탐색은 O(N)의 시간 복잡도를 가짐.
주어진 array가 정렬됐다는 가정하에 이진 탐색을 사용하면 O(logN)의 시간 복잡도로 특정 원소를 찾을 수 있음.
-> 정렬 되지 않은 리스트는 정렬 후 O(NlogN) + 이진 탐색 O(N)을 이용!

유형:
1. 특정 값 찾기
2. lower bound, upper bound 찾기
3. parametric search: 최적화 문제를 결정 문제로 변형하여 binary search를 통해 해결하는 방식.
    조건:
    1)  condition(x) = True를 만족하는 x의 최댓값 혹은 최솟값을 구하는 문제
    2)  parameter x는 discrete set
    3)  argmax_x {condition(x) = True} 에서, condition(x_0) = True라면 x <= x_0인 모든 x에서 condition(x) = True
        또는
        argmin_x {condition(x) = True} 에서, condition(x_0) = True라면 x >= x_0인 모든 x에서 condition(x) = True
        을 만족
"""
def bin_search(array, target, st, end):
    # array: 입력 배열
    # target: 찾고자 하는 값
    # st: 시작 인덱스, end: 끝 인덱스 ; target값과 일치하는 원소를 찾으므로 인덱스의 범위는 [0, len(array)-1]
    # end: 끝 인덱스
    while st <= end:
        mid = (st+end)//2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            st = mid+1
    
    return -1

"""
[1       2      2       3       3       3       4       6       7]
st                  LB(3)                   UB(3)                   end_index=len(array) not len(array)-1
"""

def lower_bound(array, target, st, end):
    # 정렬된 list의 target 이상의 값이 나오는 첫 인덱스 리턴.
    # end는 len(array)로 설정 len(array-1)이 아님.
    while st < end:
        mid = (st+end)//2

        if target <= array[mid]: # 중간값이 target 이상인가?
            end = mid # st ~ mid로 한정
        else:
            st = mid + 1 # mid+1 ~ end로 한정
    return st

def upper_bound(array, target, st, end):
    # 정렬된 list의 target을 초과하는 값이 나오는 첫 인덱스 리턴.
    # end는 len(array)로 설정 len(array-1)이 아님.
    while st < end:
        mid = (st+end)//2

        if target >= array[mid]: # 중간값이 target 이하인가?
            st = mid + 1 # 
        else:
            end = mid
    return end
            

array = [1, 2, 3, 4, 4, 5, 5, 6, 6, 6, 10, 15, 17, 20, 22, 23]
print(f'len(array)={len(array)}')

print(lower_bound(array, 24, 0, len(array)))
print(upper_bound(array, 23, 0, len(array)))