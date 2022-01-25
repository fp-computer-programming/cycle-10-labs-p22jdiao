# Author: JD 01/25/2022


def sum_to(n):
    
    counter = 0
    sum = 0
    while counter <= n:
        sum += counter
        counter += 1

    return sum

print(sum_to(100))
