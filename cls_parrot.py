class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))



#Methods
#Methods are functions defined inside the body of a class.
#They are used to define the behaviors of an object.
class Parrot:
    
    # instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # instance method
    def sing(self, song):
        return print(f'{self.name} sings {song}')

    def dance(self):
        return print(f"{self.name} is now dancing")

# instantiate the object
blu = Parrot("Blu", 10)

# call our instance methods
print(blu.sing("'Happy'"))
print(blu.dance())

#Inheritance
# Inheritance is a way of creating new class for using details of existing class without modifying it.
#The newly formed class is a derived class (or child class). Similarly, the existing class is a base 
#class (or parent class).
# parent class
class Bird:
    
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class
class Penguin(Bird):

    def __init__(self):
        #call super() function. We want to pull the content of __init__()
        #method from the parent class into the child class.
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()

#Encapsulation
#Using OOP in Python, we can restrict access to methods and variables.
#This prevent data from direct modification which is called encapsulation.
#In Python, we denote private attribute using underscore as prefix i.e single “ _ “ or double “ __“.

class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price but this doesnt work because of __maxprice is a private attribute.
# We have to use the setter function
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()


#Polymorphism
#Polymorphism is an ability (in OOP) to use common interface for multiple form (data types).
class Parrot:

    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

class Penguin:

    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")

# common interface
def flying_test(bird):
    bird.fly() #Common method between Peguin and Parrot class

#instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)