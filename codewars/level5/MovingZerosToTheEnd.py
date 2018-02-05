'''
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]
'''
def move_zeros(array):
    newa = [x for x in array if isinstance(x, bool) or x != 0]
    le = len(array) - len(newa)
    newa += [0] * le
    return newa


# 终于和我自己的代码有点儿类似了。这道题的难度在于，在python，False==0是成立的，唯一的区别
# 在于它们的instance不同。
def move_zeros1(arr):
    l = [i for i in arr if isinstance(i, bool) or i != 0]
    return l + [0] * (len(arr) - len(l))

if __name__ == '__main__':
    print(move_zeros(['a', 'b', None, 'c', 'd', 1, False, 1, 3, [], 1, 9, {}, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
# ['a', 'b', None, 'c', 'd', 1, False, 1, 3, [], 1, 9, {}, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print(False == 0)
    print(100 + False)  # False 和 0 基本上完全通用
#     print(isinstance(0, bool))
#     x = False
#     print(not  isinstance(x, bool))
    wtf = [False, False, False]
    print(wtf.count(0))
