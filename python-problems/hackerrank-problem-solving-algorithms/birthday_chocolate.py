# problem statement: https://www.hackerrank.com/challenges/the-birthday-bar/problem


def birthday(s, d, m):
    tp = (len(s) - m) + 1  # total number of pieces possible
    count = 0
    for i in range(tp):
        if sum(s[i:i + m]) == d:
            count += 1
    return count


birthday([1, 2, 1, 3, 2], 3, 2)
