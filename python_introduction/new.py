# import random
# day = input("Enter a day of the week (Monday - Sunday)").lower()
# match day:
#     case "monday":
#         print("Ugh, Mondays ....")
#     case "tuesday":
#         print("Just another workday... ")
#     case "wednesday":
#         print("Hump day!")
#     case "thursday":
#         print("Almost there...")
#     case "friday":
#         print("TGIF!")
#     case "saturday"|"sunday":
#         print("Weekend vibes!")
#     case _:
#         print("Invalid day entered.")
        
# value = input("Enter a value (number or string):")
# match value:
#     case int():
#         print("You entered an integer:", value)
#     case str():
#         print("You entered a string:", value)
#     case _:
#         print("Invalid data type entered")
        

# user = bool(input("Do you have a valid ID? (true/false)").lower() == "true")

# has_id = user

# age = int(input("Enter your age"))

# match age:
#     case 18 | 19:
#         if age >= 18 :
#             print("You are eligible to vote")
#         else:
#             print("You need a valid ID to vote")
#     case _:
#         print("You are not yet eligible to vote")

# secret_number = random.randint(1, 10)
# guess = int(input("I am thinking of a number between 1 and 10. Can you guess it?"))
# match guess:
#     case _ if guess > secret_number:
#             print("Nope! Too high")
#     case _ if guess < secret_number:
#             print("Nope! Too low")
#     case _ if guess == secret_number:
#             print("Congratulations! You guessed it right.")
#     case _:
#         print("Invalid input. Please enter a number between 1 and 10.")
    
#     #  for loops
# fruits = ["apple", "banana", "mangoes","Cherry"]

# for fruit in fruits:
#     print(fruit)
    
# colors = ("red", "blue", "green")
# for color in colors:
#     print(color)

# message = "Hello, world!"
# for character in message:
#     print(character)
    
# for number in range(1, 6):
#     print(number)

# numbers = [1, 5, 3, 9]

# total = 0
# for  num in numbers:
#     total += num
# print("Numbers:", numbers)
# print("Total sum:", total)

# # while loops
# age = 0

# while age < 18:
#     age = int(input("Enter your age (must be 18 or older)"))
    
# print("You are old enough to proceed.")


# secret_number = 7

# guess_count = 0
# guess = 0

# while guess != secret_number:
#     guess_count += 1
#     guess = int(input("Guess a number between 1 and 10:"))
    
# print(f"You guessed it in {guess_count} tries!")

# shopping_list = ["apples", "bread", "milk", "cheese", ]
# item_found = False

# while not item_found:
#     item = input("Search for an item in your lists(or 'q' to quit):")
#     if item.lower() == "q":
#         break
#     if item in shopping_list:
#         item_found = True
#         print(f"{item} is in your shopping list!")
#     else:
#         print(f"{item} is not in your shopping list. Try again.")

# outer_count = 5

# while outer_count > 0:
#     inner_count = 1
#     while inner_count <= outer_count:
#         print(inner_count, end=" ")
#         inner_count += 1
#     print()
#     outer_count -= 1

# for i in range(1, 11):
#     for j in range(1, 11):
#         product = i * j
#         print(i, "x", j, "=", product, end="\t")
#     print()

# rows = 25

# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()

# rows = 5
# i = 1

# while i <= rows:
#     space = 1
#     while space <= rows - i:
#         print(" ", end="")
#         space += 1
#     star = 1
#     while star <= (2 * i -1):
#         print("*", end="")
#         star += 1
#     print()
#     i += 1

# add = lambda x, y: (2*x) + y/
# result = add(5, 3)
# print(result)        


# def calculate_area(length, width):
#     '''Calculate the area of a rectangle.'''
#     area = length * width
#     return area

# result = calculate_area(5, 3)
# print("Area of rectangle:", result)


# def user_info(name, age=None):
#     """Prints user information."""
#     print(f"Name: {name}")
#     if age:
#         print(f"Age: {age}")
# user_info("Alice", 30)


# Function definition with default value
# def greet(name="World"):
#     """Prints a greeting message,"""
#     print(f"Hello, {name}!")
# greet()
# greet("Alice")

# def square(number):
#     """Returns the square of a number."""
#     return number * number
# squared_value = square(4)
# print("Squared value:", squared_value)

# count = 0 #global variable
# def increment():
#     count += 1 #this refers to the local count within the function
#     increment()
# print("Count value:", count)

