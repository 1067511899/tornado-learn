'''
An Arithmetic Progression is defined as one in which there is a constant difference between the consecutive terms of a given series of numbers. You are provided with consecutive elements of an Arithmetic Progression. There is however one hitch: exactly one term from the original series is missing from the set of numbers which have been given to you. The rest of the given series is the same as the original AP. Find the missing term.

You have to write the function findMissing(list), list will always be at least 3 numbers. The missing term will never be the first or last one.

Example :

findMissing([1,3,5,9,11]) == 7
PS: This is a sample question of the facebook engineer challenge on interviewstreet. I found it quite fun to solve on paper using math, derive the algo that way. Have fun!

不知道哪里有问题

'''
def find_missing(sequence):
    le = len(sequence)
    step = 0
    print(sequence[0], sequence[-1])
    if sequence[0] > 0:
        step = (sequence[0] + sequence[-1]) // le
#         print(step)
    else:
        step = (sequence[-1] - sequence[0]) // le
#     print(step)
    for x in range(1, le):
        if sequence[x] - sequence[x - 1] != step:
            return sequence[x - 1] + step



if __name__ == '__main__':
    print(find_missing([-9, -8, -7, -6, -4, -3]))
