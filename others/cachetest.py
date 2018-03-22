from functools import lru_cache
import urllib
import urllib.request
from requests.exceptions import HTTPError


@lru_cache(maxsize=32)
def get_pep(num):
    'Retrieve text of a Python Enhancement Proposal'
    resource = 'http://www.python.org/dev/peps/pep-%04d/' % num
    try:
        with urllib.request.urlopen(resource) as s:
            return s.read()
    except Exception as e:
        print(e)
        print(isinstance(e, BaseException))
        return e

    
# for n in 8, 9991:
n = 9991
pep = get_pep(n)
if not isinstance(pep, urllib.error.HTTPError):
    print(n, len(pep))

print(get_pep.cache_info())
