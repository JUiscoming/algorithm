# 시간 복잡도: 2초 -> CPU clock 1GHz 기준, K=10,000일 때, O(K^2)=10^8 이하로 설계 (log_2(10) ~ 3.3)
# 공간 복잡도: 256MB -> int 기준 64M (64 * 10^6)개 변수 = 약 6,400만개 , 1,000만 이하로 설계 (int: 4 Byte)
"""
초기 상태:
    K개의 랜선 길이 리스트 len_list가 주어짐.
    K<=N인 N에 대해 K개의 랜선을 가지고 N개의 동일한 길이의 랜선을 만들어야 함.
계획:
    1. len_list 정렬 (KlogK)
    2. N개의 동일한 길이의 랜선으로 만들어야 함. -> max_bound는 len_list[0], 랜선은 정수 길이로 잘라야함.
    3. len_est = len_list[0]부터 시작. 
        if K<N: (len_list[-1]이 잘라지는 횟수가 증가하지 않으면 그보다 작은 랜선들은 다 안잘림 그러므로 len_list[-1]을 정수 나눗셈 한 것들을 체크)
            len_est = len_list[-1] // i ; i = ceil(len_list[-1] // len_list[0]) 부터 1씩 증가하면서 검사. 그렇다면 max_len = 2^31-1이므로 32번 안에 구할 수 있음.
            len_list[-1]//i 의 배수 bound를  찾아서 갯수 계산 필요.
        elif K=N:
            answer = len_list[0]
"""

def binary_search_lower(array, end, target):
    st = 0

    while st <= end:
        mid = (st+end)//2
        if target <= array[mid]:
            end = mid
        else:
            st = mid+1
