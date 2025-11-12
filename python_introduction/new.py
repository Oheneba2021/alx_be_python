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

rows = 5
i = 1

while i <= rows:
    space = 1
    while space <= rows - i:
        print(" ", end="")
        space += 1
    star = 1
    while star <= (2 * i -1):
        print("*", end="")
        star += 1
    print()
    i += 1
        
