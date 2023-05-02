#  Create a program that will cycle through a list until the correct number is printed (Have the user pick a number)
#  SHOULD DO:
import random


user = input("Pick a number 1-10:")
while True:

    cycle = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    number = random.choice(cycle)

    if number == user:
        print("\nYour number was ⇒", user)
        quit()

    elif number != user:
        print(random)
        print("Trying Again!")
