A, B = input().split(' ')

len_diff = len(B) - len(A)

min_dist = len(A)

for shift_idx in range(len_diff+1):
    dist = len(A)
    for char_idx in range(len(A)):
        if A[char_idx] == B[shift_idx+char_idx]:
            dist -= 1
    if min_dist > dist:
        min_dist = dist
        
print(min_dist)