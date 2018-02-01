'''
Complete the method so that it does the following:
Removes any duplicate query string parameters from the url
Removes any query string parameters specified within the 2nd argument (optional array)
Examples:
stripUrlParams('www.codewars.com?a=1&b=2&a=2') // returns 'www.codewars.com?a=1&b=2'
stripUrlParams('www.codewars.com?a=1&b=2&a=2', ['b']) // returns 'www.codewars.com?a=1'
stripUrlParams('www.codewars.com', ['b']) // returns 'www.codewars.com'
1、删除重复的参数，比如有两个 a=，那么只保留最前面的一个。
2、删除第二个参数里面标注的参数，比如['b']，那么删除 参数b。
有实际应有价值。
'''
import re


def checkinside(par, url=[]):
    if url == []:
        return True
    for x in url:
        if re.split('=', x)[0].strip() == re.split('=', par)[0].strip():
            return False
    return True
    

def strip_url_params(url, params_to_strip=[]):
    tmp = re.split('\?', url)

    if len(tmp) <= 1:
        return url
    
    para = re.split('&', tmp[1])
    
    last = []
    for x in para:
        if checkinside(x, last):
            last.append(x)
     
    last1 = []
    if params_to_strip != []:
        for y in last:
            if re.split('=', y)[0] in params_to_strip:
                pass
            else:
                last1.append(y)
    else:
        last1 = last             

    return tmp[0] + '?' + '&'.join(last1)


# 总有人代码写的这么牛逼            
def strip_url_params1(url, params_to_strip=[]):
    if '?' not in url:
        return url
    hier, query = url.split('?')
    params = {}
    for param in query.split('&'):
        k, v = param.split('=')
        if k not in params and k not in params_to_strip:
            params[k] = v
    return '{0}?{1}'.format(hier, '&'.join('='.join(kv) for kv in params.items()))
        

if __name__ == '__main__':
    print(strip_url_params('www.codewars.com', ['b']))
