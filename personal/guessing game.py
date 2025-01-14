import random
print("Hi! I'm going to try to guess your age")
name = input("What's your name?")
guessed = False
while(guessed == False):
    guess = random.randint(15,30)
    response = input("Are you"+str(guess) + "years old?")
    if response == "yes":
        guessed = True
        print("I guessed it! You're" + str(guess) + "years old")
    if response == "no":
        print("I'll try again")