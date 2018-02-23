'''
Imagine we have ATM with many currencies. User can get money of any currency ATM has.

Our function must analyze currency and value of what users wants and give money to user starting from bigger values to lesser.

This KATA has preloaded dictionary of possible bank note values for different currencies.

VALUES = {'EUR': [5, 10, 20, 50, 100, 200, 500], '...':'...'}
Function must return string containing how many bank notes of each value ATM will give out like this:

8 * 100 USD, 2 * 20 USD, 1 * 2 USD
If it can't do that because it has no notes for this value, it returns See tests.

"Can't do *value* *currency*. Value must be divisible by *something*!"
If it hasn't requested currency at all, it returns

"Sorry, have no *currency*."
See testcases for user input samples. Note that 'EUR 1000' and '1000eur' are the same.

Note that you shouldn't create your own VALUES dictionary or you'll get tests broken.

Tested on Python 3.5. PS: Sorry for bad English.
'''
import re
VALUES = {'EUR': [5, 10, 20, 50, 100, 200, 500], 'RMB': [2, 5, 10, 20, 50, 100]}
def atm(value):
    sp = re.findall('[\d]?', value)
    print(sp)
    return None


if __name__ == '__main__':
    print(atm('XSF 1000'), 'Sorry, have no XSF.')
    print(atm('rub 12341'), 'Can\'t do 12341 RUB. Value must be divisible by 10!')
    print(atm('10202UAH'), '20 * 500 UAH, 2 * 100 UAH, 1 * 2 UAH')
    print(atm('842 usd'), '8 * 100 USD, 2 * 20 USD, 1 * 2 USD')
    print(atm('euR1000'), '2 * 500 EUR')
    print(atm('sos100'), 'Can\'t do 100 SOS. Value must be divisible by 1000!')
