def isProperly(sequence):
    counter = 0
    mapping = {
        "(" : 1,
        ")" : -1,
    }
    
    
    conter = 0
    for i in sequence:
        counter += mapping[i]
        if counter < 0:
            return False
    return True
    



def isProperly2(sequence):
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
