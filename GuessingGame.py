import random
# This will help us select the random number for this game :)

# Prompt the user with the header/intro
print("Guess the number!")

# get users input

Limit = (input("\nEnter the limit: "))
while not Limit.isdigit(): 
    Limit = (input("Value not reconized. Please enter a numeric value: "))
# create a loop to fact check that its a number

Limit = (int(Limit))
Lower_bound = 1
num = random.randint(Lower_bound, Limit)

print("\fnum")
# if num
# Too low.
# Too high.
# if the guess is correct, display message and exit loop

# You gussed it in {} tries.

# Would you like to play again? (y/n): y
# Write a condition to fact check that it is y or n

# Bye! <3
