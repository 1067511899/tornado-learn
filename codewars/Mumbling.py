'''
This time no story, no theory. The examples below show you how to write function accum:

Examples:

accum("abcd")    # "A-Bb-Ccc-Dddd"
accum("RqaEzty") # "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt")    # "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
'''
def accum(s):
    count = 0
    res = []
    for x in s:
        res.append(x.upper() + x.lower() * count)
        count += 1
    return '-'.join(res)

def accum1(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

if __name__ == '__main__':
    print(accum('RqaEzty'))
