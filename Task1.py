def minSplit(x):
    if x < 0:
        print("Please enter a positive number")
        return -1
    counter = 0
    for i in lst:
        if x >= i:
            counter += int(x/i)
            x = x % i

    return counter


lst = [50, 20, 10, 5, 1]
