import matplotlib.pyplot as plt
import numpy as np


def Begin():
    keuze = None #Keuze heeft nu geen waarde/niets
    while keuze is None:
        value = input("Enter a whole positive integer where you want to start with:")
        try:
            keuze = int(value) #int(float(6.3))zou bv. geen error geven.
            if keuze < 0:
                print("This isn't a positive number...\n")
                keuze = None
            else:
                continue
        except ValueError:
            print("This isn't a whole number... \n")
    return keuze
    

keuze_ec=["e", "c"]
def prompt_continue():
    print("What to do next?\n"
          "<c(ontinue)?>\n"
          "<e(xit)?>\n")
    check=input().lower()
    while(check not in keuze_ec):
        check = input("This isn't a choice!").lower()
    return (check == "c") #return () is altijd true or false


def seq_num():
    x = Begin()
    sequence = [x]
    while (x > 1 ):
        if x % 2 == 0:
            x = x//2
        
        else:
            x = x*3+1

        sequence.append(x) #hierdoor wordt een list aangevuld
    return sequence

def range1(x):
    return range(1, x+1)

     
while (1):
    numbers = seq_num() #seq_num() moet ik gelijkstellen aan een 'iets' want anders als ik hem nog eens gebruik roep ik de functie 2x op, en moet ik 2x de input geven. geeft ook fouten 
    elements = len(numbers)
    logaritme = np.log(numbers)
    a = elements + 5
    b = max(numbers)+5
    c = max(logaritme)+5
    x1 = np.array(range1(elements))
    y1 = numbers
    y2 = logaritme
    #Eerste plot
    plt.subplot(1, 2, 1)
    plt.axis([1, a, 0, b])#x, y
    plt.grid(alpha=.4,linestyle='--') #grid
    plt.plot(x1, y1)
    #tweede plot
    plt.subplot(1, 2, 2)
    plt.axis([1, a, 0, c]) #x, y
    plt.grid(alpha=.4,linestyle='--') #grid
    plt.plot(x1, y2)
    print(numbers)
    print("This list has", elements, "elements in it. \n")
    plt.show()
    if prompt_continue(): 
        continue
    else:
        print("See you later!")
        break
   
