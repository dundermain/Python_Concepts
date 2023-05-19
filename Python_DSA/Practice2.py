'''
This script is developed to practice some DSA questions
Date: 06/03/2023
'''

#which of the follwing is NOT equivalent ot O(N)
    #O(N+P) where P<N/2
    #O(2N)
    #O(N + logN)
    #O(N + NlogN) (ANSWER)
    #O(N+M) (Dont neglect M from here as it can be anything)

#Find the runtime of the below code
def factorial(n):
    if n < 0:
        return -1
    elif n == 0:
        return 1
    else:
        return n*factorial(n-1)
#answer is O(N)
    
#FInd the runtime for the following algorithm
def allFib(n):
    for i in range(n):
        print(str(i)+ ":,"+ str(fib(i)))

def fib(n):
    if n <=0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)  
#answer is O(2^n)

#Find the runtime of following code
def powerOf2(n):
    if n < 1:
        return 0
    
    elif n == 1:
        print(1)
        return 1
    
    else:
        prev = powerOf2(int(n/2))
        curr = prev*2
        print(curr)
        return curr
#ans is O(logN) as the recursion is decreasing at the rate of 2