# count = 0  # global variable
# def increment_global():
#     global count
#     count += 9
# increment_global()
# print("Count value:", count)

# def outer_function():
#     x = 10 # enclosing variable
#     def inner_function():
#         nonlocal x #using nonlocal to modify enclosing variable
#         x += 5 # modify enclosing variable
#     inner_function()
#     print("Modified value of x from inner function:", x)
# outer_function()

# def greet_user(name):
#     """Greets the user by name."""
#     print("Greetings,", name,  "!" )
# greet_user("Bob")

# def area_of_rectangle(length, width):
#     """Calculates the area of a rectangle"""
#     return length * width
# print("Area of rectangle:", area_of_rectangle(4, 6))

# def check_even_odd(number):
#     """Checks if a number is even or odd."""
#     if number % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
# print("5 is", check_even_odd(5))


#Data Structure: Tuples, sets and Dictionaries
# # Tuples - immutable ordered containers
# a = (3,5,6,'asdf')
# print(a)
# print(type(a))

# print(a[0])  # Accessing elements
# print(a[::2]) # Slicing
# #a[1] = 10  # This will raise an error since tuples are immutable

# b = list(a)  # Converting tuple to list
# print(b)
# b[1] = 10  # Modifying the list
# print(b)
# a = tuple(b)  # Converting back to tuple
# print(a)

# b = set(a)  # Converting tuple to set
# print(b)

# # Sets - unordered collections of unique elements
# s = {3,4,5,6,7,7,7,7,7,7,7,7,7}
# print(s)
# print(type(s))

# b = set()
# print(b)

# a = {3,4,5}
# b = {4,5,6,7,8,9,6,6,5,4}
# print(b)
# c = a.intersection(b)
# print(c)
# d = a.union(b)
# print(d)
# e = 8 
# print(e in b)
# print(e in a)
# f = b.difference(a)
# print(f)


# x = {3,4,5,6}
# y = {5,4,3,6}
# print(x == y)  # True, since sets are unordered and contain the same elements
# print(x is y)  # False, since they are different objects in memory

# c = list(y)
# print(c)

# c = [3,4,5,6,6,7,7,8,8]
# print(c)
# d = set(c)
# print(d)
# e = list(d)
# print(e)

# # Dictionaries - key-value pairs
# ydict = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
# print(ydict)
# print(type(ydict))  
# print(ydict['k1'])  # Accessing values by key
# ydict['k1']=True  # Modifying values
# print(ydict)
# ydict['k4'] = 'v4'  # Adding new key-value pairs
# print(ydict)
# del ydict['k2']  # Deleting key-value pairs
# print(ydict)
# print(ydict.keys())  # Getting all keys
# print(ydict.values())  # Getting all values
# print(ydict.items())  # Getting all key-value pairs

# xdict = {1:1, 2:3, 3:3}
# print(xdict)
# ydict.

# Modules and Packages
# classes in python

# class Student:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.current_class = "10th Grade"
        
    

#     def approved(self):
#         print(f"{self.first_name} {self.last_name} has been approved and admitted to {self.current_class} ")
        
#     def withdrawn(self):
#         print(f"{self.first_name} {self.last_name} has been withdrawn from {self.current_class} ")
        
# student1 = Student("Godwin", "Boakye", 12)

# is_approved = True
# def process_student(student, approved):
#     if approved:
#         student.approved()
#     else:
#         student.withdrawn()
# process_student(student1, is_approved)

# class FileHandler:
#     def __init__(self, filename):
#         self.filename = filename
#         self.file = open(filename, 'r')
        
#     def read_data(self):
#         return self.file.read()
    
#     def __del__(self):
#         self.file.close()
#         # close the file when the object is destroyed 
    
# #create an instance or object of FileHandler
# file_object = FileHandler ("testfile.txt")
# print(file_object.read_data())

# # object is no longer needed, it will be garbage collected, and __del__ method will be called automatically to close the file 

# # __str__ and __repr__ methods
# class Point:
#     def __init__(self, x = str, y =str):
#         self.x = x
#         self.y = y
        
#     def __str__(self):
#         return (f"Point({self.x}, {self.y})")
    
#     def __repr__(self):
#         return (f"Point(x={self.x}, y={self.y})")
# point1 = Point('3', '4')
# print(point1)  # Calls __str__ method
# print(repr(point1))  # Calls __repr__ method

