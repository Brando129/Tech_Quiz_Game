print("Hello! Welcome to my tech quiz.. I hope you brought your game face!")

playing = input("Would you like to give it a go? ")

if playing.lower() != "yes":
    quit()

print("Very well, let's play!")
score = 0

answer = input("What company was founded by Steve Jobs? ")
if answer.lower() == "apple":
    print("Well done, you are correct!")
    score += 1
else:
    print("Sorry, that's not the right answer.")


answer = input("What is the name of the gaming company that Microsoft owns? ")
if answer.lower() == "xbox":
    print("Correct!")
    score += 1
else:
    print("I'm afraid thats not the right answer. Let's try another.")


answer = input("Which computer language has the logo of a snake? ")
if answer.lower() == "python":
    print("Very good, you're right!")
    score += 1
else:
    print("Not quite, sorry.")


answer = input("In what year was the Nintendo Gamecube released in America? ")
if answer == "2001":
    print("Nice job! That was a tough one. ")
    score += 1
else:
    print("Incorrect!")

print("Okay, and the final question is...")

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Congratulations, that's right! ")
    score += 1
else:
    print("Ohh, I don't think thats right. Sorry!")

print("Thank you for playing my tech quiz! You scored " +str(score) + " out of 5!")