'''
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, and u as vowels for this Kata.

The input string will only consist of lower case letters and/or spaces.
'''
def getCount(inputStr):
    num_vowels = 0
    for x in inputStr:
        if x in 'aeiouAEIOU':
            num_vowels += 1
    return num_vowels
#
def getCount1(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")

if __name__ == '__main__':
    pass
