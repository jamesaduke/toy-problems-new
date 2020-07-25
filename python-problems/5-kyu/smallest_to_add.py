# This is a demo task.
#
# Write a function:
#
# def solution(A)
#
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
#
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
#
# Given A = [1, 2, 3], the function should return 4.
#
# Given A = [−1, −3], the function should return 1.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].
# Copyright 2009–2020 by Codility Limited. All Rights Reserved. Unauth

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    # write your code in Python 3.6
    # set method sorts the array and removes duplicates
    A = set(A)
    # Because the number should not be 0 we start with 0 because it is the smallest possible integer
    ans = 1
    while ans in A:
        ans += 1
    print(ans)


solution([1, 3, 6, 4, 1, 2])

# without set method

# TODO: EXPLAIN THE FOLLOWING CODE BELOW IN COMMENT FASHION
def smallest_missing_positive_integer(A):
    A.sort()
    N = len(A)

    i = 0
    previous = 0
    while i < N:
        current = A[i]

        if current > 0:
            if current > previous + 1:  # breaks consecutiveness
                return previous + 1
            else:
                previous = current

        i += 1

    return max(previous + 1, current + 1)

# Compilation successful.
#
# Example test:   [1, 3, 6, 4, 1, 2]
# WRONG ANSWER (got 7 expected 5)
#
# Example test:   [1, 2, 3]
# OK
#
# Example test:   [-1, -3]
# OK
