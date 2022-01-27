N = int(input())
M = int(input())
s = input()

def count_pattern(N, M, s):
    pattern = 'IO' * N + 'I'
    len_p = 2*N+1
    i = 0
    count = 0
    while i <= (M-len_p):
        if s[i: i+len_p] == pattern:
            count += 1
            i += 1
        i += 1
        
    return count

print(count_pattern(N, M, s))