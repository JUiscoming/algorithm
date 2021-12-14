import sys
input = sys.stdin.readline

s = input().rstrip()
b = input().rstrip()

stack = []

# 터질때마다 새 접점만 검사해주면 됨
# 문자열 터지는걸 visualize하면 stack이 생각나는 것 같기도..
for i, c in enumerate(s):
    stack.append(c)
    if len(stack) >= len(b) and c == b[-1]:
        boom = True
        for j in range(len(b)):
            if stack[-len(b)+j] != b[j]:
                boom = False
                break
        if boom:
            for _ in range(len(b)):
                stack.pop()
            # stack = stack[:-len(b)]
if stack:
    print(''.join(stack))
else:
    print('FRULA')