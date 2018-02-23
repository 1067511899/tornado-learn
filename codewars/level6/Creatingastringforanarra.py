'''
You're given a string. You have a sequence of words separated with whitespaces. Let's say it is a sequence of patterns: a name and a corresponding number - like this:

"red 1 yellow 2 black 3 white 4"

You want to turn it into a list of objects you plan to work with later on - like this:

"[{name : 'red', id : '1'}, {name : 'yellow', id : '2'}, {name : 'black', id : '3'}, {name : 'white', id : '4'}]"

Doing this manually is a pain. So you've decided to write a short function that would make the computer do the job for you. Keep in mind, the pattern isn't necessarily a word and a number. Consider anything separeted by a whitespace, just don't forget: an array of objects with two elements: name and id.

As a result you'll have a string you may just copy-paste whenever you feel like defining a list of objects - now without the need to put in names, IDs, curly brackets, colon signs, screw up everything, fail searching for a typo and begin anew. This might come in handy with large lists.

It is also possible to make a function which would return a list of objects - another approach, deserving, as I believe, another kata.
'''
import collections
def words_to_object(s):
    res = []
    ss = s.split()

    tmp = len(ss)
    if tmp == 0:
        return []
    
    for x in range(0, tmp, 2):
        tmp1 = collections.OrderedDict()
        tmp1['name'] = ss[x]
        tmp1['id'] = ss[x + 1]

        res.append(tmp1)
    return res

if __name__ == '__main__':
    print(words_to_object("red 1 yellow 2 black 3 white 4"))
#     print(words_to_object("1 red 2 white 3 violet 4 green"))
#     print(words_to_object("1 1 2 2 3 3 4 4"),)
#     print(words_to_object("#@&fhds 123F3f 2vn2# 2%y6D @%fd3 @!#4fs W@R^g WE56h%"))
#     print(words_to_object(""), "[]")
