# 시간 복잡도: 2초 -> CPU clock 1GHz 기준, N = 50일 때, O(N^4) 이하로 설계 (K=10^3, M=10^6, G=10^9)
# 공간 복잡도: 128MB -> int 기준 32M (32 * 10^6)개 변수 = 약 3,200만개 , 1,000만 이하로 설계 (int: 4 Byte)

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

answer = sum([A[i]*B[i] for i in range(N)])
print(answer)