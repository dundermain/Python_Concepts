'''
FInd the results of exponents
'''

def power(x, n):
    assert int(n)==n, 'The exponent shpuld be integer'

    if n == 0:
        return 1
    
    elif n<0:
        return 1/x * power(x, n+1)
    
    else:
        return x * power(x, n-1)
    

print(power(2,3))
