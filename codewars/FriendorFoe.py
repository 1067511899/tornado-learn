'''
Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

Note: keep the original order of the names in the output.Created on 2018年1月29日

@author: lenovo
'''
def friend(x):
    ret = []
    for m in x:
        if len(m) == 4:
            ret.append(m)
    return ret


def friend1(x):
    return [f for f in x if len(f) == 4]