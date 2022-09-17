from socket import SocketIO


print("Welcome to The Riddle")

playingGame = input("Do you want to play? ")
score = 0

if playingGame.lower() != "yes":
    print("I guess your a pussy, or you cant spell yes. xD")
    quit()

print("Okie Dokie, Let the game begin ... :D")

#Q1
answer = input("What word is spelled incorrectly in every single dictionary? ")
if answer.lower() == "incorrectly":
    print("Jheeze... Not a bad start.")
    score += 1
else:
    print("It's the first question bro... Brain AFK?")

#Q2
answer = input("What has a face and two hands, but no arms or legs? ")
if answer.lower() == "clock":
    print("Okaaay, i see you.")
    score += 1
else:
    print("One hit wonder pleb.")

#Q3
answer = input("What 5-letter word becomes shorter when you add two letters to it? ")
if answer.lower() == "short":
    print("Damn, So we got someone who can think outside the box...")
    score += 1
else:
    print("2 Puffs and done.")

#Q4
answer = input("What can you make that no one—not even you—can see? ")
if answer.lower() == "noise":
    print("Nice, your doing pretty well, next one won't be so easy.")
    score += 1
else:
    print("TBF you got halfway, it's something, be proud.")

#Q5
answer = input("What runs, but never walks. Murmurs, but never talks. Has a bed, but never sleeps. And has a mouth, but never eats? ")
if answer.lower() == "river":
    print("GG WP, you got to the end. MadLad")
    score += 1
else:
    print("So close yet so far. KEKW")

print("Well, you've reachd the end, Lets see your score eh?")
print("You got " + str(score) + " riddles correct!")
print("that's " + str((score/5) * 100) + "% correct")
