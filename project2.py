import random
computer = random.randint(1,10)
for i in range(5):
    user = int(input("Enter a number from 1 to 10 to guess:"))
    if user == computer:
        print("Your guess is correct")
        break
    else:
        print("wrong guess please try again")
        i += 1
print(f" computer choosen number is {computer}")