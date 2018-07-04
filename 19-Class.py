'''
   ### Object Oriented Programing ###

Class:-> A collection of ,attributes that are defined for any object data
            members,methods
         Template for creating objects.All objects crated using the same class
Object:-> An Instance of a class.
Instantiate:->Create an defined of a class.
Method:-> A function defined in a class.
attribute:->A Variable bound to an Instance of a class

'''
# Simple class
# use class keyword
# And __init__() method is important
class narsi:
    def __init__(self,name,age):
        self.name=name
        self.age=age

get=narsi('narsighost',20)               # Here create get  instantion_object of narsi class
print(get.name)
print(get.age)


# Class Method
class cal:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        a=self.a+self.b
        print('sum=',a)


vals=cal(7,8)
vals.add()
