def lower_bound(X, Y, st, end):
    pre_Z = (Y*100)//X
    while st < end:
        mid = (st+end)//2
        post_Z = ((Y+mid)*100)//(X+mid)

        if pre_Z < post_Z:
            end = mid
        else:
            st = mid+1
    return st

try:
    while True:
        X, Y = map(int, input().split())
        Z = (Y*100)//X

        if Z >= 99:
            answer = -1
        else:
            answer = lower_bound(X, Y, 0, X)
        print(answer)
except:
    exit()