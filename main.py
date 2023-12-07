import random

def pick_Interval(x,y):
    if x > y:
        temp = x
        x = y
        y = temp

print("Welcome to Guess the Number!")
print("I am thinking of a number from 1 to 100.")

num = random.randint(1,100)
guess = int(input("Guess the number: "))
count = 1

while num != guess:
    if guess > num:
        print("\033c")
        print("Too high!")
    if guess < num:
        print("\033c")
        print("Too low!")
    guess = int(input("Guess again: "))
    count += 1
print("You guessed correctly!")
print("It only took you " + str(count) + " tries.")
