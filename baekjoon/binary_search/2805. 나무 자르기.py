import sys

input = sys.stdin.readline

def upper_bound(tree_list, tgt_length, st, end):
    while st < end:
        mid = (st+end)//2
        S = 0 # summation
        for tree in tree_list:
            if tree > mid:
                S += (tree - mid)
        
        if S >= tgt_length:
            st = mid + 1
        else:
            end = mid
    
    return end

N, M = map(int, input().split(' '))
tree_list = list(map(int, input().split(' ')))
tree_list.sort() # O(NlogN)

print(upper_bound(tree_list, M, 0, tree_list[-1])-1)