x = int(input())
y = int(input())

answer = x*y

n = 10
while y > 0:
    print(x*(y%10))
    y //= 10
print(answer)