'''
Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)

##Examples :

iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even

iq_test("1 2 1 1") => 2 // Second number is even, 
'''
from collections import Counter
def duplicate_count(text):
    return len([k for k, v in Counter(text).items() if v > 1])


def unique_in_order(iterable):
    
    s = list(iterable)
    s1 = []
    le = len(s)
    if le <= 1:
        return s
    s1.append(s[0])
    for x in range(1, le):
        if s[x] != s[x - 1]:
            s1.append(s[x])
    return s1

from itertools import groupby

def unique_in_order1(iterable):
    tmp = groupby(iterable)
    for (k, v) in tmp:
        print(k, v)
    return [k for (k, _) in groupby(iterable)]


def likes(names):
    le = len(names)
    if le == 0:
        return 'no one likes this'
    elif le == 1:
        return '{} likes this'.format(names[0])
    elif le == 2:
        return '{} and {} like this'.format(names[0], names[1])
    elif le == 3:
        return '{}, {} and {} like this'.format(names[0], names[1], names[2])
    return '{}, {} and {} others like this'.format(names[0], names[1], le - 2)


def likes1(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n - 2)


if __name__ == '__main__':
#     print(duplicate_count("abcde"), 0)
#     print(duplicate_count("abcdea"), 1)
#     print(duplicate_count("indivisibility"), 1)
#     print(unique_in_order1('AAAABBBCCDAABBB'), ['A', 'B', 'C', 'D', 'A', 'B'])
#     print(unique_in_order1('ABBCcAD'))
#     print(unique_in_order1([1, 2, 2, 3, 3]))
    print(likes([]), 'no one likes this')
    print(likes(['Peter']), 'Peter likes this')
    print(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
    print(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
    print(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')
