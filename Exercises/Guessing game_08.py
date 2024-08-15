'''Exercise 08: Guessing game
Write a function that takes a number 1 to 9 from the user input (use input function inside
a function). Store a number in a variable (let’s assume 6). If the input value is less than
the variable, print (your guess is almost there), if the input value is greater than the
variable, print - your guess is higher, if the input value and variable are equals, print -
Your Guess Is Correct! '''

def guess_number():
    # Assume the variable is 6
    my_number = 7

    # Get user input
    user_input = int(input("Enter a number between 1 and 9: "))

    # Compare user input with the correct number
    if user_input < my_number:
        print("Your guess is almost there. Your guess is too low.")
    elif user_input > my_number:
        print("Your guess is higher. Your guess is too high.")
    else:
        print("Your guess is correct! Congratulations!")

# Call the function
guess_number()
