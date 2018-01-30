'''
Examples:

"din" => "((("

"recede" => "()()()"

"Success" => ")())())"

"(( @" => "))(("


'''
import time
import collections
def duplicate_encode(word):
    a=collections.defaultdict(int)
    word=word.lower()
    for x in word:
        a[x]+=1
    y=''
    for x in word:
        if a[x]>1:
            y+=')'
        else:
            y+='('
    return y
    #your code here


def duplicate_encode1(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

if __name__=='__main__':
    begin=time.time()
    for x in range(1000000):
        duplicate_encode("21 similar code variations are grouped with this one")
    end1=time.time()
    for x in range(1000000):
        duplicate_encode1("21 similar code variations are grouped with this one")
    end2=time.time()
    print(end1-begin)
    print(end2-end1)