import math

z = [3, 1, -3]

m = []

for x in z:
    m.append(math.exp(x))
    
print(sum(m))

for x in m:
    print('%.2f' % round(x / sum(m), 2))
