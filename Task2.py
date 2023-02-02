def sum(i):
    sum = 0
    while i != 0:
        sum += i % 10
        i = int(i/10)
    return sum


def sumOfDigits(x,y):
    final_sum = 0
    for i in range(x,y+1):
        final_sum += sum(i)
    return final_sum


print(sumOfDigits(17, 20))
