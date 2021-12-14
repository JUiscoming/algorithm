# 시간 복잡도: 1초 -> CPU clock 1GHz 기준, N=10,000일 때, O(K^2)=10^8 이하로 설계 (log_2(10) ~ 3.3)
# 공간 복잡도: 128MB -> int 기준 32M (32 * 10^6)개 변수 = 약 3,200만개 , 1,000만 이하로 설계 (int: 4 Byte)
# 배열 원소의 condition 확인시 끝 원소나 시작원소 체크 중요!
import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    book = []
    for i in range(n):
        book.append(input().rstrip())
    
    book.sort() # O(NlogN)
    
    consistency = 'YES'
    for idx in range(len(book)-1):
        if len(book[idx]) >= len(book[idx+1]):
            continue
        if book[idx+1][:len(book[idx])] == book[idx]:
            consistency = 'NO'
            break
    print(consistency)

"""
정렬된 단어 리스트에서 단어 abc의 일관성
임의의 단어 ---가 abc뒤에 더해졌을 때, 사전 순으로 abc < abc--- 를 만족.
만약 abc와 abc---가 일관성 있다면, abc--- 뒤의 단어들은 abc---*** 형태 또는 abx (x>c)인 형태이므로 바로 전 단어만 체크하면 됨.
"""

