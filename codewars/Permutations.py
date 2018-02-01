'''
In this kata you have to create all permutations of an input string and remove duplicates, if present. This means, you have to shuffle all letters from the input in all possible orders.

Examples:

permutations('a'); # ['a']
permutations('ab'); # ['ab', 'ba']
permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
The order of the permutations doesn't matter.
这个题没什么意思，因为可以直接调用itertools的内置函数。
'''
import itertools
def permutations(string):
    tmp = set(itertools.permutations(string))
    result = []
    for x in tmp:
        result.append(''.join(x))
    return result


def permutations1(string):
    return list("".join(p) for p in set(itertools.permutations(string)))

if __name__ == '__main__':
    print(permutations('aabb'))
