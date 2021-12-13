import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    ps = input().rstrip()

    stack = []

    for c in ps:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if stack:
                stack.pop()
            else:
                stack = [0]
                break
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')