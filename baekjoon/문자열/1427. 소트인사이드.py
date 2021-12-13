N = input()
digit_count = {k: 0 for k in '0123456789'}

for c in N:
    digit_count[c] += 1

answer = ""

for c in "9876543210":
    answer += (c*digit_count[c])

print(answer)