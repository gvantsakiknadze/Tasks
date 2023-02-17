def countWays(n, steps):
    if n == 1:
        return steps[0]+1
    lst = [1]
    if steps[0] == 0:
        lst.append(0)
    else:
        lst.append(1)
    for i in range(2,n+1):
        if steps[i-1] == 1:
            lst.append(lst[i-1]+lst[i-2])
        else:
            lst.append(0)

    return lst[n]+lst[n-1]



print(countWays(5,[1, 1, 0, 1, 1]))









