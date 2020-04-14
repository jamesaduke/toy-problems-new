# A string is considered to be in title case if each word in the string is either (a) capitalised (that is, only the first letter of the word is in upper case) or (b) considered to be an exception and put entirely into lower case unless it is the first word, which is always capitalised.

# Write a function that will convert a string into title case, given an optional list of exceptions (minor words). The list of minor words will be given as a string with each word separated by a space. Your function should ignore the case of the minor words string -- it should behave in the same way even if the case of the minor word string is changed.

# ###Arguments (Haskell)

#     First argument: space-delimited list of minor words that must always be lowercase except for the first word in the string.
#     Second argument: the original string to be converted.

# ###Arguments (Other languages)

#     First argument (required): the original string to be converted.
#     Second argument (optional): space-delimited list of minor words that must always be lowercase except for the first word in the string. The JavaScript/CoffeeScript tests will pass undefined when this argument is unused.

# ###Example

# title_case('a clash of KINGS', 'a an the of') # should return: 'A Clash of Kings'
# title_case('THE WIND IN THE WILLOWS', 'The In') # should return: 'The Wind in the Willows'
# title_case('the quick brown fox') # should return: 'The Quick Brown Fox'


def title_case(title, minor_words=''):
    if title != '':
        edited = []
        title = [word.lower() for word in title.split()]
        edited.append(title.pop(0).capitalize())

        if minor_words != None:
            minor_words = [word.lower() for word in minor_words.split()]

            for word in title:
                if word not in minor_words:
                    edited.append(word.capitalize)
                else:
                    edited.append(word)

        else:
            for word in title:
                edited.append((word.capitalize()))

        return ' '.join(edited)# gives this error TypeError: sequence item 0: expected str instance, bytes found

    else:
        return title

    # clever solution
def title_case(title, minor_words=''):
    title = title.capitalize().split()
    minor_words = minor_words.lower().split()
    return ' '.join([word if word in minor_words else word.capitalize() for word in title])