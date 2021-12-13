def fib_count(num_list):
    dict_01 = {0: (1,0), 1: (0, 1)}
    def fib(n):
        nonlocal dict_01

        c0, c1 = 0, 0
        if n == 0:
            c0 += 1
            return c0, c1
        elif n == 1:
            c1 += 1
            return c0, c1
        else:
            if n not in dict_01:
                left_c0, left_c1 = fib(n-1)
                right_c0, right_c1 = fib(n-2)
                dict_01[n] = (left_c0+right_c0, left_c1+right_c1)
            return dict_01[n]

    for num in num_list:
        a, b = fib(num)
        print(a, b)

T = int(input())
num_list = []
for _ in range(T):
    num_list.append(int(input()))
fib_count(num_list)