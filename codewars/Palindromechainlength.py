'''
Number is a palindrome if it is equal to the number with digits in reversed order. For example, 5, 44, 171, 4884 are palindromes and 43, 194, 4773 are not palindromes.

Write a method palindrome_chain_length which takes a positive number and returns the number of special steps needed to obtain a palindrome. The special step is: "reverse the digits, and add to the original number". If the resulting number is not a palindrome, repeat the procedure with the sum until the resulting number is a palindrome.

If the input number is already a palindrome, the number of steps is 0.

Input will always be a positive integer.

For example, start with 87:

87 + 78 = 165; 165 + 561 = 726; 726 + 627 = 1353; 1353 + 3531 = 4884

4884 is a palindrome and we needed 4 steps to obtain it, so palindrome_chain_length(87) == 4
'''
def is_palindrome(n):  
    n = str(n)  
    m = n[::-1]  
    return n == m


def palindrome_chain_length(n):  
    count = 0
    while True:
        tmp = str(n)
        m = tmp[::-1]
        if m == tmp:
            return count
        else:
            count += 1
            n = int(m) + n
# 下面是最好的（我认为）的答案，我就是写不出这么简洁的代码
def palindrome_chain_length1(n):
    steps = 0
    while str(n) != str(n)[::-1]:
        n = n + int(str(n)[::-1])
        steps += 1
    return steps

if __name__ == '__main__':
    print(palindrome_chain_length(87))
