def diagonaldifference(arr):
    # Write your code here
    primary=0
    secondary=0
    length = len(arr)
    for count in range(length):
        primary += arr[count][count]
        secondary += arr[count][(length-count-1)]
    return abs(primary-secondary)