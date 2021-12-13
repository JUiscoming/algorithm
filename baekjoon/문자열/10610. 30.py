N = input()

digit_dict = {k: 0 for k in range(10)}
S = 0
for c in N:
    S += int(c)
    digit_dict[int(c)] += 1

if S%3 != 0 or digit_dict[0] == 0:
    print(-1)
else:
    answer = ""
    for i in reversed(range(10)):
        answer += (str(i)*digit_dict[i])
    print(answer)