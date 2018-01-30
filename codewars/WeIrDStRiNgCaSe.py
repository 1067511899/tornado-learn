'''
Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased.

The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').

Examples:
to_weird_case('String'); # => returns 'StRiNg'
to_weird_case('Weird string case') # => returns 'WeIrD StRiNg CaSe'
'''
def to_weird_single(str1):
    tmp = ''
    leng = len(str1)
    for i in range(leng):
        if i % 2 == 0:
            tmp += str1[i].upper()
        else:
            tmp += str1[i].lower()
    return tmp

def to_weird_case(string):
    ls = string.split(' ')
    ls1 = []
    for x in ls:
        tmp = to_weird_single(x)
        ls1.append(tmp)
    return(' '.join(ls1))       

def to_weird_case_word(string):
    return "".join(c.upper() if i % 2 == 0 else c for i, c in enumerate(string.lower()))
'''
enumerate(iterable[, start]) -> iterator for index, value of iterable
    
    Return an enumerate object.  iterable must be another object that 
     supports
    iteration.  The enumerate object yields pairs containing a count (from
    start, which defaults to zero) and a value yielded by the iterable 
     argument.
    enumerate is useful for obtaining an indexed list:
    (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
'''   
def to_weird_case1(string):
    return " ".join(to_weird_case_word(str) for str in string.split())

if __name__ == '__main__':
    for i, c in enumerate('Eclipse'.lower()):
        print(i, c)
