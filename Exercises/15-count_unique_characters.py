# Python program to list unique characters with their count in a string

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


