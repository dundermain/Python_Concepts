'''
Greatest common divisor

generally done by euclidean algorithm which states that GCD of two number also divides the difference. 
Example:

gcd(48,18):
    step 1: 48/18 = 2 remainder 12
    step 2: 18/12 = 1 remainder 6
    step 3: 12/6 = 2 remainder 0

Hence, gcp(48, 18) is 6
'''

def gcd(a , b):
    assert int(a)==a and int(b)==b, 'The numbers must be integer only'

    if a < 0:
        a = -1*a

    if b<0:
        b = -1*b
    
    if b == 0:
        return a
    
    else:
        return gcd (b, a%b)


print(gcd(48,18))