import random
user_number = 0
computer_score = 0

for i in range(1, 4): 
    print(f"Round {i}")
    
    my_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)
    
    print("User_number:", my_number)

    Guess = input("Which number do you think is greater? Type 'high' or 'low': ").lower()
    
    print("Computer_number:", computer_number)

    if my_number > computer_number:
        if Guess == 'user':
            print("You get a point!")
            user_number += 1
        else:
            print("No point.")
    elif my_number < computer_number:
        if Guess == 'computer':
            print("Computer gets a point!")
            computer_score += 1
        else:
            print("No point.")
    else:
        print("It's a tie! No points awarded.")
    
   