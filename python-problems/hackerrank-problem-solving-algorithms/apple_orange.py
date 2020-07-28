# Problem statement: https://www.hackerrank.com/challenges/apple-and-orange/problem

# s: integer, starting point of Sam's house location.
# t: integer, ending location of Sam's house location.
# a: integer, location of the Apple tree.
# b: integer, location of the Orange tree.
# apples: integer array, distances at which each apple falls from the tree.
# oranges: integer array, distances at which each orange falls from the tree.


def count_apples_and_oranges(s, t, a, b, apples, oranges):
    apple_no = 0
    orange_no = 0
    for i in range(len(apples)):
        position = apples[i] + a
        if s <= position <= t:
            apple_no += 1
    for i in range(len(oranges)):
        position = oranges[i] + b
        if s <= position <= t:
            orange_no += 1
    print(apple_no)
    print(orange_no)


count_apples_and_oranges(7, 11, 5, 15, [-2, 2, 1], [5 - 6])
