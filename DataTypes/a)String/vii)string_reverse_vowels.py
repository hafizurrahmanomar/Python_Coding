def string_reverse(input_string):
    return input_string[::-1]


original_string = "Hello Python Programmer"
Reverse_String = string_reverse(original_string)

print("Reverse String Print Now: ", Reverse_String.upper())


def vowels_count(input_text):
    vowels = "aeiouAEIOU"
    return sum(1 for Chr in input_text if Chr in vowels)


text = "Hello Python Programmer,How Are You"
total_vowel = vowels_count(text)
print(" Original Text:", text)
print("Total Vowels in text:", total_vowel)
