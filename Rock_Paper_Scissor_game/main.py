import random
from art import img
choose = input("What do you choose? Type 0 for 'Rock', 1 for 'Paper', 2 for 'Scissors'.")
choose_img = int(choose)
print(f"{choose}\n",img[choose_img])


choose_computer_img = random.randint(0,2)
print(f"Computer choose:\n",img[choose_computer_img])


if choose_img == 0 :
    if choose_computer_img == 0 :
        print("Draw")
    elif choose_computer_img == 1 :
        print("You lose")
    else :
        print("You win!!") 
elif choose_img == 1:
    if choose_computer_img == 1 :
        print("Draw")
    elif choose_computer_img == 2 :
        print("You lose")
    else :
        print("You win!!") 
else:
    if choose_computer_img == 2 :
        print("Draw")
    elif choose_computer_img == 0 :
        print("You lose")
    else :
        print("You win!!") 