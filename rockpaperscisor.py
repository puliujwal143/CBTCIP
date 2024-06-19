import random
user_choice=int(input("Enter Your Choice: Type 0 for Rock , 1 For Paper, 2 For Scissors."))
if user_choice >=3 or user_choice < 0:
    print("You entered invalid number, you lose.")
else:   
     computer_choice=random.randint(0,2)
     print("Computer Chose:")
     print(computer_choice)
     if computer_choice == user_choice:
       print("It's a Draw.")
     elif computer_choice == 0 and user_choice == 2:
       print("You lose.")
     elif computer_choice == 2 and user_choice ==0:
       print("You win.")
     elif computer_choice > user_choice:
       print("You lose.")
     elif user_choice > computer_choice:
        print("You win")