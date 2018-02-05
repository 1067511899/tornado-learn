'''
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldWay !
'''
import re
def pig_it(text):
    st = text.split()
    result = []
    for x in st:
        if re.search('\W', x):
            result.append(x)
        else:
            result.append(x[1:] + x[0] + 'ay')
    return ' '.join(result)


if __name__ == '__main__':
    print(pig_it('Hello world !'))
