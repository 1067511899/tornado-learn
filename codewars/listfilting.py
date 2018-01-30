'''
In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.
我操。这里面是说，是由字符串和非负整数组成，而不是说，输出非负整数。
Example
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
'''
def filter_list(l):
    res=[]
    for x in l:
        if isinstance(x,int):
            res.append(x)
    return res


def filter_list1(l):
    return [i for i in l if not isinstance(i, str)]


if __name__=='__main__':
    print(filter_list1([1,'a','b',0,-15]))