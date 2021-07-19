# Function description: https://www.hackerrank.com/challenges/kangaroo/problem

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    for n in range(1000):
        if (x1 + v1) == (x2 + v2):
            print("YES")
        x1 += v1
        x2 += v2
    print("NO")


kangaroo(0, 2, 5, 3)
