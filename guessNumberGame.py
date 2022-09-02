import random
secretNumber = random.randint(1,20)

for guessesTaken in range(1,6):
    print(" You Can Guess Your Number ")
    guess=int(input())

    if guess < secretNumber:
        print(" Your Guess Is Too Low ")
    elif guess > secretNumber:
        print(" Your Guess Is Too High ")
    else:    
      break    

if guess == secretNumber:
    print(' You Guessed My Number Correctly ' + str(guessesTaken))
else:
    print(" I Was Guess Some Other Number " + str(secretNumber))