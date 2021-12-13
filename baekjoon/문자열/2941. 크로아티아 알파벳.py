len_2 = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
len_3 = 'dz='

s = input()
count = 0
i = 0
while i < len(s):
    if s[i:i+2] in len_2:
        count += 1
        i += 2
    elif s[i:i+3] == len_3:
        count += 1
        i += 3
    else:
        count += 1
        i += 1
print(count)