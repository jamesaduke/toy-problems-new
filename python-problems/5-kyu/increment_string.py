# Your job is to write a function which increments a string, to create a new string.
#
#     If the string already ends with a number, the number should be incremented by 1.
#     If the string does not end with a number. the number 1 should be appended to the new string.
#
# Examples:
#
# foo -> foo1
#
# foobar23 -> foobar24
#
# foo0042 -> foo0043
#
# foo9 -> foo10
#
# foo099 -> foo100


def increment_string(strng):
    # strip the decimals from the right
    stripped = strng.rstrip('1234567890')

    # get the part of strng that was stripped
    ints = strng[len(stripped):]

    if len(ints) == 0:
        return strng + '1'
    else:
        # find the length of ints
        length = len(ints)

        # add 1 to ints
        new_ints = 1 + int(ints)

        # pad new_ints with zeroes on the left
        new_ints = str(new_ints).zfill(length)

        return stripped + new_ints


print(increment_string("foo"))
print(increment_string("foo1"))
