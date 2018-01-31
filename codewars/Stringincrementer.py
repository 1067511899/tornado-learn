'''
Your job is to write a function which increments a string, to create a new string. If the string already ends with a number, the number should be incremented by 1. If the string does not end with a number the number 1 should be appended to the new string.

Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.
'''
import re
def increment_string(strng):
    result = re.findall(r'\d+$', strng)
    formatn = len(result)
    if formatn == 0:
        return strng + '1'
    
    lenvalue = len(result[0])
    count = int(result[0]) + 1
    tmp = str(count)
    if len(tmp) >= lenvalue:
        return strng[:len(strng) - lenvalue] + tmp
    else:
        return strng[:len(strng) - lenvalue] + '0' * (lenvalue - len(tmp)) + tmp


def increment_string1(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng + "1"
    return head + str(int(tail) + 1).zfill(len(tail))

if __name__ == '__main__':
    print(increment_string('foo6677bar00999'))
