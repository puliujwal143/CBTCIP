import random
number = random.randrange(1000, 10000) 
a = int(input("Guess the 4 digit number:"))
if(a == number):
    print("Great! You guessed the number in just 1 try! You're a Mastermind!")
else:
    b = 0
    while(a != number):
        b += 1
        c = 0
        a = str(a)
        number = str(number)
        correct = []
        for i in range(0, 4):
            if(a[i] == number[i]):
                c += 1
                correct.append(a[i])
            else:
                continue
        if (c < 4) and (c != 0):
            print("Not quite the number. But you did get ",
                  c, " digit(s) correct!")
            print("Also these numbers in your input were correct.")
 
            for d in correct:
                print(d, end=' ')
            print('\n')
            print('\n')
            a = int(input("Enter your next choice of numbers: "))
        elif(c == 0):
            print("None of the numbers in your input match.")
            a = int(input("Enter your next choice of numbers: "))
    if a == number:
        print("You've become a Mastermind!")
        print("It took you only", b, "tries.")