# # Inheritance
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
    
#     def car_origin(self, origin):
#         super().__init__()
#         self.origin = origin
#         return f"{self.make} {self.model} is manufactured in {self.origin}."

# Car1 = Car("Toyota", "Tacoma", 2020)
# print(Car1.car_origin("USA"))

# # Composition as an alternative to inheritance
# class Engine(Car):
#     def __init__(self, make, model, year, horsepower):
#         super().__init__(make, model, year)
#         self.horsepower = horsepower
    
#     def start(self):
#         return f"{self.make} Engine started."

# start_engine = Engine.start(Car1)
# print(start_engine)

# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
    
#     def make_sound(self, sound):
#         return f"{self.name} the {self.species} says {sound}"

# class Dog(Animal):
#     def make_sound(self,):
#         return "Woof!"
    
# dog1 = Dog("Buddy", "Dalmatian")
# print(dog1.make_sound())

# # multiple inheritance
# class Flyer:
#     def fly(self):
#         return "Flying high!"   

# class swimmer:
#     def swim(self):
#         return "Swimming fast!"

# class Duck(Flyer, swimmer):
#     pass

# duck1 = Duck()
# print(duck1.fly())  
# print(duck1.swim()) 

# # multilevel inheritance
# class Vehicle:
#     def move(self):
#         print("Moving...")

# class NewCar(Vehicle):
#     pass

# class ElectricCar(NewCar):
#     def charge(self):
#         print("Charging...")
        
# tesla = ElectricCar()
# tesla.move() #Moving...
# tesla.charge() #Charging...

# # Method Resolution Order (MRO)
# class A:
#     def greet(self):
#         return " Hello from class A"

# class B(A):
#     def greet(self):
#         return "Hello from  class B"
    
# class C(A):
#     def greet(self):
#         return "Hello from class C"
    
# class D(B, C):
#     pass

# # Creating an instance of class D
# d_instance = D()

# print(d_instance.greet())  # Output: Hello from class B

# # polymorphism

# class Animal:
#     def make_sound(self):
#         print("Some generic animal sound")

# class Cat(Animal):
#     def make_sound(self):
#         print("meow")

# class Cow(Animal):
#     def make_sound(self):
#         print("moo")

# class Dog(Animal):
#     def make_sound(self):
#         print("woof")

# animals = [Cat(), Cow(), Dog()]

# for each_animal in animals:
#     each_animal.make_sound() 


# # polymorphic behavior with duck typing 
# class Duck:
#     def quack(self):
#         return "Duck quacks"
# class Person: 
#     def quack(self):
#         return "Person imitates a duck"
    
# def make_sound(obj):
#     return obj.quack()

# duck_object = Duck()
# person_object = Person()

# print (make_sound(duck_object))  # Output: Duck quacks
# print (make_sound(person_object))  # Output: Person imitates a duck

# # practice exercise 
# # single inheritance instruction 

# class Shape:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width  
    
#     def calculate_area(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self, length, width):
#         super().__init__(length, width)
        
#     def calculate_area(self):         
#         return self.length * self.width
         
# new_rectangle = Rectangle(5, 3)
# print ("Area of rectangle:", new_rectangle.calculate_area())

# @classmethod

class Person:
    count = 0 #Class variable to count instances
    
    def __init__(self, name):
        self.name = name
        Person.count += 1 # Increment count on instannce creation
    
    @classmethod
    def display_count(cls):
        print(f"Total persons created: {cls.count}")
    
    
# Usage
person1 = Person("Alice")
person2 = Person("Bob")
person3 = Person("Dessy")
person4 = Person("Godwin")
person5 = Person("Esi")
person6 = Person("Kofi")
person7 = Person("Ama")


Person.display_count()


# @static Methods
class MathUtils:
    @staticmethod
    def add(a,b):
        return a + b
    
    @staticmethod
    def multiply(a,b):
        return a * b

# Usage
print("Addition:", MathUtils.add(5, 3))
print("Multiplication:", MathUtils.multiply(5, 3))


class A:
    def rk(self):
        print("In class A")

class B(A):
    def rk(self):
        print("In class B")
        
class C(A):
    def rk(self):
        print("In Class C")

class D(B, C):
    pass        

r = D()
r.rk()  # Output: In class B


