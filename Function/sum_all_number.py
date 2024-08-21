print("// Summation wit function ")

def SumAllNumber(arg):
    Sum =0
    for value in arg:
        Sum +=value
    return Sum

num =[2,5,6,8,9]
total = SumAllNumber(num)
print(f" The sum of num is = {total}")
num_2 =[2,5,6,8,9,10]
total_1 = SumAllNumber(num_2)
print(f" The sum of num_1 is = {total_1}")

print("// Max of three numbers")
def MaxOfThree(a,b,c):
    Max_num = a
    if Max_num<b:
        Max_num=b
    if Max_num<c:
        Max_num=c
    print(f"Max Number Of {a},{b} and {c} is :",Max_num)
MaxOfThree(40,50,20)

print("// count_unique_characters")
def count_unique_characters(my_String):
    # Initialize an empty dictionary to hold character counts
    char_count = {}

    # Iterate over each character in the string
    for char in my_String:
        # If the character is not in the dictionary, add it with count 1
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Print the characters and their counts
    for char, count in char_count.items():
        print(f"Character: {char}, Count: {count}")


# Example usage
inputString = "Hafizur Rahman"
count_unique_characters(inputString)


