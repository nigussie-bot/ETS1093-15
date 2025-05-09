# Create class
class sew:  
    def __init__(self, name, age):  
        self.name = name
        self.age = age

    def myfunc(self):
        print('My name is ' + self.name) 
        print('I am ' + str(self.age) + ' years old')
   #inheried from fist class     
class lij(sew):
    pass       
#object  

me = sew('biifado', 24)  
me.myfunc()



p2 = sew('roza', 90)  
p2.myfunc()

