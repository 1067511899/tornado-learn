'''
Complete the function/method so that it takes CamelCase string and returns the string in snake_case notation. Lowercase characters can be numbers. If method gets number, it should return string.

Examples:

# returns test_controller
to_underscore('TestController')

# returns movies_and_books
to_underscore('MoviesAndBooks')

# returns app7_test
to_underscore('App7Test')

# returns "1"
to_underscore(1)
'''

def to_underscore(string):
    if type(string) != str:
        return str(string)
    result = []
    result.append(string[0].lower())
    for x in string[1:]:
        if x.isupper():
            result.append('_' + x.lower())
        else:
            result.append(x)
    return ''.join(result)


import re
# 不要在意细节，有些人正则好就牛逼吗？显然。。。。。。。牛逼
def to_underscore1(string):
    return re.sub(r'(.)([A-Z])', r'\1_\2', str(string)).lower()    

if __name__ == '__main__':
    print(to_underscore('App7Test'))
