'''
Your task is to sort a given string. Each word in the String will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input String is empty, return an empty String. The words in the input String will only contain valid consecutive numbers.

For an input: "is2 Thi1s T4est 3a" the function should return "Thi1s is2 3a T4est"

your_order("is2 Thi1s T4est 3a")
[1] "Thi1s is2 3a T4est"
'''
import re
def order(sentence):
    if not sentence:
        return ''
    dic = {}
    for x in sentence.split():
        pos = int(re.findall('\d', x)[0])
        dic[pos] = x
    
    key = list(dic.keys())
    key.sort()
    result = []
    for x in key:
        result.append(dic[x])
    
    return ' '.join(result)

def order1(words):
    return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))
# 因为 数字比字母小，如果数字在最前面，那么排序其实是按照数字来排序的。


if __name__ == '__main__':
    print(order1("is2 Thi1s T4est 3a"))
