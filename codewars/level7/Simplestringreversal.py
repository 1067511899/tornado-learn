'''
In this Kata, we are going to reverse a string while maintaining spaces.

For example:

solve("our code") = "edo cruo"
-- Normal reversal without spaces is "edocruo". 
-- However, there is a space after the first three characters, hence "edo cruo"

solve("your code rocks") = "skco redo cruoy"
solve("codewars") = "srawedoc"
More examples in the test cases. All input will be lower case letters and in some cases spaces.

Good luck!
'''
def solve(s):
    return [x[::-1] for x in s.split()][::-1]


if __name__ == '__main__':
    print(solve("your"), "skco redo cruoy")
