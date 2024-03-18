# Rock-Paper-Scissor Game 
# Author- Rajat Gupta Sec-B 18-03-2024
import random as rnd

possibilities = ["rock","paper","scissor"]
print("Possibilities list: ",possibilities)

def game(possibilities):
    while(True):
        print("--------------------")
        p1 = rnd.choice(possibilities)
        print("Player 1 chose: ",p1)
        p2 = rnd.choice(possibilities)
        print("Player 2 chose: ",p2)
        p1 = p1.lower()
        p2 = p2.lower()
        
        if p1 == p2:
            print('Tie')
            continue
        elif p1 == "rock":
            if p2 == "scissor":
                print("Player 1 wins")
                break
            else:
                print("Player 2 wins")
                break
        elif p1 == "paper":
            if p2 == "rock":
                print("Player 1 wins")
                break
            else:
                print("Player 2 wins")
                break
        else:
            if p2 == "paper":
                print("Player 1 wins")
                break
            else:
                print("Player 2 wins")
                break
     

while(True):
    print("--------------------")
    print("Press 1 to start the game: ")
    print("Press 2 to terminate: ")
    inp = int(input('Choose: '))
    
    if inp == 1:
        game(possibilities)
        continue
    elif inp == 2:
        print("Game ended!")
        break
    else:
        print('Invalid input. Try again!')

    
        