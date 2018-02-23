'''
You are given two sorted arrays that both only contain integers. Your task is to find a way to merge them into a single one, sorted in asc order. Complete the function mergeArrays(arr1, arr2), where arr1 and arr2 are the original sorted arrays.

You don't need to worry about validation, since arr1 and arr2 must be arrays with 0 or more Integers. If both arr1 and arr2 are empty, then just return an empty array.

Note: arr1 and arr2 may be sorted in different orders. Also arr1 and arr2 may have same integers. Remove duplicated in the returned result.

Example:

arr1 = [1,2,3,4,5];
arr2 = [6,7,8,9,10];
mergeArrays(arr1, arr2);  // [1,2,3,4,5,6,7,8,9,10];

arr3 = [1,3,5,7,9];
arr4 = [10,8,6,4,2];
mergeArrays(arr3, arr4);  // [1,2,3,4,5,6,7,8,9,10];

arr5 = [1,3,5,7,9,11,12];
arr6 = [1,2,3,4,5,10,12];
mergeArrays(arr5, arr6);  // [1,2,3,4,5,7,9,10,11,12];

sorted(iterable, *, key=None, reverse=False)
Return a new sorted list from the items in iterable.

Has two optional arguments which must be specified as keyword arguments.

key specifies a function of one argument that is used to extract a comparison key from each list element: key=str.lower. The default value is None (compare the elements directly).

reverse is a boolean value. If set to True, then the list elements are sorted as if each comparison were reversed.

Use functools.cmp_to_key() to convert an old-style cmp function to a key function.

The built-in sorted() function is guaranteed to be stable. A sort is stable if it guarantees not to change the relative order of elements that compare equal — this is helpful for sorting in multiple passes (for example, sort by department, then by salary grade).

For sorting examples and a brief sorting tutorial, see Sorting HOW TO.
'''

# 嗯嗯，soted返回的就是个list
def merge_arrays(arr1, arr2):
    return sorted(set(arr1 + arr2))


if __name__ == '__main__':
    arr1 = [1, 2, 3, 4, 5];
    arr2 = [6, 7, 8, 9, 10];
    print(merge_arrays(arr1, arr2))
    
    arr3 = [1, 3, 5, 7, 9];
    arr4 = [10, 8, 6, 4, 2];
    print(merge_arrays(arr3, arr4))
    
    arr5 = [1, 3, 5, 7, 9, 11, 12];
    arr6 = [1, 2, 3, 4, 5, 10, 12];
    print(merge_arrays(arr5, arr6))
