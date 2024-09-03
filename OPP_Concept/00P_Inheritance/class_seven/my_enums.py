from enum import Enum


class grades(Enum):
    A_PLUS = 80
    A = 70
    A_MINUS = 60
    B_PLUS = 55

r1 = grades(80)
print(r1)


