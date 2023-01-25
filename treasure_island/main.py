from art import logo
print(logo)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


choice1 = input("You're at a crossroad, where do you want to go? Type 'left' or 'right' ").lower()
if choice1 == 'right':
    print("Fall into a hole. Game Over.")
if choice1 == 'left':
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
    if choice2 == 'swim':
        print("Attacked by trout. Game Over.")
    if choice2 == 'wait':    
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? \n").lower()
        if choice3 == 'red':
            print("Burned by fire. Game Over.")
        elif choice3 == 'blue':
            print("Eaten by beasts. Game Over.")
        elif choice3 == 'yellow':
            print("You Win!")
        else :
            print("Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")
