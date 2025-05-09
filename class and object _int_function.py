class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

fc = Person('mosh', 26)
print(fc.name)
print('your age is '+str(fc.age))
