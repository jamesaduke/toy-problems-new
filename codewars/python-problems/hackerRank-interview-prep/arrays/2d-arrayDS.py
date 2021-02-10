# While going back on my grind with Algos I came across this fun Algo question on HackerRank.
# Let’s dive in!
# Problem Statement
# Given a 6*6 2D Array arr:
#
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
#
# We define an hourglass to be a subset of values with indices falling in this pattern in arr‘s graphical
# representation: a b c d e f g
#
# There are 16 hourglasses in arr, and an hourglass sum is the sum of an hourglass’ values.
# Calculate the hourglass sum for every hourglass in arr, then print the maximum hourglass sum.

# For example, given the 2D array:
#
# -9 -9 -9  1 1 1
#  0 -9  0  4 3 2
# -9 -9 -9  1 2 3
#  0  0  8  6 6 0
#  0  0  0 -2 0 0
#  0  0  1  2 4 0
#
# We calculate the following 16 hourglass values:
#
# -63, -34, -9, 12,
# -10, 0, 28, 23,
# -27, -11, -2, 10,
# 9, 17, 25, 18
# Our highest hourglass value is 28 from the hourglass:
#
# 0 4 3
#   1
# 8 6 6
#
# Function Description
#
# Complete the function hourglassSum in the editor below. It should return an integer, the maximum hourglass sum in
# the array.
#
# hourglassSum has the following parameter(s):
#
#     arr: an array of integers
#
# Input Format
#
# Each of the 6 lines of inputs arr[i] contains space-separated integers arr[i][j].
#
# Output Format
#
# Print the largest (maximum) hourglass sum found in arr.
#
# Sample Input
#
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0
# Sample Output
#
# 19
#
# Explanation
# arr contains the following hourglasses:
# Image for post
# Image for post
# The hourglass with the maximum sum (19) is:
#
# 2 4 4
#   2
# 1 2 4
#
# Copyright © 2015 HackerRank.
# All Rights Reserved.
#
# Let’s go step by step to make it more clear for you.
#
# create a count variable that will hold the lowest sum of the hourglass. ex: lowest sum will be -9 * 7 = -63 as the
# number goes from -9 to 9 and an hourglass is 7 elements so count will equal -63. create a first for loop to iterate
# over the array. create a second for loop to iterate over subarray. add up each element from subarrays for a square
# of 3 * 3. create a variable sum to hold the total of the added elements. check if the total of sum is bigger than
# the count variable. If yes, replace count by sum. This allows us to compare the previous sum of the hourglass to
# the most recent one to be able to return the highest one.

def hourglassSum(arr):
    max_hour_glass_sum = -63
    for i in range(4):
        for j in range(4):

            # sum of top 3 elements
            top = sum(arr[i][j:j + 3])

            # sum of the mid element
            mid = arr[i + 1][j + 1]

            # sum of bottom 3 elements
            bottom = sum(arr[i + 2][j:j + 3])

            hour_glass_sum = top + mid + bottom

            if hour_glass_sum > max_hour_glass_sum:
                max_hour_glass_sum = hour_glass_sum

    return max_hour_glass_sum


