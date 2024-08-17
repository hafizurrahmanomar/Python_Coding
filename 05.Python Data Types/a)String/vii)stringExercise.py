def String_Reverse(input_string):
    return input_string[::-1]


original_string = "Hello Python Programmer"
Reverse_String = String_Reverse(original_string)

print("Reverse String Print Now: ", Reverse_String.upper())


def vowels_Cunt(input_text):
    vowels = "aeiouAEIOU"
    return sum(1 for chr in input_text if chr in vowels)


text = "Hello Python Programmer,How Are You"
total_vowel = vowels_Cunt(text)
print(" Original Text:", text)
print("Total Vowels in text:", total_vowel)
