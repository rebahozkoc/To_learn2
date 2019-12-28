import sys
import math
a=sys.argv[1]
b=sys.argv[2]
c=sys.argv[3]
def quadratic_formula(a,b,c):
    discriminant = float(b)**2 - 4*float(a)*float(c)
    if pow(int(b),2)-4*int(a)*int(c)<0:
        print("There is no solution")
    elif pow(int(b),2)-4*int(a)*int(c)==0:
        print("""There are one solution
Solution(s):""",(-int(b))/(2*int(a)))
    else:
        print("""There are two solutions
Solution(s):""",(-float(b)-math.sqrt(discriminant))/2*float(a), (-int(b)-(pow(int(b),2)-4*int(a)*int(c))**1/2)/2*int(a))
quadratic_formula(sys.argv[1],sys.argv[2],sys.argv[3])






