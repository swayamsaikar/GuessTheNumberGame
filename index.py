import random

chances = 0
while chances < 5:
    chances = chances +1
    guess = int(input('Guess a number between (1 and 9) :- '))
    number = random.randint(1, 9)
    
    if(guess > number):
        print("Your guess is greater than the number , try entering less than ")
        print(guess)

    elif(guess < number):
        print("Your Guessed is slightly less Than the number , try entering greater than")
        print(guess)
        
    elif(guess > 9):
        print("Your guessed number is greater the 9")
        
    elif(guess < 0):
        print("Your guessed number is less than 0")
        
    elif(guess == number):
        print("Congratulations ! YOU WON")
        
    if(chances == 5):
        print("YOU LOSE")    
        
