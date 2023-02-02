def isProperly(sequence):
    counter = 0
    for i in sequence:
        if i == "(":
            counter += 1
        elif i == ")":
            counter -= 1
        if counter < 0:
            return False
    if counter == 0:
        return True
    return False
