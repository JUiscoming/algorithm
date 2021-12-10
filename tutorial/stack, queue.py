from collections import deque

items = [5, 2, 3 ,1]
# 1. stack (Last In First Out, LIFO)
print('1. Stack')
stack = []

for value in items:
    stack.append(value) # push
    print(f'pushed: {stack[-1]}, state: {stack}')

for _ in range(2):
    top = stack.pop() # pop
    print(f'popped: {top}, state: {stack}')

# 2. queue
print('2. Queue')
queue = deque()

for value in items:
    queue.append(value)
    print(f'pushed: {value}, state: {queue}')

queue[2] = 6 # 인덱싱을 통한 탐색, 대입 가능
# print(queue[:]) # deque는 list 자료형과 다르게 슬라이싱을 사용할 수 없음.

for _ in range(2):
    output = queue.popleft() # pop
    print(f'popped: {output}, state: {queue}')
    # appendleft() 또한 사용 가능 (double-ended queue이기 때문)

