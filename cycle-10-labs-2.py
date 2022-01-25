# Author: JD 01/25/2022

def five_divi(lst):
    new = []
    for x in lst:
        if x > 500:
            break
        elif x % 5 == 0 and x <= 150:
            new.append(x)

    return(new)

