#!/bin/python3


#
# Complete the 'meanderingArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY unsorted as parameter.
#

def meanderingArray(unsorted):
    # Write your code here
    unsorted.sort()
    results =[]
    for i in range(len(unsorted)):
        results.append(unsorted[len(unsorted)-1-i])
        results.append(unsorted[i])
    results = results[:len(results)//2]
    unsorted = results
    return unsorted
