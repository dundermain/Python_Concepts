#Here we will discuss about encapsulation and abstarction

#Encapsulation is a mechanism of hiding of data implementation. Instance variables/methods can be hidden or made private. 
#This can only be accessed by accessor 

class SoftwareEngineer:

    def __init__(self, name, age):
        self.name = name
        self.age =  age

        #Lets salary and number of bugs solved attribute to private
        # One underscore (e.g _x) is called "protected attribute"
        #double underscore (e.g. __x) is called "private attribute"
        self._salary =  None
        self._num_bugs_solved = 0
        
    #now lets assume someone wants to access the private tags
    def get_salary(self):
        return self._salary
    
    def set_salary(self, value):
        self._salary = value



se = SoftwareEngineer("Max", 25)
print(se.age, se.name)
se.set_salary(6000)
print(se.get_salary())
