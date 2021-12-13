import sys

input = sys.stdin.readline

N = int(input())
word_list = []
for _ in range(N):
    word_list.append(input().rstrip())

answer = N
for word in word_list:
    char_dict = {k: True for k in 'abcdefghijklmnopqrstuvwxyz'}
    
    prev_char = word[0]
    for c in word[1:]:
        if char_dict[c] == False:
            answer -= 1
            break
        
        if c != prev_char:
            char_dict[prev_char] = False
        prev_char = c
print(answer)