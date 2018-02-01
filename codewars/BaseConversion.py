'''
can assume that the input value always consists of characters from the source alphabet. You don't need to validate it.

Examples
convert("15", dec, bin)       ==>  "1111"
convert("15", dec, oct)       ==>  "17"
convert("1010", bin, dec)     ==>  "10"
convert("1010", bin, hex)     ==>  "a"
convert("0", dec, alpha)      ==>  "a"
convert("27", dec, allow)     ==>  "bb"
convert("hello", allow, hex)  ==>  "320048"
Additional Notes:

The maximum input value can always be encoded in a number without loss of precision in JavaScript. In Haskell, intermediate results will probably be too large for Int.
The function must work for any arbitrary alphabets, not only the pre-defined ones
You don't have to consider negative numbers
简单的说,给你的参数,第一个是数字,第二个是数字当前的进制,第三个是要转换 成 的进制.
'''
def convert(input, source, target):
    pass

if __name__ == '__main__':
    s = 'hello'
    print(id(s))