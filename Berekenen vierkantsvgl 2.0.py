
import math
import cmath
import fractions


print("To solve ax2+bx+c=0")

a = int(float(input("Enter the value of a:")))
b = int(float(input("Enter the value of b:")))
c = int(float(input("Enter the value of c:")))

D = b**2-4.*a*c
if D<0:
   teller_real = -b 
   noemer = 2.*a

   teller_imag = math.sqrt(-D)

   print("x1=", fractions.Fraction(teller_real/noemer), "+", teller_imag,"i /", noemer)
   print("x2=", fractions.Fraction(teller_real/noemer), "-", teller_imag,"i /", noemer)
   
else:
    x1 = (-b - math.sqrt(D))/(2.*a)
    x2 = (-b + math.sqrt(D))/(2.*a)
    print("x1=", x1)
    print("x2=", x2)

a = input("Press button to quit")

