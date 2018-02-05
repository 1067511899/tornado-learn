'''
At a job interview, you are challenged to write an algorithm to check if a given string, s, can be formed from two other strings, part1 and part2.

The restriction is that the characters in part1 and part2 are in the same order as in s.

The interviewer gives you the following example and tells you to figure out the rest from the given test cases.

For example:

'codewars' is a merge from 'cdw' and 'oears':

    s:  c o d e w a r s   = codewars
part1:  c   d   w         = cdw
part2:    o   e   a r s   = oears
判断，s是否由part1和part2的字符串组合而成，并且这些字符在s当中的顺序和在part1/part2当中
的顺序一致。
'''
def is_merge(s, part1, part2):
    p1 = list(part1)
    p2 = list(part2)
    for x in s:
        if p1 and x == p1[0]:
            p1 = p1[1:]
        elif p2 and x == p2[0]:
            p2 = p2[1:]
        else:
            return False
    if not p1 and not p2:
        return True
    return False

def is_merge1(s, part1, part2):
    if not part1:
        return s == part2
    if not part2:
        return s == part1
    if not s:
        return part1 + part2 == ''
    if s[0] == part1[0] and is_merge(s[1:], part1[1:], part2):
        return True
    if s[0] == part2[0] and is_merge(s[1:], part1, part2[1:]):
        return True
    return False

if __name__ == '__main__':
    print(is_merge('codewars', 'code', 'wasr'))
    print(is_merge('codewars', 'cdw', 'oears'))
    print(is_merge('codewars', 'cod', 'wars'))
