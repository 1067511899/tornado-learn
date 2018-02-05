'''
You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

#Examples:

runBF("test\0") should return "es"

runBF("testing\0") should return "t"

runBF("middle\0") should return "dd"

runBF("A\0") should return "A"
#Input

A word (string) of length 0 < str < 200 For BF, all the input strings end with "\0". You do not need to test for this. This is only here to tell you that you do not need to worry about your solution timing out.

#Output

The middle character(s) of the word represented as a string.
'''
def get_middle(s):
    le = len(s)
    tmp = le // 2
    if le % 2 == 0:
        return s[tmp - 1:tmp + 1]
    return s[tmp]
# 最精简答案
def get_middle1(s):
   return s[(len(s) - 1) / 2:len(s) / 2 + 1]

if __name__ == '__main__':
    print(get_middle('midle'))
