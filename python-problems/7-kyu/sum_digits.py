# Write a function named sumDigits which takes a number as input and returns the sum of the absolute value of each of the number's decimal digits. For example:

#   sum_digits(10)  # Returns 1
#   sum_digits(99)  # Returns 18
#   sum_digits(-32) # Returns 5


def sumDigits(number):
    number = abs(number)
    return_number = 0
    
    while number > 0:
        return_number += number % 10
        number = int(number / 10)
        
    return return_number