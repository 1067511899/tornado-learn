'''
Write function scramble(str1,str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

For example:
str1 is 'rkqodlw' and str2 is 'world' the output should return true.
str1 is 'cedewaraaossoqqyt' and str2 is 'codewars' should return true.
str1 is 'katas' and str2 is 'steak' should return false.

Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered
'''
from collections import Counter

def scramble(s1, s2):
    print(Counter(s1))
    print(Counter(s2))
    print(Counter(s2) - Counter(s1))
    if len(s1) < len(s2):
        return False
    set1 = set(s2)
    for x in set1:
        if s1.count(x) < s2.count(x):
            return False
    return True

def scramble1(s1, s2):
    # Counter basically creates a dictionary of counts and letters
    # Using set subtraction, we know that if anything is left over,
    # something exists in s2 that doesn't exist in s1
    return len(Counter(s2) - Counter(s1)) == 0

if __name__ == '__main__':
    print(scramble('kateams', 'steaaak'))
