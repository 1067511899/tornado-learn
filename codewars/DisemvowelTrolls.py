def disemvowel(string):
    tmp=''
    for t in string:
        x=t.lower()
        if (x=='a' or x=='e' or x=='i' or x=='o' or x=='u'):
            continue
        else:
            tmp+=t
    return tmp

def disemvowel1(s):
    return s.translate(str.maketrans('', '', 'aeiouAEIOU'))


if __name__ == '__main__':
    print(disemvowel1("This website is for losers LOL!"))