'''
Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''
Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.
'''
def namelist(names):
    if not names:
        return ''
    n = [x['name'] for x in names]
    le = len(n)
    if le == 1:
        return n[0]
    elif le == 2:
        return n[0] + ' & ' + n[1]
    else:
        return ', '.join(n[:-1]) + ' & ' + n[-1]
    
def namelist1(names):
    if len(names) > 1:
        return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]),
                                names[-1]['name'])
    elif names:
        return names[0]['name']
    else:
        return ''    
    
if __name__ == '__main__':
    print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}]), 'Bart, Lisa, Maggie, Homer & Marge',
    "Must work with many names")
    print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]), 'Bart, Lisa & Maggie',
    "Must work with many names")
    print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}]), 'Bart & Lisa',
    "Must work with two names")
    print(namelist([{'name': 'Bart'}]), 'Bart', "Wrong output for a single name")
#     print(namelist([]), '', "Must work with no names")
