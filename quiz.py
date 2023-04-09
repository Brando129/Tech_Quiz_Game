import time 
import random
# need to set up  random functionality
# need to add  more questions
# make the game more universal for different kinds of trivia

print("Hello! Welcome to my tech quiz.. I hope you brought your game face!")

time.sleep(3)
playing = input("Would you like to give it a go? ")

if playing.lower() != "yes":
    quit()

time.sleep(1)
print("Great, let's get started!")
score = 0

time.sleep(2)
answer = input("What company was founded by Steve Jobs? ")
if answer.lower() == "apple":
    time.sleep(1)
    print("Well done, you are correct!")
    score += 1
else:
    time.sleep(1)
    print("Sorry, that's not the right answer.")

time.sleep(2)
answer = input("What is the name of the gaming company that Microsoft owns? ")
if answer.lower() == "xbox":
    time.sleep(1)
    print("Correct!")
    score += 1
else:
    time.sleep(1)
    print("I'm afraid thats not the right answer. Let's try another.")

time.sleep(2)
answer = input("Which computer language has the logo of a snake? ")
if answer.lower() == "python":
    time.sleep(1)
    print("Very good, you're right!")
    score += 1
else:
    time.sleep(1)
    print("Not quite, sorry.")

time.sleep(2)
answer = input("In what year was the Nintendo Gamecube released in America? ")
if answer == "2001":
    time.sleep(1)
    print("Nice job! That was a tough one. ")
    score += 1
else:
    time.sleep(1)
    print("Incorrect!")

time.sleep(2)
print("Okay, and the final question is...")

time.sleep(2)
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    time.sleep(1)
    print("Congratulations, that's right! Lets tally up your score. ")
    score += 1
else:
    time.sleep(1)
    print("Ohh, I don't think thats right. Sorry! Lets tally up your score.")

time.sleep(2)

print("Thank you for playing my tech quiz! You scored " +str(score) + " out of 5!")