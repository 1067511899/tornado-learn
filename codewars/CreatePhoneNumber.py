'''
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example:
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]]) # => returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge. 
Don't forget the space after the closing parenthesis!
'''
def create_phone_number(n):
    n = [str(x) for x in n]
    n.insert(0, '(')
    n.insert(4, ')')
    n.insert(5, ' ')
    n.insert(9, '-')
    return ''.join(n)

# best answer I think
def create_phone_number1(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
'''
关于对list使用*的解释。
自动把list解释成对应的需要的参数。
If the syntax *expression appears in the function call, expression must evaluate to an iterable. Elements from these iterables are treated as if they were additional positional arguments. For the call f(x1, x2, *y, x3, x4), if y evaluates to a sequence y1, …, yM, this is equivalent to a call with M+4 positional arguments x1, x2, y1, …, yM, x3, x4.
'''
# use map,another 
def create_phone_number2(n):
    n = ''.join(map(str, n))
    return '(%s) %s-%s' % (n[:3], n[3:6], n[6:])

if __name__ == '__main__':
    print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
