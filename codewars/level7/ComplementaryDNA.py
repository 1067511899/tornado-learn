'''
Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

If you want to know more http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You have function with one side of the DNA (string, except for Haskell); you need to get the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

DNA_strand ("ATTGC") # return "TAACG"

DNA_strand ("GTAT") # return "CATA"
'''


dnadic = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
def DNA_strand(dna):
    result = ''
    for x in dna:
        result += dnadic[x]
    return result


def DNA_strand1(dna):
    return dna.translate(dna.maketrans("ATCG", "TAGC"))
'''
static str.maketrans(x[, y[, z]])
This static method returns a translation table usable for str.translate().

If there is only one argument, it must be a dictionary mapping Unicode ordinals (integers) or characters (strings of length 1) to Unicode ordinals, strings (of arbitrary lengths) or None. Character keys will then be converted to ordinals.

If there are two arguments, they must be strings of equal length, and in the resulting dictionary, each character in x will be mapped to the character at the same position in y. If there is a third argument, it must be a string, whose characters will be mapped to None in the result.
'''
    
pairs = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
def DNA_strand2(dna):
    return ''.join([pairs[x] for x in dna])


if __name__ == '__main__':
    print(DNA_strand1("GTAT"))
