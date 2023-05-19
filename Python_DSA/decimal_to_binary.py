'''
Decimal to Binary conversion can be done by dividing the number by 2 until the quotient is 0. The total remainder in each case corresponds to binary
'''

def decimal2binary(n):
    assert int(n) == n, 'The parameter must be an integer only'

    if n == 0:
        return 0
    else:
        return n%2 + 10*decimal2binary(int(n/2))
    

print(decimal2binary(16))