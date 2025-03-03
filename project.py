import random
while True:
    computer = random.choice([1,0,-1])
    youstr = input("Enter your choice(\"R\" for Rock, \"P\" for Paper, \"S\" for Scissor): ").upper()
    if youstr == 'Q':
        print("Thanks for Playing")
        break
    dict1 = {"R": 1, "P": 0, "S": -1}
    if youstr not in dict1:
        print("Invalid option please enter 'R' for rock, 'p' for paper, 'S' for scissor" )
    else:
        younum = dict1[youstr]
        reversedict1 = {1:"R", 0:"P", -1:"S"}
        print(f"your choice is {reversedict1[younum]} and computer choice is {reversedict1[computer]}")
        
        if computer == younum:
            print("Draw")
        else:
            if (computer == 0) and (younum == 1): 
                print("You Lose")
            elif (computer == 0) and (younum == -1):
                print("You Win")
            elif (computer == 1) and (younum == -1):
                print("You Lose")
            elif (computer == 1) and (younum == 0):
                print("You Win")
            elif (computer == -1) and (younum == 0):
                print("You Lose")
            elif (computer == -1) and (younum == 1):
                print("You Win")
            else:
                print("something went wrong")