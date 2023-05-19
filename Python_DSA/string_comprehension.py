'''
To find out if the string contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters. 

Python has built in functins for certain string operations like

str.isalnum()
This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).

str.isalpha()
This method checks if all the characters of a string are alphabetical (a-z and A-Z).

str.isdigit()
This method checks if all the characters of a string are digits (0-9).

str.islower()
This method checks if all the characters of a string are lowercase characters (a-z).

str.isupper()
This method checks if all the characters of a string are uppercase characters (A-Z)

task is to find out if the string contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters. 

'''

string = input()

    
    for char in string:
        if char.isalnum():
            alnum = True
            break
        else:
            alnum = False
            
    for char in string:
        if char.isalpha():
            alpha = True
            break
        else:
            alpha = False
            
    for char in string:
        if char.isdigit():
            digit = True
            break
        else:
            digit = False
            
            
    for char in string:
        if char.islower():
            lower = True
            break
        else:
            lower = False
            
            
    for char in string:
        if char.isupper():
            upper = True
            break
        else:
            upper = False
    print(alnum) 
    print(alpha) 
    print(digit) 
    print(lower) 
    print(upper) 
