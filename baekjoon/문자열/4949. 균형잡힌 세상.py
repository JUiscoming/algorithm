import sys

input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == '.':
        break
    stack = []

    for c in s:
        if c == '(' or c == '[':
            stack.append(c)
        elif (c == ')' or c == ']') and len(stack) == 0:
            stack = [0]
            break
        elif c == ')' and stack.pop() != '(':
            stack = [0]
            break
        elif c == ']' and stack.pop() != '[':
            stack = [0]
            break            
    if len(stack) == 0:
        print('yes')
    else:
        print('no')