# 시간 복잡도: 2초 -> CPU clock 1GHz 기준, N = 50일 때, O(N^4)인 알고리즘이면 통과.
# 공간 복잡도: 128MB -> int 기준 32M (32 * 10^6)개 변수 = 약 3200만개 = 즉 1,000만 단위 이상이면 잘못된 알고리즘 설계.
# sliding window: O(N)

def solution(s):
    answer = 0
    operators = ['+', '-']
    st = 0
    minus = False

    while st < len(s):
        # 처음과 마지막 문자는 숫자이므로 처음에 -가 나오는 것은 신경 안써도 됨.
        # 1. 숫자부분 추출
        end = st
        while end < len(s) and s[end] not in operators:
            end += 1
        num = int(s[st: end])
        # 2. 연산자 결정
        if (st != 0) and s[st-1] == '-':
            minus = True

        # 3. 값 계산
        if not minus:
            answer += num
        else:
            answer -= num
        st = end+1
    
    return answer

s = input()
print(solution(s))