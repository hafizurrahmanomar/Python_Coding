# Problem-01: Take the heights of your 2 friends (in inches) as input and print their average height!

# Solution

height1 = float(input("Enter the height of the first friend in inches: "))
height2 = float(input("Enter the height of the second friend in inches: "))
average_height = (height1 + height2) / 2
feet = int(average_height // 12)
inches = int(average_height % 12) 
print("The average height is", feet, "feet", inches, "inches")
