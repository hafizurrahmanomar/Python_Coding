# Python program to find number of vowels in a given string.

def vowels_count(input_text):
    vowels = "aeiouAEIOU"
    return sum(1 for Chr in input_text if Chr in vowels)


text = "Hello Python Programmer,How Are You?"
total_vowel = vowels_count(text)
print("Total Vowels in text:", total_vowel)
