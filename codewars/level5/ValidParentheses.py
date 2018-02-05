'''
Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
Constraints
0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. Furthermore, the input string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).
'''
def clear(string):
    result = []
    for x in string:
        if x in ('(', ')'):
            result.append(x)
    return ''.join(result)

def valid_parentheses(string):
    string = clear(string)
    while('()' in string):
        string = string.replace('()', '')
    return string == ''

# 又是一种有趣的思路
def valid_parentheses1(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False

if __name__ == '__main__':
    print(valid_parentheses("(())((()())())"))
