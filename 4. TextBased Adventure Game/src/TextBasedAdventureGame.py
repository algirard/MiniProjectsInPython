
print("You enter a dark room with two doors. Do you want to enter door #1 or door #2?")
door = input("> ") 
if door == "1":
    print("Theres a giant bear eating what appears to be a human arm, though its so damaged it\'s hard to be sure")
    print("What do you want to do?")
    print("#1 try to take the arm")
    print("#2 scream at the bear")

    bear = input("> ")

    if bear == "1":
        print("You approach the bear slowly, never breaking eye contact. After what feel like a thousand years you are finally face to face with the bear. \nYou grab the arm and pull. of course the bear responds by eating you face. well done!")

    elif bear == "2":
        print("You scream at the bear, a decent sound as well. The bear however was not impressed it would seem \nas he insantly eats your face. Well done!")

    else:
        print("Well, doing %s is probably better. Bear runs away.") % bear

elif door == "2":
    print("You stare into the endless abyss of Bollofumps retina.")
    print("Oh dear, seems the insanity of Bollofumps existence had driven you quite insane.")
    print("#1. drool")
    print("#2. scream and drool")
    print("#3. Understand the fabrics of molecula toy crafting")
    insanity = input("> ")

    if insanity == "1" or "2":
        print("Your body survives, powered by pure insanity!")

    else:
        print("your mind melts into green flavoured jello! mmm!")

else:
    print("You think for a while but suddenly a troll weilding a terrible looking knife comes through a trap door and shanks you!")
    