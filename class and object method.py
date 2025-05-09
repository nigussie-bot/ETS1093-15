 # Create class
class Person:  
    def __init__(self, name, age):  
        self.name = name
        self.age = age

    def myfun(self):
        print('My name is ' + self.name) 
        print('I am ' + str(self.age) + ' years old') 
#object
me = Person('Dagnesh', 24)  
me.myfun()

p2 = Person('Duguna', 76)  
p2.myfun()

p3=Person('duguna',60) #editing the year of duguna
p3.myfun()
  
    
