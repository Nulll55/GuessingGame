import random
# This will help us select the random number for this game :)

# Prompt the user with the header/intro
print("Guess the number!")

# Main game loop
play_again = "y"
while play_again.lower() == "y":
    #get the user's input for limit
    Limit = (input("\nEnter the limit: ")
    while not Limit.isdigit(): 
        Limit = (input("Value not reconized. Please enter a numeric value: "))
      

    Limit = (input("\nEnter the limit: "))
    while not Limit.isdigit(): 
        Limit = (input("Value not reconized. Please enter a numeric value: "))

    # Will give error if you dont make limit, int after input
    Limit = int(Limit)
    Lower_bound = 1
    num = random.randint(Lower_bound, Limit)

    print(f"\nI'm thinking of a number between {Lower_bound} and {Limit}!")
    
    guess = none
    tries = 0

    while guess != num:
        user_input = input("Enter your guess: ")
        
        if not uder_input.isdigit():
            print("Please enter a valid number.")
            continue
        
        guess = int(user_input)
        tries += 1
        
        if guess < num:
            print("Too low.")
        elif guess > num:
            print("Too High.")
        else:
        print(f"
        print(f"You got it in {tries} guesses!\n")      


# Ask to play again
    play_again = input("Would you like to play again? (y/n): ").lower()
    while play_again not in ("y", "n"):
        play_again = input("Invalid input. Please enter 'y' or 'n': ").lower()


print("Thanks for playing! Goodbye!")
# Bye! <3