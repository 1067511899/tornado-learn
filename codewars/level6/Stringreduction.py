'''
In this Kata, we are going to see how a Hash (or Map or dict) can be used to keep track of characters in a string.

Consider two strings "aabcdefg" and "fbd". How many characters do we have to remove from the first string to get the second string? Although not the only way to solve this, we could create a Hash of counts for each string and see which character counts are different. That should get us close to the answer. I will leave the rest to you.

For this example, solve("aabcdefg","fbd") = 5. Also, solve("xyz","yxxz") = 0, because we cannot get second string from the first since the second string is longer.

More examples in the test cases.

Good luck!
'''
from collections import Counter
def solve(a, b):
    if len(a) < len(b):
        return 0
    ca = Counter(a)
    cb = Counter(b)
    print(ca - cb)
    ca.subtract(cb)
    result = 0
    for keys in ca.keys():
        if ca[keys] < 0:
            return 0
        result += ca[keys]
    return result

def solve1(a, b):
    return 0 if Counter(b) - Counter(a) else len(a) - len(b)

if __name__ == '__main__':
    print(solve("xyz", "yxz"), 0)
    print(solve("abcxyz", "ayxz"), 2)
    print(solve("abcdexyz", "yxz"), 5)
    print(solve("xyz", "yxxz"), 0)
    print(solve("abdegfg", "ffdb"), 0)
    print(solve("aabcdefg", "fbd"), 5)
    print(solve("aabcdefg", "fdb"), 5)
