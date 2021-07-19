# You will be given two arrays of integers and asked to determine all integers that satisfy the following two
# conditions:
#
# The elements of the first array are all factors of the integer being considered
# The integer being considered is a factor of all elements of the second array
# These numbers are referred to as being between the two arrays. You must determine how many such numbers exist.
#
# For example, given the arrays  and , there are two numbers between them:  and . , ,  and  for the first value.
# Similarly, ,  and , .
#
# Function Description
#
# Complete the getTotalX function in the editor below. It should return the number of integers that are between the
# sets.
#
# getTotalX has the following parameter(s):
#
# a: an array of integers
# b: an array of integers
# Input Format
#
# The first line contains two space-separated integers,  and , the number of elements in array  and the number of
# elements in array . The second line contains  distinct space-separated integers describing  where . The third line
# contains  distinct space-separated integers describing  where .
#
# Constraints
#
# Output Format
#
# Print the number of integers that are considered to be between  and .
#
# Sample Input
#
# 2 3
# 2 4
# 16 32 96
#
# Sample Output
#
# 3
# Explanation
#
# 2 and 4 divide evenly into 4, 8, 12 and 16.
# 4, 8 and 16 divide evenly into 16, 32, 96.
#
#
# 4, 8 and 16 are t
from functools import reduce


def getTotalX(a, b):
    def gcd(a, b):
        if b == 0:
            return a
        print(gcd(b, a % b))

    def lcm(a, b):
        return a * b // gcd(a, b)

    l = reduce(lcm, a)
    g = reduce(gcd, b)

    s = 0
    for i in (l, g + 1, l):
        if g % i == 0:
            s += 1
    return s
# Alternative solution
#
# def getTotalX(a, b):
#     lcm_num = a[0]
#     gcd_num = b[0]
#     if len(a) > 1:
#         for x in range(1,len(a)):
#             lcm_num =  (lcm_num * a[x])//math.gcd(lcm_num,a[x])
#     if len(b) > 1:
#         for x in range(1,len(b)):
#             gcd_num = math.gcd(gcd_num,b[x])
#     count = 0
#     for x in range(lcm_num, gcd_num+1, lcm_num):
#         if gcd(x, gcd_num) == x:
#             count += 1
#     return count