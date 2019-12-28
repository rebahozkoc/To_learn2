import sys
import math


def quadratic_equation(input_list):
    a = float(input_list[1])
    b = float(input_list[2])
    c = float(input_list[3])
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt((b**2)-4*a*c))/(2*a)
        root2 = (-b - math.sqrt((b**2)-4*a*c))/(2*a)
        print("There are two solutions")
        print("Solution(s): {0:.2f}, {1:.2f}".format(root1, root2))
    elif discriminant == 0:
        root = (-b + math.sqrt((b**2)-4*a*c))/(2*a)
        print("There is one solution")
        print("Solution(s): {0:.2f}".format(root))
    else:
        print("There is no solution")


quadratic_equation(sys.argv)
