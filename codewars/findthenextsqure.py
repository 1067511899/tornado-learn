'''
Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the parameter is itself not a perfect square, than -1 should be returned. You may assume the parameter is positive.

Examples:

findNextSquare(121) --> returns 144
findNextSquare(625) --> returns 676
findNextSquare(114) --> returns -1 since 114 is not a perfectovo
'''
from Testmodule import Test
import math

def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    sqr=int(math.sqrt(sq))
    if sqr**2==sq:
        return (sqr+1)**2
    
    return -1

if __name__=='__main__':
    Test=Test()
    Test.assert_equals(find_next_square(121), 144, "Wrong output for 121")
    Test.assert_equals(find_next_square(625), 676, "Wrong output for 625")
    Test.assert_equals(find_next_square(319225), 320356, "Wrong output for 319225")
    Test.assert_equals(find_next_square(15241383936), 15241630849, "Wrong output for 15241383936")

    Test.assert_equals(find_next_square(155), -1, "Wrong output for 155")
    Test.assert_equals(find_next_square(342786627), -1, "Wrong output for 342786627")
