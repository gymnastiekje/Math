import math


def set_variable(name):
    keuze=None #Keuze_a heeft nu geen waarde/niets
    while (not keuze): #Zolang er geen keuze is/keuze niet bestaat, blijft de loop gaan
        value = input(f"Enter the value of {name}:") #De f zorgt ervoor dat python naar name gaat zoeken 
        try:
            keuze = float(value)
        except ValueError:
            print(f"This wasn't a value number for '{name}' lolbroek!")
    return keuze


def teller_noemer(a,b,c): #Ik zorg hier voor dat a, b en c de input van deze functie wordt. Volgorde functies maakt nu niet meer uit.
   D = b**2-4.*a*c
   if D<0:
       teller_real = -b 
       noemer = 2.*a
       teller_imag = math.sqrt(-D)
       
       x1 = teller_real, '/', noemer, '+', teller_imag,'i /', noemer
       x2 = teller_real, '/', noemer, '-', teller_imag,'i /', noemer
      
   else:
       x1 = (-b - math.sqrt(D)),"/",(2.*a)
       x2 = (-b + math.sqrt(D)),"/",(2.*a)
       
   return x1, x2

keuze_ec=["e", "c"]
def prompt_continue():
    print("What to do next?\n"
          "<c(ontinue)?>\n"
          "<e(xit)?>\n")
    check=input()
    if check == "e":
        return False
    elif check == "c":
        return True
    while(check not in keuze_ec):
        check = input("Dit was geen keuze lolbroek!:")
        if check == "e":
            return False
        elif check == "c":
            return True

#De inputs voor de functie moeten in de while
#Anders geef je de input 1x in, en slaat de while alleen op de print.


while(1):
    a = set_variable("a")
    b = set_variable("b")
    c = set_variable("c")
    x1,x2=teller_noemer(a,b,c) #Ik zorg ervoor dat de output van de functie x1, x2 wordt
    print("x1 = ", x1, "\n"
          "x2 = ", x2)
    if prompt_continue()==True: #True moet niet aangezien if al checkt of het true is
        continue
    else:
        print("See you next time!")
        break
