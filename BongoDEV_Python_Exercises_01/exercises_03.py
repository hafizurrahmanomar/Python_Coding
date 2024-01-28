''' Exercise 03: Write a function that takes 2 numbers as arguments (age of two brothers)
and find who is elder
Hints: Use condition inside the function '''

def find_elder_brother(Nayeem_Age, Toha_Age):
    if Nayeem_Age > Toha_Age:
        return " Nayeem is elder Brother "
    elif Nayeem_Age  < Toha_Age:
        return "Toha is elder."
    else:
        return "Nayeem and Toha are of the same age."

# Example usage:
Nayeem_Age = 16
Toha_Age = 10

result = find_elder_brother(Nayeem_Age, Toha_Age)
print(result)


