import sys

input = sys.stdin.readline

while True:
    s = input().rstrip()

    if s == '0':
        break

    condition = 'yes'
    for i in range(len(s)//2):
        if s[i] != s[len(s)-1-i]:
            condition = 'no'
            break
    print(condition)