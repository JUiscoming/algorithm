s = input()

suffix_list = []
for i in range(len(s)):
    suffix_list.append(s[i:])

suffix_list.sort()
for suffix in suffix_list:
    print(suffix)