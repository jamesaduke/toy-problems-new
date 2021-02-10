# Problem definition - https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    # Complete this function
    count = 0
    for i in range(n - 1):
        j = i + 1
        while j < n:
            if ((ar[i] + ar[j]) % k) == 0:
                count += 1
            j += 1
    return count