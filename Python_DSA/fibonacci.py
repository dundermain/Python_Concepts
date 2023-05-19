#this code is for fibonaaci sequence using recursion
#n = int(input("Enter the number:"))


def fibonacci(n):
    #asserting the nummber to be greater than 0 and an integer
    assert n>=0 and int(n)==n
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
        
print(fibonacci(11))