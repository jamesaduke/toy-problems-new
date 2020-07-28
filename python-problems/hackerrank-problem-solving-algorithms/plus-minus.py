# Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros.
# Print the decimal value of each fraction on a new line.
#
# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers
# with absolute error of up to 10 ^ -4are acceptable.
#
# For example, given the array arr = [1,1,0, -1 , -1]
# there are 5 elements, two positive, two negative and one zero. Their ratios would be 2/5  , 2/ 5 and 1/5
#
# . It should be printed as
#
# 0.400000
# 0.400000
# 0.200000
#
# Function Description
#
# Complete the plusMinus function in the editor below. It should print out the ratio of positive, negative and zero
# items in the array, each on a separate line rounded to six decimals.
#
# plusMinus has the following parameter(s):
#
#     arr: an array of integers
#
# Input Format
#
# The first line contains an integer,
# , denoting the size of the array.
# The second line contains space-separated integers describing an array of numbers
#
# .
#
# Constraints
# 0 < n <= 100

#
# Output Format
#
# You must print the following
#
# lines:
#
#     A decimal representing of the fraction of positive numbers in the array compared to its size.
#     A decimal representing of the fraction of negative numbers in the array compared to its size.
#     A decimal representing of the fraction of zeros in the array compared to its size.
#
# Sample Input
#
# 6
# -4 3 -9 0 4 1
#
# Sample Output
#
# 0.500000
# 0.333333
# 0.166667
#
# Explanation
#
# There are 3 positive numbers, 2 negative numbers, and 1 zero in the array.
# The proportions of occurrence are positive:3/ 6 = 0.50000 , negative: 2/6 = 0.33333 and zeros: 1/6 = 0.166667 .

# Complete the plusMinus function below.


def plusminus(arr):
    positive = 0
    negative = 0
    zeros = 0
    array_length = len(arr)

    for num in arr:
        if num > 0:
            positive += 1
        elif num < 0:
            negative += 1
        else:
            zeros += 1
    new_negative = negative / array_length
    new_positive = positive / array_length
    new_zeroes = zeros / array_length
    formatted_negative = "{:.4f}".format(new_negative)
    formatted_zeroes = "{:.4f}".format(new_zeroes)
    formatted_positive = "{:.4f}".format(new_positive)
    print(formatted_positive)
    print(formatted_negative)
    print(formatted_zeroes)
