'''
Write a function named firstNonRepeatingLetter† that takes a string input, and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return the empty string ("").

† Note: the function is called firstNonRepeatingLetter for historical reasons, but your function should handle any Unicode character.
'''
def first_non_repeating_letter1(string):
    tmp = string.lower()
    for x in string:
        if tmp.count(x.lower()) == 1:
            return x
    return ''

# 这个更好，毕竟Counter是一次性的。
from collections import Counter
def first_non_repeating_letter(string):
    cnt = Counter(string.lower())
    for letter in string:
        if cnt[letter.lower()] == 1:
            return letter
    return ''


if __name__ == '__main__':
    print(first_non_repeating_letter('sTreSS'))
