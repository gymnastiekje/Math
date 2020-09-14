
import math
import cmath
import fractions


print("To solve ax²+bx+c=0")

a = int(float(input("Enter the value of a:")))
b = int(float(input("Enter the value of b:")))
c = int(float(input("Enter the value of c:")))

D = b**2-4.*a*c
if D<0:
   teller_1 = -b + cmath.sqrt(D)
   noemer_1 = 2.*a

   teller_2 = -b - cmath.sqrt(D)
   noemer_2 = 2.*a

   print("x1=", fractions.Fraction(teller_1.real/noemer_1), "+", teller_1.imag,"i /", noemer_1)
   print("x2=", fractions.Fraction(teller_2.real/noemer_2), teller_2.imag,"i /", noemer_2)
   
else:
    x1 = (-b - math.sqrt(D))/(2.*a)
    x2 = (-b + math.sqrt(D))/(2.*a)
    print("x1=", x1)
    print("x2=", x2)

a = input("Press button to quit")

