def sqrt(x):
    y = 1.0
    while abs(y*y - x) > 1e-6 :
        print(y)
        y=(y+x/y)/2
    return y
    
if __name__=='__main__':
    print(sqrt(99))
    
