import math
import cmath
import fractions
import bcolors

class bcolors:
    ENDC='\033[0m'
    BOLD='\033[01m' #Maakt vet
    DISABLE='\033[02m' #Maakt lichter
    UNDERLINE='\033[04m' #Onderlijnt
    REVERSE='\033[07m' #Witte achtergrond
    STRIKETHROUGH='\033[09m'
    INVISIBLE='\033[08m'#Maamkt onzichtbaar, duhhh
class text:   
    BLACK='\033[30m'
    RED='\033[31m'
    GREEN='\033[32m'
    ORANGE='\033[33m'
    BLUE='\033[34m'
    PURPLE='\033[35m'
    CYAN='\033[36m'
    LIGHTGREY='\033[37m'
    DARKGREY='\033[90m'
    LIGHTRED='\033[91m'
    LIGHTGREEN='\033[92m'
    YELLOW='\033[93m'
    LIGHTBLUE='\033[94m'
    PINK='\033[95m'
    LIGHTCYAN='\033[96m'
class background:    
    BLACK='\033[40m'
    RED='\033[41m'
    GREEN='\033[42m'
    ORANGE='\033[43m'
    BLUE='\033[44m'
    PURPLE='\033[45m'
    CYAN='\033[46m'
    LIGHTGREY='\033[47m'

print(bcolors.UNDERLINE+"To solve ax2+bx+c=0"+bcolors.ENDC)

a = int(float(input("Enter the value of a:")))
b = int(float(input("Enter the value of b:")))
c = int(float(input("Enter the value of c:")))

D = b**2-4.*a*c
if D<0:
   teller_real = -b 
   noemer = 2.*a

   teller_imag = math.sqrt(-D)

   print("x1=", teller_real,"/", noemer, "+", teller_imag,"i /", noemer)
   print("x2=", teller_real,"/", noemer, "-", teller_imag,"i /", noemer)
   
else:
    x1 = (-b - math.sqrt(D))/(2.*a)
    x2 = (-b + math.sqrt(D))/(2.*a)
    print("x1=", round(x1, 2))
    print("x2=", round(x2, 2))

a = input("Press button to quit")
