import random
print("********WELCOME TO HAND CRICKET*******")
user = input("Do you want to play the game?!!\n")
if user.lower() == "yes":
    print("****GAME BEGINS****")
    msg = (input("press any key to continue\n"))
    com = True
    player = False
    score = 0
    while com != player:
        try:

            player = int(input("enter your number b/w [0,6]\n"))
            com = random.randint(0, 6)

            if -1 < player < 7:
                print(f"you hit a {player}")
                print(f"computer chose {com}")
                if com != player:
                    score += player
            else:
                print(
                    "*********you can only choose b/w [0,6]***************\n You are OUT")
                break
        except:
            print("enter a valid integer with no special characters or any other symbol")
    print(f"You scored: {score}")
else:
    print("THANKS FOR VISITING")


# add high score saving name entry too
