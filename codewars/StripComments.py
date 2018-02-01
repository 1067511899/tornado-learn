'''
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
'''
# 直接看答案了，有问题，没搞定。
def solution(string, markers):
    parts = string.split('\n')
    for s in markers:
        parts = [v.split(s)[0].rstrip() for v in parts]
    return '\n'.join(parts)

def solution1(string, markers):
    s = string.split('\n')
    result = []
    for x in s:
        hascomm = False
        for m in markers:
            ind = x.find(m)
            if  ind > 0:
                hascomm = True
                tmp = x[:ind]
                result.append(tmp.strip())
        if not hascomm:
            result.append(x)
        
    return '\n'.join(result)


if __name__ == '__main__':
    print(solution("a #b\nc\nd $e f ", ["#", "$"]))
