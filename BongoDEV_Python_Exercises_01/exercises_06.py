'''
Exercise 06: Write a function named “isLandscape” that takes 2 numbers (image width
and height) as arguments and the function returns Landscape if the image width has a
higher value than height. Returns Portrait otherwise
Hints: Use condition inside the function
'''


def isLandscape(width, height):
    if width > height:
        return "Landscape"
    else:
        return "Portrait"

# Example usage:
image_width = 800
image_height = 600

result = isLandscape(image_width, image_height)
print(result)
