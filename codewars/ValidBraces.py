'''
Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false if it's invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}. Thanks to @arnedag for the idea!

All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

What is considered Valid?
A string of braces is considered valid if all braces are matched with the correct brace.

Examples
"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False
'''
# 别人实现的，我抄了一个一个题的实现办法，但显然脑筋没有能急转弯
def validBraces(s):
    while '{}' in s or '()' in s or '[]' in s:
        s = s.replace('{}', '')
        s = s.replace('[]', '')
        s = s.replace('()', '')
    return s == ''

opposite = {')': '(', ']': '[', '}': '{'}
keys = [')', ']', '}']
def dirReduc(plan):
    new_plan = []
    for d in plan:
        if d in keys:
            if new_plan and new_plan[-1] == opposite[d]:
                new_plan.pop()
            else:
                new_plan.append(d)
        else:
            new_plan.append(d)
    if len(new_plan) > 0:
        return False
    return True



if __name__ == '__main__':
    print(dirReduc('[({})](]'))
