import random
import sys

computer = random.choice([1,0,-1])
print("Choose form this Letters")
print("s => snake or w => water or g => gun")
youstr = input("Enter your choice: ")

letter = ["s", "g", "w"]
if youstr not in (letter):
    print("Please Enter The Valide Character!")
    sys.exit()


dict = {"s" : 1, "g" : 0, "w" : -1}
reversedict = {1 : "snake", 0 : "gun", -1 : "water"}

you = dict[youstr]
youchoosed = reversedict[you]
computerchoosed = reversedict[computer]


print(f"You choosed {youchoosed}\ncomputer choosed {computerchoosed}")

if (you == computer):
    print("It's Draw")
else:
    if (computer == 1 and you == -1):
        print("You lose!")
    elif (computer == 0 and you == -1):
        print("You win!")
    elif (computer == -1 and you == 0):
        print("You lose!")
    elif (computer == -1 and you == 1):
        print("You win!")
    elif (computer == 1 and you == 0):
        print("You win!")
    elif (computer == 0 and you == 1):
        print("You lose!")
    else:
        print("Smething went wrong!")