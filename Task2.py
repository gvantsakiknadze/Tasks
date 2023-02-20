
def sumOfDigits(start,end):
    sum_of_digits = 0 
    for number in range(start, end+1):
        sum_of_digits += sum([int(digit) for digit in str(number)])
    return sum_of_digits



def sum(i):
    sum = 0
    while i != 0:
        sum += i % 10
        i = int(i/10)
    return sum


def sumOfDigits2(x,y):
    final_sum = 0
    for i in range(x,y+1):
        final_sum += sum(i)
    return final_sum

