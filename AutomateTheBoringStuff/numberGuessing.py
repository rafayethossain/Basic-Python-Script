import random

print("Hello! What is you name?")
name = input("> ")

print("Well, " + name + "I am thinking of a number between 1 and 20.")

secretNumber = random.randint(1, 20)

for gueessTaken in range(1, 7):
    print("Take a guess.")
    guess = int(input("> "))

    if guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print(" Your guess is too high.")
    else:
        break #This condition is for correct guess

if guess == secretNumber:
    print("Good job!" + name + "you gueesed my number in" + str(gueessTaken)+"guesses!" )
else:
    print("Nope! The number I was thinking was: " + str(secretNumber)) 
