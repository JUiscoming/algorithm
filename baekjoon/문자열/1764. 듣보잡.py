import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))

no_see = set()
no_hear = set()

for _ in range(N):
    no_see.add(input().rstrip())
for _ in range(M):
    no_hear.add(input().rstrip())

no_see_hear = sorted(list(no_see.intersection(no_hear)))

print(len(no_see_hear))
for name in no_see_hear:
    print(name)