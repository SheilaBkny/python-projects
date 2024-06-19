'''
the steps:
1. create a starting dialogue, and allow the user to pick a range
2. use the random function to choose a number between the range.
3. calculate the min. number of guesses and store it
4. dialogue saying that the number is picked, and ask the user to pick a number
    - if number is higher than target: "Try again, you picked too high!"
    - if number is lower than target: "Try again, you picked too low!"
5. count the number of times that the user has inputted a number
    - if chances is less than or equal to the min. number of guesses: "Congratulations, you picked right!"
    - else: "Better luck next time!"
'''
import math
import random

# initialising the game play and getting upper/ lower bounds
print("This is the Number Guessing Game!")
lo = int(input("Pick a lower bound for your range: "))
up = int(input("Pick an upper bound for your range: "))
while up <= lo:
    up = int(input("Invalid upper bound. Choose another number: "))

print("Okay! Let's get started!")

# calculating the target num, and minimum guesses,
target = random.randint(lo, up)
min_guesses = math.log2(up - lo + 1)

# for testing purposes
print("the target number is: %d " % target)
print("the minimum number of guesses is %d" % min_guesses)

num_guesses = 1
user_guess = int(input("Try to guess the number that was chosen: "))


def in_range(guess):
    return guess <= lo or guess <= up


while num_guesses < min_guesses:
    num_guesses += 1
    if in_range(user_guess):
        if user_guess < target:
            user_guess = int(input("You picked too low! Try again: "))
        elif user_guess > target:
            user_guess = int(input("You picked too high! Try again: "))
        elif user_guess == target:
            print("Congratulations! You Won! The number was indeed %d!" % target)
            break
    else:
        user_guess = int(input("Invalid number. Choose another number in the range: "))


if user_guess != target:
    print("Better luck next time!")







