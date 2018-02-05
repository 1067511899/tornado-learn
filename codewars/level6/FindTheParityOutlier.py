'''
You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
'''
# 嗯嗯，这种格式其实是可以加条件的
def find_outlier(integers):
    odd = [x for x in integers if x % 2]
    even = [x for x in integers if not x % 2]
    
    if len(odd) == 1:
        return odd[0]
    else:
        return even[0]

def find_outlier1(inte):
    odds = [x for x in inte if x % 2 != 0]
    evens = [x for x in inte if x % 2 == 0]
    return odds[0] if len(odds) < len(evens) else evens[0]

if __name__ == '__main__':
    print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
