import random
print("Hi! I'm going to try to guess your age")
name = input("What's your name?")
guesses = []
guessed = False
while(guessed == False):
    guess = random.randint(15,30)
    if guess in guesses:
        continue
    response = input("Are you"+str(guess) + " years old?")
    if response == "yes":
        guessed = True
        print("I guessed it! You're" + str(guess) + " years old")
    if response == "no":
        print("I'll try again")
        guesses.append(guess)