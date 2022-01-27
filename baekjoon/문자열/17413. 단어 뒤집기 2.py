x = list(input())

# 문자열 알고리즘에서는 for문보다 while문이 좀 더 편한듯
# 문자열 끝부분에 처리 안된 문자열 예외처리 하는 경우, 특정 조건을 만족할 때까지 탐색 등..

def reverse_words(s):
    tag = False
    start = 0
    i = 0
    while i < len(s):
        if s[i] == '<':
            while s[i] != '>':
                i += 1
            i += 1
        elif s[i].isalnum():
            start = i
            while i < len(s) and s[i].isalnum():
                i += 1
            s[start: i] = s[start: i][::-1]
        else:
            i += 1
    return ''.join(s)

print(reverse_words(x))