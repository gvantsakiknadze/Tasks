def zeros(x):
    counter = 0
    while x != 0:
        counter += int(x/5)
        x = int(x/5)
    return counter


print(zeros(490))