#This code is for factorial calculation using recursion

#n = int(input("Enter the number:")

def factorial(n):
    assert n>=0 and int(n)==n
    if n in [0,1]:
        return 1
    else:
        return n*factorial(n-1)