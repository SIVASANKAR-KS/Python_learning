def highest_even(*numbers):
    highest_number = 0
    for x in numbers:
        if (x > highest_number) and (x%2==0):
            highest_number = x
    return highest_number

print(highest_even(10,2,18,4,11))
