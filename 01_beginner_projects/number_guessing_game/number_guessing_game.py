from random import randint
attempts = 0
computer_choice = randint(1, 100)
print("Welcome to the number guessing game")
print("I am thinking of a number between 1 and 100")
playing = True
while playing:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess == computer_choice:
        print(f"You got it! The number is {computer_choice}")
        attempts += 1
        print(f"Total attempts = {attempts}")
        playing = False
        choice = input("Do you wish to continue? 'y' for yes and 'n' for no: ").lower()
        if choice == 'y' or choice == 'yes':
            computer_choice = randint(1, 100)
            playing = True
            attempts = 0
        elif choice == 'n' or choice == 'no':
            playing = False
            print("Thanks for playing!")
        else:
            print("Invalid input!")
            playing = True

    elif guess > computer_choice:
        print("Too high")
        print("Guess again")
        attempts += 1
        print(f"Total attempts = {attempts}")
    else:
        print("Too low")
        print("Guess again")
        attempts += 1
        print(f"Total attempts = {attempts}")
