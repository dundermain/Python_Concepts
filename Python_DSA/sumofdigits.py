#This code is for sum of digits in Python using recursion

def sumofdigits(n):
    assert n>=0 and int(n)==n, "THe number has to be positive integer"
    if n==0:
        return 0
    
    else:
        return int(n%10) + sumofdigits(int(n//10))

        
print(sumofdigits(123))
print(sumofdigits(-123))