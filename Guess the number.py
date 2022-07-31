#Create a game where the person has to guess a number with a limited number of guesses i.e 5 guess
n = 50
i = int(input("Enter a number\n"))
b = 9 #number of guesses
while(True):

    b = b - 1


    if i>n:
        if b == 0:  # when no of guesses left are 0
            print("Game over, Better luck next time!")
        # when the number guessed by the person is greater than 30

        print("You are guessing a higher number, Try again!" , "no of guesses", b)
        i = int(input())

        continue
    elif i<n:
        if b == 0:  # when no of guesses left are 0
            print("Game over, Better luck next time!")
            break
        # when the number guessed by the person is lesser than 30
        print("You are guessing a smaller number, Try again!", "no of guesses", b)
        i = int(input())

        continue
    elif i == n: #when the guessed number = 30
        print("Congrats you have guessed the number")
        print("No of guesses left", b)
        break
